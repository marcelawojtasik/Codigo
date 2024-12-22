#Importo modulo para BBDD
import sqlite3

#Creacion/Conexion a BBDD - verificar ruta!
conexion = sqlite3.connect("C:/Users/marce/Escritorio/Python/Codigo/inventario.db") 

#Creacion puntero para interactuar con BBDD
cursor = conexion.cursor()

#Ejecucion queries sql
cursor.execute("SELECT * FROM productos")

#Almacenamiento datos en variable temporal
datos = cursor.fetchall() #devuelve lista de tuplas (1 tupla:1 registro)
#datos = cursor.fetchone()  #devuelve tupla


#Trabajo con los datos
if not datos:
    print("No hay datos para mostrar")
else:
    print(datos)
    for registro in datos:
        for campo in registro:
            print(f"{campo}")



"""
#Convertir tupla a diccionario
conexion.row_factory = sqlite3.Row #Obtener filas como objetos tipo Row
for registro_object in datos:
    registro = dict(registro_object)
    print(registro_object)
    for key, value in registro.items():
        print(f"{key} : {value}")


# Iterar sobre los registros
for registro_ in datos:
    print(type(registro_))  # Verifica el tipo de cada registro
    print(registro_)        # Inspecciona el contenido del registro

    # Convertir Row a diccionario si es posible
    try:
        registro = dict(registro_)
        for key, value in registro.items():
            print(f"{key} : {value}")
    except ValueError as e:
        print(f"Error al convertir el registro: {e}")
"""
#Persistir cambios
conexion.commit()

#Cerrar conexion al finalizar
conexion.close()