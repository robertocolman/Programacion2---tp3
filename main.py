from empresa import Empresa
from empleado import Empleado
from producto import Producto

# --- 1. CREACIÓN DE OBJETOS ---

# Crear 2 Productos (serán usados en ambas empresas)
p1 = Producto("Monitor 4K")
p2 = Producto("Teclado Mecánico")
p3 = Producto("Mouse Vertical")

# Crear 6 Empleados
e_juan = Empleado("Juan", "Pérez")
e_maria = Empleado("María", "Gómez")
e_carlos = Empleado("Carlos", "López")
e_ana = Empleado("Ana", "Martínez")
e_pedro = Empleado("Pedro", "Rodríguez")
e_laura = Empleado("Laura", "Sánchez")


# --- 2. CREACIÓN DE EMPRESAS ---

# 1. Empresa A: "TecnoSolutions S.A."
empresa_a = Empresa("TecnoSolutions S.A.")

# Agregar Productos
empresa_a.agregarProducto(p1)
empresa_a.agregarProducto(p2)

# Agregar Empleados (se les asignará legajo automáticamente, iniciando en 1)
empresa_a.altaEmpleado(e_juan)   # Legajo 1
empresa_a.altaEmpleado(e_maria)  # Legajo 2
empresa_a.altaEmpleado(e_carlos) # Legajo 3

# 2. Empresa B: "SoftDevelop SRL"
empresa_b = Empresa("SoftDevelop SRL")

# Agregar Productos
empresa_b.agregarProducto(p2)
empresa_b.agregarProducto(p3)

# Agregar Empleados (se les asignará legajo automáticamente, iniciando en 1)
empresa_b.altaEmpleado(e_ana)    # Legajo 1
empresa_b.altaEmpleado(e_pedro)  # Legajo 2
empresa_b.altaEmpleado(e_laura)  # Legajo 3


# --- 3. REMOVER 2 EMPLEADOS DE UNA DE ELLAS (Empresa A) ---

print("--- Ejecutando Bajas en TecnoSolutions S.A. ---")
empresa_a.bajaEmpleado(e_juan)
print(f"-> Empleado {e_juan.obtenerNombres()} dado de baja.") # Juan (Legajo 1)
empresa_a.bajaEmpleado(e_maria)
print(f"-> Empleado {e_maria.obtenerNombres()} dado de baja.") # María (Legajo 2)

# Carlos (Legajo 3) se mantiene en estado de ALTA.
print("\n")


# --- 4. IMPRIMIR INFORMACIÓN DE CADA EMPRESA (Usando __str__) ---

print("================================================")
print("             REPORTE FINAL DE EMPRESAS            ")
print("================================================")

# Se utiliza automáticamente el método __str__() al usar print() sobre el objeto
print(empresa_a)

print("\n------------------------------------------------")

print(empresa_b)

print("================================================")