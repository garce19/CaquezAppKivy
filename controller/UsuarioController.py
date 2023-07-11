from model.Usuario import Usuario
import psycopg2


class UsuarioController:
    def __init__(self):
        self.model = Usuario()

    def crear_usuario(self, id: str, nombre: str, apellido: str, email: str, celular: str, barrio: str, direccion: str):
        """
        Crea un nuevo usuario con base al modelo
        :param id: Cédula o tarjeta de identidad del usuario
        :param nombre: Nombre del usuario
        :param apellido: Apellido del usuario
        :param email: Email del usuario
        :param celular: Celular del usuario
        :param barrio: Barrio del usuario
        :param direccion: Dirección del usuario
        :return:
        """
        self.model.id = id
        self.model.nombre = nombre
        self.model.apellido = apellido
        self.model.email = email
        self.model.celular = celular
        self.model.barrio = barrio
        self.model.direccion = direccion
