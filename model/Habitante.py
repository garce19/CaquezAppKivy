from model.Usuario import Usuario


class Habitante(Usuario):
    def __init__(self,id, nombre, apellido, celular, email, password, barrio, direccion):
        super().__init__(id, nombre, apellido, celular, email, password)
        self._barrio = barrio
        self._direccion = direccion

    @property
    def barrio(self):
        return self._barrio

    @property
    def direccion(self):
        return self._direccion

    @barrio.setter
    def barrio(self, barrio):
        self._barrio = barrio

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion
