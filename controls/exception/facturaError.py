class FacturaError(Exception):
    pass

class ErrorRUC(FacturaError):
    def __init__(self, tipo_ruc):
        self.tipo_ruc = tipo_ruc
        self.message = f"Tipo de RUC inválido: {self.tipo_ruc}"
        super().__init__(self.message)
