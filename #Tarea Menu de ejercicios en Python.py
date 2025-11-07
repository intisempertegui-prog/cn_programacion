#Tarea Menu de ejercicios en Python
opcion = 0
menu = """Bienvenido al sistema de ejercicios en Python.
Elija una de la siguientes opciones
1. Numero Par
2. NÚMERO MAYOR
3. ORDENACIÓN DE TRES NÚMEROS
4. NUMERO ES MÚLTIPLO DE OTRO
5. Salir
"""

while(opcion != 5):
    opcion = int(input(menu))
    
    if opcion == 1:
        numero = int(input("Ingrese un numero entero: "))
        if numero % 2 == 0:
            print(f"El numero {numero} es par.")
        else:
            print(f"El numero {numero} es impar.")
        opcion = int(input("Desea realizar otra operación? (1=si): "))
    elif opcion == 2:
        #Solicitamos los números con los cuales vamos a trabajar
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        numero3 = float(input("Ingrese el tercer numero: "))

        #Evaluamos si todos son iguales. Mostramos que son iguales en caso positivo
        if numero1 == numero2 and numero1 == numero3: 
            print("Los números ingresados son iguales")
        else:
            #Evaluamos si numero1 es mayor a los otros 2. Lo mostramos en caso positivo
            if numero1 >= numero2 and numero1 >= numero3: 
                print(f"El numero mayor es {numero1}")

            #Evaluamos si numero2 es mayor a los otros 2. Lo mostramos en caso positivo
            elif numero2 >= numero3 and numero2 >= numero1: 
                print(f"El número mayor es {numero2}")

            #Caso contrario el numero 3 es el mayor y lo mostramos
            else:                                            
                print(f"El número mayor es {numero3}")
    elif opcion == 3:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        numero3 = float(input("Ingrese el tercer número: "))
        
        numeros = [numero1, numero2, numero3]
        numeros.sort()

        print(f"El número menor es: {numeros[0]}")
        print(f"El número del medio es: {numeros[1]}")
        print(f"El número mayor es: {numeros[2]}")
            
        opcion = int(input("Desea realizar otra operación? (1=si): "))
    elif opcion == 4:
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))

        if numero1 == 0 :
            print ("error")
        elif numero1 % numero2 == 0 :
             print(f"{numero2} es multiplo {numero1}")  
        else : 
            print(f"{numero2} no es multiplo {numero1}")  

        opcion = int(input("Desea realizar otra operación? (1=si): "))

print("Gracias por usar el sistema de ejercicios en Python.")