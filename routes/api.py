from flask import Blueprint, jsonify, make_response, request
from controls.facturaControl import FacturaControl
from controls.retencionControl import RetencionControl
from controls.exception.facturaError import ErrorRUC
from flask_cors import CORS

api = Blueprint('api', __name__)
CORS(api)

facturaControl = FacturaControl()
retencionControl = RetencionControl()

@api.route('/')
def home():
    return make_response(
        jsonify({"msg": "OK", "code": 200}),
        200
    )

@api.route('/facturas', methods=['POST'])
def guardarFactura():
    data = request.json
    try:
        factura = FacturaControl.crearFactura(data['numero'], data['ruc'], data['monto'], data['tipo_ruc'])
        retencion = RetencionControl.agregarRetencion(factura)
        return make_response(
            jsonify({"msg": "Factura y retención guardadas correctamente", "code": 200, "data": retencion.to_dict()}),
            200
        )
    except ErrorRUC as e:
        return make_response(
            jsonify({"msg": str(e), "code": 400}),
            400
        )
    except KeyError as e:
        return make_response(
            jsonify({"msg": f"Falta el campo {str(e)}", "code": 400}),
            400
        )

@api.route('/api/retenciones', methods=['GET'])
def listaRetenciones():
    historial = retencionControl.mostrarHistorial()
    return make_response(
        jsonify({"msg": "OK", "code": 200, "data": [ret.to_dict() for ret in historial]}),
        200
    )
