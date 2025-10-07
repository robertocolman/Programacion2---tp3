from empresa import Empresa
from empleado import Empleado
from producto import Producto

p1 = Producto("Procesador Intel Celeron G4900 3.10GHz")
p2 = Producto("Mother Asrock Z390 Phantom Gaming 4S Wi-Fi")
p3 = Producto("Memoria Team DDR4 8GB 3200Mhz")
p4 = Producto("Placa de Video MSI GeForce RTX 3050 6GB GDDR6")
p5 = Producto("Gabinete Antec AX20 ELITE RGB Black Mesh 4x120mm")
p6 = Producto("Monitor Dahua DHI-LM22-A201Y")

empresa_a = Empresa("compumundo hiper mega red S.A.")
empresa_b = Empresa("SoftTech SRL")

e_roberto = Empleado("Colman", "Roberto")
e_nahuel = Empleado("Nahuel", "Valenzuela")
e_esteban = Empleado("Esteban", "Chavez")
e_pedro = Empleado("Pedro", "Gose")
e_luis = Empleado("Luis", "Cabral")
e_josefina = Empleado("Josefina", "Cardozo")

empresa_a.agregarProducto(p1)
empresa_a.agregarProducto(p2)

empresa_a.altaEmpleado(e_nahuel)
empresa_a.altaEmpleado(e_luis)
empresa_a.altaEmpleado(e_josefina)

empresa_b.agregarProducto(p2)
empresa_b.agregarProducto(p3)

empresa_b.altaEmpleado(e_esteban)
empresa_b.altaEmpleado(e_pedro)
empresa_b.altaEmpleado(e_roberto)


print("--- Ejecutando Bajas en compumundo hiper mega red S.A. ---")
empresa_a.bajaEmpleado(e_nahuel)
print(f"-> Empleado {e_nahuel.obtenerNombres()} dado de baja.")
empresa_a.bajaEmpleado(e_pedro)
print(f"-> Empleado {e_pedro.obtenerNombres()} dado de baja.")

print("\n")

print("# # # # # # # # # # # # # # # # # # # # # # # # # # # #")
print("  ♦ ♦ ♦ INFORME DETALLADO DE ESTADO DE EMPRESAS ♦ ♦ ♦  ")
print("# # # # # # # # # # # # # # # # # # # # # # # # # # # #")

print(empresa_a)

print("\n# # # # # # # # # # # # # # # # # # # # # # # # # # # #")
print(empresa_b)
print("# # # # # # # # # # # # # # # # # # # # # # # # # # # #")