#nomina basica
name = ""
salaryForHours = 0.0 # 7.0
numberHoursWorker = 0   # 40
salaryForMonth = 0.0    # 470

name = input("Ingrese el nombre del trabajador: ")
salaryForHours = float(input("Ingrese el salario por hora del trabajador: "))
numberHoursWorker = int(input("Ingrese el número de horas trabajadas en el mes: "))
salaryForMonth = float(input("Ingrese el salario minimo del trabajador: "))

cal = salaryForHours * numberHoursWorker
if cal < salaryForMonth:
    print(f"Nombre: {name}.")
else:
    print(f"\tNombre: {name},\n Salario mensual: {cal}.")