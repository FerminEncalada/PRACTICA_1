from controls.facturaControl import FacturaControl
from controls.retencionControl import RetencionControl
from controls.exception.facturaError import ErrorRUC

def main():
    facturaControl = FacturaControl()
    retencionControl = RetencionControl()

    while True:
        print("\n1. Ingresar nueva factura")
        print("2. Mostrar historial de retenciones")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            numero = input("Ingrese el número de la factura: ")
            ruc = input("Ingrese el RUC: ")
            monto = float(input("Ingrese el monto: "))
            tipo_ruc = input("Ingrese el tipo de RUC (educativo/profesional): ").lower()
            try:
                factura = facturaControl.crearFactura(numero, ruc, monto, tipo_ruc)
                retencionControl.agregarRetencion(factura)
            except ErrorRUC as e:
                print(e.message)
        elif opcion == '2':
            retencionControl.mostrarHistorial()
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

