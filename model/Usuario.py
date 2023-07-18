import bcrypt


class Usuario:
    def __init__(self, id, nombre, apellido, email, password, celular):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._password = self.hash_password(password)
        self._celular = celular

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

    @property
    def password(self):
        return self._password

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

    def hash_password(self, password):
        """
        Aplica un hash a la contraseña ingresada por el usuario para guardarla de manera segura
        :param password: Contraseña del usuario
        :return: Contraseña con hash aplicado
        """
        salt = bcrypt.gensalt()  # Generamos una salt aleatoria
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)  # Aplicamos hash a la contraseña
        return hashed.decode('utf-8')

    def verificar_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def __str__(self):
        return f'Nombre: {self.nombre} | Apellido: {self.apellido} | ID: {self.id}'
