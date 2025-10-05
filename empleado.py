class Empleado:
    
    ESTADO_ALTA = 1
    ESTADO_BAJA = 2

    def __init__(self, nombres, apellidos):
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__estado = Empleado.ESTADO_ALTA
        self.__numeroLegajo = None

    def __str__(self):
        estado_texto = "ALTA" if self.__estado == Empleado.ESTADO_ALTA else "BAJA"
        legajo = self.__numeroLegajo if self.__numeroLegajo is not None else "SIN ASIGNAR"
        
        return "Empleado(Legajo: {}, Nombre: {} {}, Estado: {})".format(
            legajo, self.__nombres, self.__apellidos, estado_texto
        )
        
    def __eq__(self, otro):
        if isinstance(otro, Empleado) and self.__numeroLegajo is not None:
            return self.__numeroLegajo == otro.__numeroLegajo
        return False

    def establecerNumeroLegajo(self, numero):
        self.__numeroLegajo = numero

    def establecerNombres(self, nombres):
        self.__nombres = nombres

    def establecerApellidos(self, apellidos):
        self.__apellidos = apellidos

    def establecerEstado(self, estado):
        self.__estado = estado

    def obtenerNumeroLegajo(self):
        return self.__numeroLegajo

    def obtenerNombres(self):
        return self.__nombres

    def obtenerApellidos(self):
        return self.__apellidos

    def obtenerEstado(self):
        return self.__estado