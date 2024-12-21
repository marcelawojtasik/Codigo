#Importo modulo para BBDD
import sqlite3

#Creacion/Conexion a BBDD - verificar ruta!
conexion = sqlite3.connect("C:/Users/marce/Escritorio/Python/Codigo/inventario.db") 

#Creacion puntero para interactuar con BBDD
cursor = conexion.cursor()

#Ejecucion consultas sql
cursor.execute("SELECT * from productos")

#Almacenamiento datos en variable temporal
datos = cursor.fetchall()
print(datos)

#Trabajo con los datos
if not datos:
    print("No hay datos para mostrar")
else:
    print(datos)
    #recorrer datos para ver como diccionario
    for registro in datos:
        for campo in registro:
            print(f"{campo}")


