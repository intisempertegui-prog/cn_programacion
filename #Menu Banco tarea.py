#caso 2
cuenta_bancaria = 4000

opcion = int(input("""
Bienvenido al sistema de gestión bancaria.
\n1. Depositar dinero
\n2. Retirar dinero.
\nSeleccione opcion (1-2):
"""))

if opcion == 1:
    deposito = float(input("Ingrese la cantidad a depositar: "))
    if deposito < 10000:
        cuenta_bancaria += deposito
        if deposito > 2000:
            cuenta_bancaria += cuenta_bancaria*0.1
        print(f"El deposito de {deposito} se efectuo de forma exitosa.")
        print("El balance de cuenta es: ",cuenta_bancaria)
    
if opcion == 2:
    retiro = float(input("Ingrese la cantidad a retirar: "))
    if retiro < 10000:
        cuenta_bancaria -= cuenta_bancaria * 0.05
        if deposito > 2000:
            cuenta_bancaria += cuenta_bancaria*0.1
        print(f"El deposito de {deposito} se efectuo de forma exitosa.")
        print("El balance de cuenta es: ",cuenta_bancaria)  