import producto,historial


def registrar_producto():
    print("registrar producto")
    producto.agregar_roducto()
def ingresar_producto():
    print("ingresar producto")
    producto.ingresar_producto()
def retirar_producto():
    print("retirar producto")
    producto.retirar_producto()
def buscar_producto():
    print("buscar producto")
    producto.buscar_producto()
def historial_producto():
    print("historial producto")
    historial.historial_producto()
def reporte():
    print("reporte")
    historial.reporte()


while True:
    print("1.registro de productos")
    print("2. ingresar producto")
    print("3.sacar productos del nventario")
    print("4.buscar producto")
    print("5.historial de producto")
    print("6.reporte")
    print("7.salir")
    op=input ("digite opcion")

    if op=="1":
        registrar_producto()
    elif op=="2":
        ingresar_producto()
    elif op=="3":
        retirar_producto()
    elif op == "4":
        buscar_producto()
    elif op == "5":
        historial_producto()
    elif op == "6":
        reporte()
    elif op == "7":
        print ("gracias por usar el sistema")
        break