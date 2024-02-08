import os
import codecs
from art import *
from libros import Libro, LibrosManager
from miembros import Miembro, MiembrosManager
from eventos import Evento, EventosManager
from prestamos import Prestamo, PrestamosManager

#Menú principal
def mostrar_menu_principal():
    os.system("cls")
    print("Bienvenido a la Biblioteca")
    print("1. Libros")
    print("2. Miembros")
    print("3. Eventos")
    print("4. Prestamos")
    print("5. Buscar")
    print("6. Salir")

#Mostrar el menú de la elección del usuario
def seleccionar_submenu(opcion, miembros_manager, libros_manager):
    while True:
        if opcion == "1":
            mostrar_menu_libros()
        elif opcion == "2":
            mostrar_menu_miembros()
        elif opcion == "3":
            mostrar_menu_eventos()
        elif opcion == "4":
            mostrar_menu_prestamos(miembros_manager, libros_manager)
        elif opcion =="5":
            mostrar_menu_busqueda()
        elif opcion == "6":
            os.system("cls")
            print("Gracias por usar esta biblioteca :D")

            tprint("GRACIAS", "rand-xlarge")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
        opcion = input("Seleccione una opción: ")

#Menú de búsqueda
def mostrar_menu_busqueda():
    os.system("cls")
    print("Menú de Búsqueda")
    print("Ingrese su término de búsqueda:")
    termino = input("> ")

    resultados = buscar_en_archivos(termino)

    os.system("cls")

    if resultados:
        print("Resultados de la búsqueda:")
        for resultado in resultados:
            print(resultado)
    else:
        print("No se encontraron resultados para el término de búsqueda.")

    input("Presione Enter para continuar...")
    mostrar_menu_principal()

# Función para buscar en archivos de texto sin distinguir mayúsculas y minúsculas
# Función para buscar en archivos de texto sin distinguir mayúsculas y minúsculas
def buscar_en_archivos(termino):
    resultados = []
    # Lista de archivos de texto en el directorio 'data'
    archivos = [f for f in os.listdir("data") if f.endswith(".txt")]

    # Convertir el término de búsqueda a minúsculas para hacer una búsqueda insensible a mayúsculas
    termino = termino.lower()

    for archivo in archivos:
        with codecs.open(os.path.join("data", archivo), "r", "utf-8") as file:
            for linea in file:
                if termino in linea.lower():
                    resultados.append(f"Resultado encontrado en {archivo}:\n{linea.strip()}")

    return resultados

#Menú de libros
def mostrar_menu_libros():
    os.system("cls")
    print("Menú de Libros")
    print("1. Mostrar Libros")
    print("2. Añadir Libros")
    print("3. Eliminar Libros")
    print("4. Volver al menú principal")
    seleccionar_submenu_libros()

#Acciones del menú "Libros"
def seleccionar_submenu_libros():
    libros_manager = LibrosManager("data/libros.txt")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        os.system("cls")  # Limpia la pantalla
        libros = libros_manager.cargar_libros()
        print("\nLista de Libros:")
        for libro in libros:
            print(f"ID: {libro.id}\nNombre: {libro.nombre}\nAutor: {libro.autor}\nGénero: {libro.genero}\n")
        input("Presione enter para continuar...")
        mostrar_menu_libros()

    elif opcion == "2":
        os.system("cls")
        id = input("Ingrese el ID del libro: ")
        nombre = input("Ingrese el nombre del libro: ")
        autor = input("Ingrese el autor del libro: ")
        genero = input("Ingrese el género del libro: ")
        nuevo_libro = Libro(id, nombre, autor, genero)
        libros_manager.agregar_libro(nuevo_libro)
        print("Libro agregado con éxito.")
        input("Presione enter para continuar...")
        mostrar_menu_libros()

    elif opcion == "3":
        os.system("cls")
        id = input("Ingrese el ID del libro a eliminar: ")
        libros_manager.eliminar_libro(id)
        print("Libro eliminado con éxito.")
        input("Presione enter para continuar...")
        mostrar_menu_libros()

    elif opcion == "4":
        mostrar_menu_principal()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        input("Presione enter para continuar...")

#Menú de miembros
def mostrar_menu_miembros():
    os.system("cls")
    print("Menú de Miembros")
    print("1. Mostrar Miembros")
    print("2. Añadir Miembros")
    print("3. Eliminar Miembros")
    print("4. Volver al menú principal")
    seleccionar_submenu_miembros()

#Acciones del menú "Miembros"
def seleccionar_submenu_miembros():
    miembro_manager = MiembrosManager("data/miembros.txt")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        os.system("cls")
        miembros = miembro_manager.cargar_miembros()
        print("\nLista de Miembros:")
        for miembro in miembros:
            print(f"ID: {miembro.id}\nNombre: {miembro.nombre}\nEmail: {miembro.email}\n")
        input("Presione enter para continuar...")
        mostrar_menu_miembros()
    
    elif opcion == "2":
        os.system("cls")
        id = input("Ingrese el ID del usuario: ")
        nombre = input("Ingrese el nombre del usuario: ")
        email = input("Ingrese el email del usuario: ")
        nuevo_miembro = Miembro(id, nombre, email)
        miembro_manager.agregar_miembro(nuevo_miembro)
        print("Miembro agregado con éxito")
        input("Presione enter para continuar...")
        mostrar_menu_miembros()

    elif opcion == "3":
        os.system("cls")
        id = input("Ingrese el ID del miembro a eliminar: ")
        miembro_manager.eliminar_miembro(id)
        print("Miembro eliminado con éxito.")
        input("Presione enter para continuar...")
        mostrar_menu_miembros()
    
    elif opcion == "4":
        mostrar_menu_principal()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        input("Presione enter para continuar...")

#Menú de eventos
def mostrar_menu_eventos():
    while True:
        os.system("cls")
        print("Menú de Eventos")
        print("1. Agendar evento")
        print("2. Mostrar eventos")
        print("3. Eliminar evento")
        print("4. Volver al menú principal")
        seleccionar_submenu_eventos()

#Acciones del sub menú "Eventos"
def seleccionar_submenu_eventos():
    eventos_manager = EventosManager("data/eventos.txt")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        os.system("cls")
        id_evento = input("Ingrese el ID del evento: ")
        nombre = input("Ingrese el nombre del evento: ")
        fecha = input("Ingrese la fecha del evento (DD/MM/AAAA): ")
        nuevo_evento = Evento(id_evento, nombre, fecha)
        eventos_manager.agregar_evento(nuevo_evento)
        print("Evento agendado con éxito.")
        input("Presione Enter para continuar.")

    elif opcion == "2":
        os.system("cls")
        eventos = eventos_manager.cargar_eventos()
        if not eventos:
            print("No hay eventos agendados.")
        else:
            for evento in eventos:
                print(evento)
        input("Presione Enter para continuar.")

    elif opcion == "3":
        os.system("cls")
        id_evento = input("Ingrese el ID del evento a eliminar: ")
        eventos_manager.eliminar_evento(id_evento)
        print("Evento eliminado con éxito.")
        input("Presione Enter para continuar.")

    elif opcion == "4":
        mostrar_menu_principal()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        input("Presione enter para continuar...")

#Menú de prestamos
def mostrar_menu_prestamos(miembros_manager, libros_manager):
    os.system("cls")
    print("Menú de Préstamos")
    print("1. Solicitar préstamo")
    print("2. Lista de préstamos")
    print("3. Eliminar préstamo")
    print("4. Volver al menú principal")
    seleccionar_submenu_prestamos(miembros_manager, libros_manager)

#Acciones del sub menú "Prestamos"
def seleccionar_submenu_prestamos(miembros_manager, libros_manager):
    prestamos_manager = PrestamosManager("data/prestamos.txt", miembros_manager, libros_manager)
    miembros_manager = MiembrosManager("data/miembros.txt")
    libros_manager = LibrosManager("data/libros.txt")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        os.system("cls")
        miembros = miembros_manager.cargar_miembros()
        libros = libros_manager.cargar_libros()

        id_prestamo = input("Ingrese el ID del préstamo: ")

        print("Miembros disponibles:")
        for miembro in miembros:
            print(f"ID: {miembro.id}\nNombre: {miembro.nombre}\nCorreo: {miembro.email}\n")

        miembro_id = input("Ingrese el ID del miembro: ")

        os.system("cls")
        print("\nLibros disponibles:")
        for libro in libros:
            print(f"ID: {libro.id}\nNombre: {libro.nombre}\nAutor: {libro.autor}\nGénero: {libro.genero}\n")

        libro_id = input("Ingrese el ID del libro: ")
        os.system("cls")
        fecha_prestamo = input("Ingrese la fecha de préstamo (DD/MM/AAAA): ")
        fecha_devolucion = input("Ingrese la fecha de devolución (DD/MM/AAAA): ")

        nuevo_prestamo = Prestamo(id_prestamo, miembro_id, libro_id, fecha_prestamo, fecha_devolucion)
        prestamos_manager.agregar_prestamo(nuevo_prestamo)
        print("Préstamo registrado con éxito.")
        input("Presione enter para continuar...")
        mostrar_menu_prestamos(miembros_manager, libros_manager)


    elif opcion == "2":
        os.system("cls")
        prestamos = prestamos_manager.cargar_prestamos()
        miembros = miembros_manager.cargar_miembros()
        libros = libros_manager.cargar_libros()

        print("\nLista de Préstamos:")
        for prestamo in prestamos:
            miembro_nombre = next((miembro.nombre for miembro in miembros if miembro.id == prestamo.id_miembro), "Desconocido")
            libro_nombre = next((libro.nombre for libro in libros if libro.id == prestamo.id_libro), "Desconocido")

            
            print(f"ID Préstamo: {prestamo.id_prestamo}")
            print(f"Miembro: {miembro_nombre}")
            print(f"Libro: {libro_nombre}")
            print(f"Fecha de Préstamo: {prestamo.fecha_prestamo}")
            print(f"Fecha de Devolución: {prestamo.fecha_devolucion}\n")
            
        input("Presione enter para continuar...")
        mostrar_menu_prestamos(miembros_manager, libros_manager)

    elif opcion == "3":
        os.system("cls")
        id_prestamo = input("Ingrese el ID del préstamo a eliminar: ")
        prestamos_manager.eliminar_prestamo(id_prestamo)
        print("Préstamo eliminado con éxito.")
        input("Presione enter para continuar...")
        mostrar_menu_prestamos(miembros_manager, libros_manager)

    elif opcion == "4":
        mostrar_menu_principal()

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        input("Presione enter para continuar...")
