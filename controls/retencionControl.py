from models.retencion import Retencion
from controls.dao.historialRetencion import HistorialRetencion
from controls.tda.linkedList import LinkedList
import os

class RetencionControl:
    def __init__(self):
        self.historial = LinkedList()
        self.dao = HistorialRetencion()
        self.cargarHistorial()

    def agregarRetencion(self, factura):
        nueva_retencion = Retencion(factura)  # Utiliza el nombre de la clase para crear la instancia
        self.historial.append(nueva_retencion)
        self.dao.guardarHistorial(self.historial)

        folder_path = 'partica/Taller/data'

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        return nueva_retencion

    def cargarHistorial(self):
        self.historial = self.dao.cargarHistorial()

    def mostrarHistorial(self):
        return list(self.historial)
