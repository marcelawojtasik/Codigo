from funciones_ddbb import *

#Función para mostrar menu principal y capturar opcion ingresada por el usuario
def mostrar_menu():
    print("Menú de Gestión de Inventario:")
    print("-" * 30)
    print(
        """
        1. Registrar producto
        2. Mostrar productos
        3. Actualizar cantidad de un producto
        4. Eliminar producto
        5. Buscar producto por id
        6. Reporte de Bajo Stock
        7. Salir
        """
    )    
    opcion0 = input("Ingrese la opción deseada: ")
    return opcion0


#Función para agregar producto
def registrar_producto():
    print("\nPor favor, ingrese los datos del producto")
    #Ingreso y validacion del nombre
    while True:
        try: 
            nombre = input("Ingrese el nombre del producto: ").strip()
            if not nombre:
                raise ValueError("Error: Este campo no puede estar vacío.")
            break
        except ValueError:
            print("El campo no puede estar vacio")

    descripcion = input("Ingrese una breve descripción: ")
    #Ingreso y validacion de la categoria
    while True:
        try: 
            categoria = input("Ingrese la categoría del producto: ").strip()
            if not categoria:
                raise ValueError("Error: Este campo no puede estar vacío.")
            break
        except ValueError:
            print("El campo no puede estar vacio")    
    #Ingreso y validacion de la cantidad
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad disponible: "))
            break
        except ValueError:
            print("Error: Debe ingresar un número entero")
        #except Exception as e - si quiero info de error tecnico
    #Ingreso y validacion del precio
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            break
        except ValueError:
            print("Error: Debe ingresar un número")    

    """ #Diccionario temporal en memoria
        producto = {
        "nombre" : nombre,
        "descripcion" : descripcion,
        "categoria" : categoria,
        "cantidad" : cantidad,
        "precio" : precio,
    }
    print("\n", producto) """
    #Persisto producto
    resultado = db_registrar_producto(nombre, descripcion, categoria, cantidad, precio)
    if resultado == True:
        print("Producto agregado")
    else:
        print("No se agregó el producto debido a un error")


#Funcion para mostrar productos    
def mostrar_productos():
    lista_productos = db_mostrar_productos()
    if not lista_productos:
        print("No hay registros en la tabla")
    else:
        print("\n****Lista de Productos****")
        for producto in lista_productos:
            print(f"id: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Categoría: {producto[3]}, Cantidad: {producto[4]}, Precio: {producto[5]}")


#Funcion para buscar un producto por id
def buscar_producto():
    id = int(input("Ingrese id del producto a buscar: "))
    producto = db_buscar_producto(id)
    if not producto:
        print(f"No existe el producto con id {id}")
    else:
        print(producto)
    

#Funcion para generar un reporte de productos con stock menor al señalado
def reporte_bajo_stock():
    min_stock = int(input("Ingrese el valor para definir stock mínimo para generar el reporte: "))
    lista_productos = db_reporte_bajo_stock(min_stock)
    if lista_productos:
        for producto in lista_productos:
            print(producto)
    else:
        print(f"No hay productos con stock menor a {min_stock} unidades")


#Funcion para actualizar un registro
def actualizar_cantidad_producto():
    id = int(input("Ingrese id del producto a actualizar: "))
    producto = db_buscar_producto(id)
    if producto:
        print(producto)
        nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
        db_actualizar_cantidad_producto(id, nueva_cantidad)
        print("Cantidad del producto actualizada")
    else:
        print("No existe el producto con el id ingresado")


#Funcion para eliminar un registro
def eliminar_producto():
    id = int(input("Ingrese id del producto a eliminar: "))
    producto = db_buscar_producto(id)
    if producto:
        print(f"Está seguro de querer eliminar {producto}?")
        continuar = input("Ingrese 's' para continuar o cualquier tecla para salir : ").lower()  
        if continuar == "s":
            db_eliminar_producto(id)
            print(f"El producto con id {id} ha sido eliminado")
        else:
            print("Operacion cancelada")
    else:
        print("No existe el producto con el id ingresado")


