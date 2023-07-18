from model.Usuario import Usuario


class Turista(Usuario):
    def __init__(self, id, nombre, apellido, celular, email, password, ciudad):
        super().__init__(id, nombre, apellido, email, password, celular)
        self._ciudad = ciudad

    @property
    def ciudad(self):
        return self._ciudad

    @ciudad.setter
    def ciudad(self, ciudad):
        self._ciudad = ciudad

