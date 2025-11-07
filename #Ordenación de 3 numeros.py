#Ordenación de 3 numeros
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

numeros = [num1, num2, num3]
numeros.sort()

print(f"El número menor es: {numeros[0]}")
print(f"El número del medio es: {numeros[1]}")
print(f"El número mayor es: {numeros[2]}")