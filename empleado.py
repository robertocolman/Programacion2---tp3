class Empleado:
    ESTADO_ALTA = 1
    ESTADO_BAJA = 2

    def __init__(self, nombres, apellidos):
        self.nombres = nombres
        self.apellidos = apellidos

        self.estado = Empleado.ESTADO_ALTA
        self.numeroLegajo = None

    def establecerNumeroLegajo(self, numero):
        self.numeroLegajo = numero

    def establecerNombres(self, nombres):
        self.nombres = nombres

    def establecerApellidos(self, apellidos):
        self.apellidos = apellidos

    def establecerEstado(self, estado):
        self.estado = estado

    def obtenerNumeroLegajo(self):
        return self.numeroLegajo

    def obtenerNombres(self):
        return self.nombres

    def obtenerApellidos(self):
        return self.apellidos

    def obtenerEstado(self):
        return self.estado
