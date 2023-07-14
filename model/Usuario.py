class Usuario:
    def __init__(self):
        self._id = None
        self._nombre = None
        self._apellido = None
        self._email = None
        self._celular = None

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def id(self):
        return self._id

    @property
    def email(self):
        return self._email

    @property
    def celular(self):
        return self._celular


    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @id.setter
    def id(self, id):
        self._id = id

    @email.setter
    def email(self, email):
        self._email = email

    @celular.setter
    def celular(self, celular):
        self._celular = celular

    def __str__(self):
        return f'Nombre: {self.nombre} | Apellido: {self.apellido} | ID: {self.id}'

