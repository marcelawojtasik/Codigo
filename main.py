
#Importo modulos
from funciones_menu import *
from funciones_ddbb import (
    db_crear_tabla_productos
)

#Declaro funcion ppal "main"
def main():
    #Inicializo BBDD y tabla de productos
    db_crear_tabla_productos()

    
    #Cuerpo funcion main
    while True:
        opcion = mostrar_menu()
        #print(f"Ud. seleccionó: {opcion}")    

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_cantidad_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")        
        continuar = input("Ingrese 's' para salir o cualquier tecla para continuar: ").lower()  
        if continuar == "s":
            print("\n*/*/*/*/*Gracias por usar nuestra App*\*\*\*\*")
            break  
   
main()