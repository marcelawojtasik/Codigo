"""
Estructura del inventario de productos
inventario = {
    id: {
        "nombre": "_nombre",
        "descripcion": "_descripcion",
        "cantidad": _cantidad,
        "precio": _precio,
        "categoria": "_categoria"
    },
}
"""
inventario ={} #diccionario de productos
codigo_actual =1 #Contador para generar códigos únicos

def mostrar_menu():
    print("Menú de Gestión de Inventario:")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Buscar producto")
    print("6. Reporte de Bajo Stock")
    print("7. Salir")


def registrar_producto():
    global codigo_actual 
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese una breve descripción: ")
    cantidad = int(input("Ingrese la cantidad disponible: "))
    precio = float(input("Ingrese el precio del producto: "))
    categoria = input("Ingrese la categoría del producto: ")

#Agregar el producto al diccionario 'inventario'
    inventario[codigo_actual] ={
        "nombre": nombre,
        "descripcion" : descripcion,
        "cantidad" : cantidad,
        "precio" : precio,
        "categoria" : categoria
        }
    print("Producto registrado con el código",codigo_actual)
    codigo_actual +=1

    
def mostrar_productos():
    if not inventario:
        print("El inventario está vacío.")
    else:
        for codigo, datos in inventario.items():
            print(f"Código: {codigo}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Descripción: {datos['descripcion']}")
            print(f"Cantidad: {datos['cantidad']}")
            print(f"Precio: {datos['precio']}")
            print(f"Categoría: {datos['categoria']}")
            print("-" * 30)

def buscar_producto():
    codigo = int(input("Ingrese el código del producto a buscar: "))
    if codigo in inventario:
        datos = inventario[codigo]
        print("Nombre:", datos['nombre'])
        print("Descripción:", datos['descripcion'])
        print("Cantidad:", datos['cantidad'])
        print("Precio:", datos['precio'])
        print("Categoría:", datos['categoria'])
    else:
        print("Producto no encontrado.")


def reporte_bajo_stock():
    limite = int(input("Ingrese el límite de stock para generar el reporte: "))
    print("Productos con stock igual o inferior a", limite, ":")
    for codigo, datos in inventario.items():
        if datos["cantidad"] <= limite:
            print("Código:", codigo)
            print("Nombre:", datos['nombre'])
            print("Cantidad:", datos['cantidad'])


def actualizar_producto():
    codigo = int(input("Ingrese el código del producto que desea actualizar: "))
    if codigo in inventario:
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        inventario[codigo]["cantidad"] = nueva_cantidad
        print("Producto", codigo, "actualizado con éxito.")
    else:
        print("Producto no encontrado.")


def eliminar_producto():
    codigo = int(input("Ingrese el código del producto que desea eliminar: "))
    if codigo in inventario:
        del inventario[codigo]
        print("Producto con código", codigo, "eliminado con éxito.")
    else:
        print("Producto no encontrado.")



while True:
    mostrar_menu()
    opcion =int(input("Seleccione una opción: "))
 
    if opcion ==1:
        registrar_producto()
    elif opcion ==2:
        mostrar_productos()
    elif opcion ==3:
        actualizar_producto()
    elif opcion ==4:
        eliminar_producto()
    elif opcion ==5:
        buscar_producto()
    elif opcion ==6:
        reporte_bajo_stock()
    elif opcion ==7:
        print("Saliendo delprograma...")
        break
    else:
        print("Opción inválida. Intente nuevamente.")


    