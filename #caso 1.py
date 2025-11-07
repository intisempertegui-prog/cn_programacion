#caso 1
saldo = float(input("Ingrese el saldo inicial de la cuenta bancaria: "))
while True:
   
    opcion = int(input("""
    Bienvenido al sistema de gestión bancaria.
    \n1. Depositar dinero.
    \n2. Retirar dinero.
    \n3. Salir.
    \nSeleccione opcion (1-3):
    """))

    if opcion == 1:
        monto = float(input("Ingrese la cantidad a depositar: "))
        if monto > 0: 
            saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")

            if monto > 500:
                bono = monto * 0.05
                saldo += bono
                print(f"Bono de ${bono:.2f} aplicado. Saldo final: ${saldo:.2f}")
            else:
                print("No se aplicó bono")
        else:
            print("El monto debe ser mayor que cero.")

    elif opcion == 2:
        monto = float(input("Ingrese la cantidad a retirar: "))
        if monto > 0:
            if monto <= saldo:
                saldo -= monto
                print(f" Retiro exitoso. Nuevo saldo: ${saldo:.2f}")

                if monto > 1000:
                    comision = monto * 0.02
                    saldo -= comision
                    print(f"Comisión de ${comision:.2f} aplicada. Saldo final: ${saldo:.2f}")
                else:
                    print("No se aplicó comisión.")
            else:
                print("No tiene suficiente saldo para realizar el retiro.")
        else:
            print("El monto debe ser mayor que cero.")

    elif opcion == 3:
        print("\nGracias por usar su sistema bancario de confianza")
        break
    
    else:
        print("Opcion invalida intente de nuevo")

    continuar = input("\n¿Desea realizar otra operación? (s/n): ").lower()
    if continuar != 's':
        print("\nGracias por usar el sistema bancario")
        break

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