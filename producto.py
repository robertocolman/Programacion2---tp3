class Producto:

    def __init__(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return "Producto(Nombre: {})".format(self.__nombre)

    def __eq__(self, otro):
        if isinstance(otro, Producto):
            return self.__nombre == otro.__nombre
        return False

    def obtenerNombre(self):
        return self.__nombre