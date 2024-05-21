import json
from models.retencion import Retencion
from models.factura import Factura
from controls.tda.linkedList import LinkedList

class HistorialRetencion:
    def __init__(self, filename='historial_retenciones.json'):
        self.filename = filename

    def guardarHistorial(self, historial):
        with open(self.filename, 'w') as file:
            json.dump([ret.__dict__ for ret in historial], file, indent=4, default=lambda o: o.__dict__)

    def cargarHistorial(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                historial = LinkedList()
                for item in data:
                    factura_data = item['factura']
                    factura = Factura(**factura_data)
                    retencion = Retencion(factura)
                    historial.append(retencion)
                return historial
        except FileNotFoundError:
            return LinkedList()
