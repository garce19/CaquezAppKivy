class Espacio:
    def __init__(self, nombre, direccion, es_24_horas, barrio, calificacion, descripcion):
        self._nombre = nombre
        self._direccion = direccion
        self._es_24_Horas = es_24_horas
        self._barrio = barrio
        self._calificacion = calificacion
        self._descripcion = descripcion

    @property
    def nombre(self):
        return self._nombre

    @property
    def direccion(self):
        return self._direccion

    @property
    def es_24_horas(self):
        return self._es_24_Horas

    @property
    def barrio(self):
        return self._barrio

    @property
    def calificacion(self):
        return self._calificacion

    @property
    def descripcion(self):
        return self._descripcion
