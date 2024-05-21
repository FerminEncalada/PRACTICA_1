from models.factura import Factura

class Retencion:
    def __init__(self, factura: Factura):
        self.factura = factura
        self.retencion = self.calcularRetencion()

    def calcularRetencion(self):
        if self.factura.tipo_ruc == 'educativo':
            return self.factura.monto * 0.08
        elif self.factura.tipo_ruc == 'profesional':
            return self.factura.monto * 0.10
        else:
            return 0

    def to_dict(self):
        return {
            'factura': self.factura.to_dict(),
            'retencion': self.retencion
        }

    def __repr__(self):
        return f"Factura Nro: {self.factura.numero}, RUC: {self.factura.ruc}, Monto: {self.factura.monto}, Retención: {self.retencion}"
