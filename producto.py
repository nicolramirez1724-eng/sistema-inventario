import json
from datetime import *
def cargar_datos():
    try:
        with open("data/producto.json","r") as f:
            lista = json.load(f)
    except:
        print("no se pudo leer el json")

def agregar_roducto():
    try:
        codigo=input("digite el codigo del producto:")
        nombre=input("digite el nombre del producto:")
        proveedor=input("digite el proveedor del producto:")

        producto=dict(
            codigo=codigo,
            nombre=nombre,
            proveedor=proveedor
        )
        list=[]
        with open("data/producto.json","r") as f:
            list = json.load(f)
        list.append(producto)
        with open("data/producto.json","w") as f:
            json.dump(list,f,indent=4)
    except:
        print("no se puede agregar producto")

def ingresar_producto():
    try:
        codigo = input("Código del producto: ")
        bodega = input("Bodega (Norte, Centro, Oriente): ")
        cantidad = int(input("Cantidad a ingresar: "))
        descripcion = input("Descripción: ")

        with open("data/producto.json", "r") as f:
            productos = json.load(f)

        encontrado = False

        for p in productos:
            if p["codigo"] == codigo:
                if "stock" not in p:
                    p["stock"] = {}

                if bodega not in p["stock"]:
                    p["stock"][bodega] = 0

                p["stock"][bodega] += cantidad

                # historial
                if "movimientos" not in p:
                    p["movimientos"] = []

                p["movimientos"].append({
                    "tipo": "entrada",
                    "bodega": bodega,
                    "cantidad": cantidad,
                    "descripcion": descripcion,
                    "fecha": str(datetime.now())
                })

                encontrado = True
                break

        if not encontrado:
            print("Producto no encontrado")
            return

        with open("data/producto.json", "w") as f:
            json.dump(productos, f, indent=4)

        print("Producto ingresado correctamente")

    except Exception as e:
        print("Error:", e)

def retirar_producto():
    try:
        codigo = input("Código del producto: ")
        bodega = input("Bodega: ")
        cantidad = int(input("Cantidad a retirar: "))
        descripcion = input("Descripción: ")

        with open("data/producto.json", "r") as f:
            productos = json.load(f)

        for p in productos:
            if p["codigo"] == codigo:
                if "stock" in p and bodega in p["stock"]:
                    if p["stock"][bodega] >= cantidad:

                        p["stock"][bodega] -= cantidad

                        if "movimientos" not in p:
                            p["movimientos"] = []

                        p["movimientos"].append({
                            "tipo": "salida",
                            "bodega": bodega,
                            "cantidad": cantidad,
                            "descripcion": descripcion,
                            "fecha": str(datetime.now())
                        })

                        with open("data/producto.json", "w") as f:
                            json.dump(productos, f, indent=4)

                        print("Retiro exitoso")
                        return
                    else:
                        print("Stock insuficiente")
                        return

        print("Producto no encontrado")

    except Exception as e:
        print("Error:", e)

def buscar_producto():
    codigo = input("Código del producto: ")

    with open("data/producto.json", "r") as f:
        productos = json.load(f)

    for p in productos:
        if p["codigo"] == codigo:
            print("Nombre:", p["nombre"])
            print("Proveedor:", p["proveedor"])
            print("Stock:", p.get("stock", {}))
            return

    print("Producto no encontrado")
