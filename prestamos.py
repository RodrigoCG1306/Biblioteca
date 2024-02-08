import codecs

class Prestamo:
    def __init__(self, id_prestamo, id_miembro, id_libro, fecha_prestamo, fecha_devolucion):
        self.id_prestamo = id_prestamo
        self.id_miembro = id_miembro
        self.id_libro = id_libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

class PrestamosManager:
    def __init__(self, file_path, miembros_manager, libros_manager):
        self.file_path = file_path
        self.prestamos = self.cargar_prestamos()
        self.miembros_manager = miembros_manager
        self.libros_manager = libros_manager

    def cargar_prestamos(self):
        prestamos = []
        with codecs.open(self.file_path, "r", "utf-8") as file:
            for line in file:
                prestamo_data = line.strip().split(",")
                if len(prestamo_data) == 5:
                    id_prestamo, id_miembro, id_libro, fecha_prestamo, fecha_devolucion = prestamo_data
                    prestamo = Prestamo(id_prestamo, id_miembro, id_libro, fecha_prestamo, fecha_devolucion)
                    prestamos.append(prestamo)
        return prestamos

    def guardar_prestamos(self, prestamos):
        prestamos_ordenados = sorted(prestamos, key=lambda x: x.id_prestamo)
        with codecs.open(self.file_path, "w", "utf-8") as file:
            for prestamo in prestamos_ordenados:
                file.write(f"{prestamo.id_prestamo},{prestamo.id_miembro},{prestamo.id_libro},{prestamo.fecha_prestamo},{prestamo.fecha_devolucion}\n")

    def agregar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)
        self.guardar_prestamos(self.prestamos)

    def eliminar_prestamo(self, id_prestamo):
        prestamos = self.cargar_prestamos()
        prestamos = [prestamo for prestamo in prestamos if prestamo.id_prestamo != id_prestamo]
        self.guardar_prestamos(prestamos)