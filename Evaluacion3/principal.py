#CREAR UN PROGRAMA DE REGISTRO Y VENTAS DE UNA LIBRERIA.
#CREAR MENU, PARA REGISTRAR LIBROS, LISTARLOS, REGISTRAR VENTAS, IMPRIMIR REPORTE, GENERAR UN TXT Y SALIR DEL PROGRAMA.
#EN REGISTRO DE VENTA VALIDAR QUE EL TITULO EXISTA Y QUE CANTIDAD DE LIBROS SOLCITADOS NO EXCEDAN EL STOCK DISPONIBLE.
#DEFINIR UNA COLECCION CON LOS GÉNEROS (FICCION/NO FICCION/CIENCIA)
#IMPRIMIR PLANILLA POR GENERO ESPECIFICO O TODOS.
#CARGAR ARCHIVO A GITHUB


import funciones as fn
libros = []
#MENU
while True:
    try:
            
        print("***BIENVENIDO AL SISTEMA DE LIBRERIA DUOCOGOTE***\n1. Registrar libro\n2. Listar todos los libros\n3. Registrar venta\n4. Imprimir reporte de ventas\n5. Generar archivo\n6. Salir")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            fn.registrar_libro(libros)
        elif opcion == 2:
            fn.listar_todos_los_libros(libros)
        elif opcion == 3:
            fn.registrar_venta(libros)
        elif opcion == 4:
            fn.imprimir_reporte_venta(libros)
        elif opcion == 5:
            print("ARCHIVO TXT")
            fn.imprimir_reporte_venta(libros)
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("opción no válida, intnte nuevamente.")



    except ValueError:
        print("opción inválida. Por favor, seleccione nuevamente.")