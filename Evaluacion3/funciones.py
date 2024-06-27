GENERO= ['ficcion','no ficcion','ciencia']
def registrar_libro(libros): #1
    titulo = input("ingrese titulo del libro: ").lower()
    autor = input("ingrese autor del libro: ").lower()
    genero = input("ingrese género del libro (ficcion/no ficcion/ciencia): ").lower()
    precio = int(input("ingrese precio del libro: "))
    libros.append({
        'titulo':titulo,
        'autor':autor,
        'genero':genero,
        'precio':precio
    })

def listar_todos_los_libros(libros):#2
    print("LISTA DE LIBROS")
    for libro in libros:
        print(libro)

def registrar_venta(libros):#3
    titulo = input("ingrese titulo del libro: ").lower()
    cantidad = int(input("ingrese cantidad vendida (Cantidad máx. 10 por libro): "))
    precio = int(input("ingrese precio de unidad: "))
    precio_final = int(input("ingrese precio final: "))
    registro_libros = libros
    for libro in libros:
        if [libro['titulo']] not in libros:
            print("El titulo no existe en el inventario.")
        elif libro['titulo'] in libros:
            print("Libro disponible.")
            libros.append(libro)
        elif titulo in libros:
            libros.append(titulo)
        if cantidad >10:
            print("cantidad excede el stock disponible.")
        else:
            print("ingrese un libro disponible o regristelo primero.")
            return
        #CALCULOS
        precio_final = precio * cantidad
    libros.append({
        'titulo':titulo,
        'cantidad':cantidad,
        'precio':precio,
        'precio final':precio_final
    })
    print(f"\n***BOLETA***\nLIBRO: {titulo}\tCANTIDAD: {cantidad}\tPRECIO FINAL: {precio_final}\n****************************************")


def imprimir_reporte_venta(libros):#4
    genero_seleccionado = input("Ingrese el género que necesite imprimir o presione ENTER para imprimir todos: ").lower()
    if genero_seleccionado == "":
        imprimir_libros = libros
        nombre_archivo = f'planilla_todos.txt'
    elif genero_seleccionado in GENERO:
        imprimir_libros = []
        for libro in libros:
            if libro['genero'] in GENERO:
                imprimir_libros.append(libro)
        nombre_archivo = f'planilla_{genero_seleccionado}.txt'
    #GENERAR TXT
    with open(nombre_archivo, 'w') as archivo:
        for libro in imprimir_libros:
            archivo.write(f"Titulo: {libro['titulo']}\n")
            archivo.write(f"Autor: {libro['autor']}\n")
            archivo.write(f"Género: {libro['genero']}\n")
            archivo.write(f"Precio: {libro['precio']}\n\n")
