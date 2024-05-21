class Factura:
    def __init__(self, numero, ruc, monto, tipo_ruc):
        self.numero = numero
        self.ruc = ruc
        self.monto = monto
        self.tipo_ruc = tipo_ruc

    @property
    def _numero(self):
        return self.numero

    @_numero.setter
    def _numero(self, value):
        self.numero = value

    @property
    def _ruc(self):
        return self.ruc

    @_ruc.setter
    def _ruc(self, value):
        self.ruc = value

    @property
    def _monto(self):
        return self.monto

    @_monto.setter
    def _monto(self, value):
        self.monto = value

    @property
    def _tipo_ruc(self):
        return self.tipo_ruc

    @_tipo_ruc.setter
    def _tipo_ruc(self, value):
        self.tipo_ruc = value

    def to_dict(self):
        return {
            'numero': self.numero,
            'ruc': self.ruc,
            'monto': self.monto,
            'tipo_ruc': self.tipo_ruc
        }
    
    def __str__(self):  
        return f'Numero: {self.numero}, Ruc: {self.ruc}, Monto: {self.monto}, Tipo Ruc: {self.tipo_ruc}'  
    

