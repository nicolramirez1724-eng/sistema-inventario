import json
import config
RUTA = config.ruta_absoluta/"data/producto.json"
def historial_producto():
    codigo = input("Código del producto: ")

    with open(RUTA, "r") as f:
        productos = json.load(f)

    for p in productos:
        if p["codigo"] == codigo:
            movimientos = p.get("movimientos", [])
            for m in movimientos:
                print(m)
            return

    print("Producto no encontrado")

def reporte():
    with open(RUTA, "r") as f:
        productos = json.load(f)

    texto_reporte = ""

    for p in productos:
        linea = f"\nProducto: {p['nombre']}\n"
        print(linea)
        texto_reporte += linea

        total = 0
        stock = p.get("stock", {})

        for bodega, cantidad in stock.items():
            linea = f"{bodega}: {cantidad}\n"
            print(linea)
            texto_reporte += linea
            total += cantidad

        linea = f"Total: {total}\n"
        print(linea)
        texto_reporte += linea

    opcion = input("¿Desea guardar el reporte en archivo txt? (s/n): ").lower()

    if opcion == "s":
        try:
            with open(config.ruta_absoluta/"reporte.txt", "a") as f:
                f.write(texto_reporte)
            print("Reporte guardado en reporte.txt")
        except:
            print("Error al guardar el archivo")