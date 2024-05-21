from models.factura import Factura
from controls.exception.facturaError import ErrorRUC

class FacturaControl:
    def __init__(self):
        self.facturas = []

    def crearFactura(self, numero, ruc, monto, tipo_ruc):
        if tipo_ruc not in ['educativo', 'profesional']:
            raise ErrorRUC(tipo_ruc)        
        factura = Factura(numero=numero, ruc=ruc, monto=monto, tipo_ruc=tipo_ruc)
        self.facturas.append(factura)        
        return factura

    def obtenerFactura(self, numero):
        for factura in self.facturas:
            if factura.numero == numero:
                return factura
        return None

    def eliminarFactura(self, numero):
        factura = self.obtenerFactura(numero)
        if factura:
            self.facturas.remove(factura)
            return True
        return False

    def editarFactura(self, numero, nuevo_numero, nuevo_ruc, nuevo_monto, nuevo_tipo_ruc):
        factura = self.obtener_factura(numero)
        if factura:
            factura.numero = nuevo_numero
            factura.ruc = nuevo_ruc
            factura.monto = nuevo_monto
            factura.tipo_ruc = nuevo_tipo_ruc
            return factura
        return None
