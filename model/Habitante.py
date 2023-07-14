from model.Usuario import Usuario


class Habitante(Usuario):
    def __init__(self):
        super().__init__()
        self._barrio = None
        self._direccion = None

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
