from model.Usuario import Usuario


class Turista(Usuario):
    def __init__(self):
        super().__init__()
        self._ciudad = None

    @property
    def ciudad(self):
        return self._ciudad

    @ciudad.setter
    def ciudad(self, ciudad):
        self._ciudad = ciudad

