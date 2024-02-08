import codecs
class Libro:
    def __init__(self, id, nombre, autor, genero):
        self.id = id
        self.nombre = nombre
        self.autor = autor
        self.genero = genero

    def __str__(self):
        return f"{self.id},{self.nombre},{self.autor},{self.genero}"

class LibrosManager:
    def __init__(self, archivo):
        self.archivo = archivo

    def obtener_libro_por_id(self, id_libro):
        libros = self.cargar_libros()
        for libro in libros:
            if libro.id == id_libro:
                return libro
        return None

    def cargar_libros(self):
        libros = []
        with codecs.open(self.archivo, "r", "utf-8") as file:
            for line in file:
                id, nombre, autor, genero = line.strip().split(",")
                libro = Libro(id, nombre, autor, genero)
                libros.append(libro)
        libros.sort(key=lambda libro: int(libro.id))  # Ordenar por ID
        return libros

    def guardar_libros(self, libros):
        libros.sort(key=lambda libro: int(libro.id))  # Ordenar por ID
        with codecs.open(self.archivo, "w", "utf-8") as file:
            for libro in libros:
                file.write(str(libro) + "\n")

    def agregar_libro(self, libro):
        libros = self.cargar_libros()
        libros.append(libro)
        self.guardar_libros(libros)

    def eliminar_libro(self, id):
        libros = self.cargar_libros()
        libros = [libro for libro in libros if libro.id != id]
        self.guardar_libros(libros)
