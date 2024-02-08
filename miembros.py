import codecs
class Miembro:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"{self.id},{self.nombre},{self.email}"

class MiembrosManager:
    def __init__(self, archivo):
        self.archivo = archivo
        
    def obtener_miembro_por_id(self, id_miembro):
        miembros = self.cargar_miembros()
        for miembro in miembros:
            if miembro.id == id_miembro:
                return miembro
        return None

    def cargar_miembros(self):
        miembros = []
        with codecs.open(self.archivo, "r", "utf-8") as file:
            for line in file:
                id, nombre, email = line.strip().split(",")
                miembro = Miembro(id, nombre, email)
                miembros.append(miembro)
        miembros.sort(key=lambda miembro: int(miembro.id))
        return miembros

    def guardar_miembros(self, miembros):
        miembros.sort(key=lambda miembro: int(miembro.id))
        with codecs.open(self.archivo, "w", "utf-8") as file:
            for miembro in miembros:
                file.write(str(miembro) + '\n')

    def agregar_miembro(self, miembro):
        miembros = self.cargar_miembros()
        miembros.append(miembro)
        self.guardar_miembros(miembros)

    def eliminar_miembro(self, id):
        miembros = self.cargar_miembros()
        miembros = [miembro for miembro in miembros if miembro.id != id]
        self.guardar_miembros(miembros)
        