from producto import Producto
from empleado import Empleado

class Empresa:

    def __init__(self, razonSocial):
        self.razonSocial = razonSocial
        self.productos = []
        self.empleados = []

        self.contadorLegajos = 0 
    
    def obtenerSiguienteLegajo(self):
        self.contadorLegajos += 1
        return self.contadorLegajos
    
    def establecerRazonSocial(self, razonSocial):
        self.razonSocial = razonSocial

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def removerProducto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            
    def altaEmpleado(self, empleado):
        nuevo_legajo = self.obtenerSiguienteLegajo()
        empleado.establecerNumeroLegajo(nuevo_legajo)
        empleado.establecerEstado(Empleado.ESTADO_ALTA)
        self.empleados.append(empleado)

    def bajaEmpleado(self, empleado):
        if empleado in self.empleados:
            empleado.establecerEstado(Empleado.ESTADO_BAJA)

    def obtenerRazonSocial(self):
        return self.razonSocial

    def obtenerProductos(self):
        return self.productos

    def obtenerEmpleadosDeAlta(self):
        empleados_alta = []
        for empleado in self.empleados:
            if empleado.obtenerEstado() == Empleado.ESTADO_ALTA:
                empleados_alta.append(empleado)
        return empleados_alta

    def obtenerEmpleadosHistorico(self):
        return self.empleados
    
    def obtenerEmpleadosDeAlta(self):
        empleados_alta = []
        for empleado in self.empleados:
            if empleado.obtenerEstado() == Empleado.ESTADO_ALTA:
                empleados_alta.append(empleado)
        return empleados_alta

    def obtenerEmpleadosHistorico(self):
        return self.empleados
    
