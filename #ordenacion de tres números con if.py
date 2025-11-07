#ordenacion de tres números con if
pass
if opcion == 5:
        # Solicitamos al usuario los números con los cuales vamos a trabajar
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        numero3 = float(input("Ingrese el tercer numero: "))
        
        #Evaluamos Caso 1 
        if numero1 <= numero2 and numero2 <= numero3:
            menor, medio, mayor = numero1, numero2, numero3

        #Evaluamos Caso 2
        elif numero1 <= numero3 and numero3 <= numero2:
            menor, medio, mayor = numero1, numero3, numero2

        #Evaluamos Caso 3
        elif numero2 <= numero1 and numero1 <= numero3:
            menor, medio, mayor = numero2, numero1, numero3

        #Evaluamos Caso 4
        elif numero2 <= numero3 and numero3 <= numero1:
            menor, medio, mayor = numero2, numero3, numero1

        #Evaluamos Caso 5
        elif numero3 <= numero1 and numero1 <= numero2:
            menor, medio, mayor = numero3, numero1, numero2

        #Caso 6 
        else:
            menor, medio, mayor = numero3, numero2, numero1

        #Mostramos los número en orden
        print(f"El número menor es {menor}")
        print(f"El número del medio es {medio}")
        print(f"El número mayor es {mayor}")