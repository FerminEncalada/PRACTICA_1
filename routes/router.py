from flask import Blueprint, render_template, redirect, request, make_response
from controls.facturaControl import FacturaControl
from controls.retencionControl import RetencionControl
from controls.exception.facturaError import ErrorRUC

router = Blueprint('router', __name__)

facturaControl = FacturaControl()
retencionControl = RetencionControl()

@router.route('/')
def home():
    return render_template('home.html')

@router.route('/facturas')
def verFacturas():
    historial = retencionControl.mostrarHistorial()
    return render_template('facturas/lista.html', lista=historial)

@router.route('/facturas/formulario')
def verGuardar():
    return render_template('facturas/guardar.html')

@router.route('/facturas/guardar', methods=['POST'])
def guardarFactura():
    data = request.form
    try:
        factura = facturaControl.crearFactura(data['numero'], data['ruc'], float(data['monto']), data['tipo_ruc'])
        retencionControl.agregarRetencion(factura)
        return redirect('/facturas', code=302)
    except ErrorRUC as e:
        return make_response(str(e), 400)
    except KeyError as e:
        return make_response(f"Falta el campo {str(e)}", 400)

@router.route('/facturas/editar/<int:numero>', methods=['GET', 'POST'])
def editarFactura(numero):
    if request.method == 'GET':
        factura = facturaControl.obtenerFactura(numero)
        if factura:
            return render_template('facturas/editar.html', factura=factura)
        else:
            return make_response("Factura no encontrada", 404)
    elif request.method == 'POST':
        data = request.form
        try:
            nueva_factura = facturaControl.editarFactura(numero, data['nuevo_numero'], data['nuevo_ruc'], float(data['nuevo_monto']), data['nuevo_tipo_ruc'])
            if nueva_factura:
                return redirect('/facturas', code=302)
            else:
                return make_response("Factura no encontrada", 404)
        except KeyError as e:
            return make_response(f"Falta el campo {str(e)}", 400)

@router.route('/facturas/eliminar/<int:numero>', methods=['POST'])
def eliminarFactura(numero):
    if request.method == 'POST':
        if facturaControl.eliminarFactura(numero):
            return redirect('/facturas', code=302)
        else:
            return make_response("Factura no encontrada", 404)

