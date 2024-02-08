import os
from miembros  import MiembrosManager
from libros    import LibrosManager
from eventos   import EventosManager
from prestamos import PrestamosManager
from menus     import mostrar_menu_principal, seleccionar_submenu

def main():
    miembros_manager  = MiembrosManager("data/miembros.txt")
    libros_manager    = LibrosManager("data/libros.txt")
    eventos_manager   = EventosManager("data/eventos.txt")
    prestamos_manager = PrestamosManager("data/prestamos.txt", miembros_manager, libros_manager)

    miembros          = miembros_manager.cargar_miembros()
    libros            = libros_manager.cargar_libros()
    eventos           = eventos_manager.cargar_eventos()
    prestamos         = prestamos_manager.cargar_prestamos()

    while True:
        os.system("cls")
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")
        seleccionar_submenu(opcion, miembros_manager, libros_manager)
        if opcion == "6":
            break

if __name__ == "__main__":
    main()
