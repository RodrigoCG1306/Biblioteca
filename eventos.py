import codecs
class Evento:
    def __init__(self, id_evento, nombre, fecha):
        self.id_evento = id_evento
        self.nombre = nombre
        self.fecha = fecha

    def __str__(self):
        return f"ID Evento: {self.id_evento}\nNombre: {self.nombre}\nFecha: {self.fecha}"

class EventosManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def cargar_eventos(self):
        eventos = []
        try:
            with codecs.open(self.file_path, "r", "utf-8") as file:
                for line in file:
                    id_evento, nombre, fecha = line.strip().split(",")
                    eventos.append(Evento(id_evento, nombre, fecha))
        except FileNotFoundError:
            eventos = []
        eventos.sort(key=lambda evento: int(evento.id_evento))
        return eventos

    def guardar_eventos(self, eventos):
        eventos.sort(key=lambda evento: int(evento.id_evento))
        with codecs.open(self.file_path, "w", "utf-8") as file:
            for evento in eventos:
                file.write(f"{evento.id_evento},{evento.nombre},{evento.fecha}\n")

    def agregar_evento(self, evento):
        eventos = self.cargar_eventos()
        eventos.append(evento)
        self.guardar_eventos(eventos)

    def eliminar_evento(self, id_evento):
        eventos = self.cargar_eventos()
        eventos = [e for e in eventos if e.id_evento != id_evento]
        self.guardar_eventos(eventos)
