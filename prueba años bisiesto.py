# NOMINA SENCILLA
nombre = input("Ingrese el nombre del empleado: ")
salario_hora = float(input("Ingrese el salario básico por hora: "))
horas_mes = float(input("Ingrese el número de horas trabajadas en el mes: "))

salario_mensual = salario_hora * horas_mes

salario_minimo = 470

if salario_mensual > salario_minimo:
    print("Empleado:", nombre)
    print("Salario mensual:", salario_mensual)
else:
    print("Empleado:", nombre)
