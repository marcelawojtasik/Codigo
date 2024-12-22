#Importo modulo para BBDD
import sqlite3

#Declaro constante
ruta_db = r"C:/Users/marce/Escritorio/Python/Codigo/inventario.db"

#Creacion/Conexion a BBDD - verificar ruta!
def db_crear_tabla_productos():
    conexion = sqlite3.connect(ruta_db) 
    puntero = conexion.cursor()
    query = """
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            categoria TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
        )
        """
    puntero.execute(query)
    conexion.commit()
    conexion.close()

#Agregar producto a BBDD - Argumento: diccionario producto
def db_registrar_producto(nombre, descripcion, categoria, cantidad, precio):
    try:
        conexion = sqlite3.connect(ruta_db) 
        puntero = conexion.cursor()
        query = """
        INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio)
        VALUES (?, ?, ?, ?, ?)
        """
        placeholder = (nombre, descripcion, categoria, cantidad, precio)
        puntero.execute(query, placeholder)
        conexion.commit()           
        state = True #flag para usar el return en finally
    except Exception as e:
        print(f"Error al registrar producto: {e}")
        state = False
    finally:        
        conexion.close() 
        return state

#Leer tabla de datos productos
def db_mostrar_productos():
    try:
        conexion = sqlite3.connect(ruta_db) 
        puntero = conexion.cursor()
        query = "SELECT * FROM productos"
        puntero.execute(query)
        lista_productos = puntero.fetchall()
    except Exception as e:
        print(f"Error al intentar traer registros de productos: {e}")
    finally:
        conexion.close() 
        return lista_productos
    
#Buscar producto por id    
def db_buscar_producto(id):
    try:
        conexion = sqlite3.connect(ruta_db) 
        puntero = conexion.cursor()
        query = "SELECT * FROM productos WHERE id = ?"
        placeholder = (id,)
        puntero.execute(query, placeholder)
        producto = puntero.fetchone() #tupla
    except Exception as e:
        print(f"Error al intentar traer registros de productos: {e}")
    finally:
        conexion.close() 
        return producto
    
#Actualizar cantidad de producto x id
def db_actualizar_cantidad_producto(id, nueva_cantidad):
    try:
        conexion = sqlite3.connect(ruta_db) 
        puntero = conexion.cursor()
        query = "UPDATE productos SET cantidad = ? WHERE id = ?"
        placeholder = (nueva_cantidad, id)
        puntero.execute(query, placeholder)
        conexion.commit()  
    except Exception as e:
        print(f"Error al intentar traer registros de productos: {e}")
    finally:
        conexion.close() 
        
#Eliminar producto por id
def db_eliminar_producto(id):
    try:
        conexion = sqlite3.connect(ruta_db) 
        puntero = conexion.cursor()
        query = "DELETE FROM productos WHERE id = ?"
        placeholder = (id)
        puntero.execute(query, placeholder)
        conexion.commit()  
    except Exception as e:
        print(f"Error al intentar traer registros de productos: {e}") 
    finally:
        conexion.close() 

#Generar reporte de stock con minimo pasado x parametro
def db_reporte_bajo_stock(min_stock):
    conexion = sqlite3.connect(ruta_db) 
    puntero = conexion.cursor()
    query = "SELECT * FROM productos WHERE cantidad < ?"
    placeholder = (min_stock,)
    puntero.execute(query, placeholder)    
    lista_productos = puntero.fetchall()
    conexion.close() 
    return lista_productos
