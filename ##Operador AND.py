#dado tres numeros, verificar si el primero es mayor que el segundo y el segundo es mayor que el tercero
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

# Determinar el mayor
if a > b and a > c:
    mayor = a
elif b > a and b > c:
    mayor = b
else:
    mayor = c

# Imprimir el mayor
print("El número mayor es:", mayor)
