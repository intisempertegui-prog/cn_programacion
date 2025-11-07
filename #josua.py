#josua

saldo = float(input("Ingrese su saldo actual: "))

# Bucle principal
while True:
    # Menú principal
    opcion = int(input("""
==============================
   SISTEMA DE GESTIÓN BANCARIA
==============================
1. Depositar dinero
2. Retirar dinero
3. Salir
------------------------------
Seleccione una opción (1-3): 
"""))

    if opcion == 1:
        # Depósito
        monto = float(input("Ingrese el monto a depositar: "))

        if monto > 0:
            saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")

            # Bono del 0.5% si el depósito es mayor a 500
            if monto > 500:
                bono = monto * 0.005
                saldo += bono
                print(f"Bono de ${bono:.2f} aplicado. Saldo final: ${saldo:.2f}")
            else:
                print("No se aplicó bono.")
        else:
            print("El monto debe ser mayor que cero.")

    elif opcion == 2:
        # Retiro
        monto = float(input("Ingrese el monto a retirar: "))

        if monto > 0:
            if monto <= saldo:
                saldo -= monto
                print(f" Retiro exitoso. Nuevo saldo: ${saldo:.2f}")

                # Comisión del 0.02% si el retiro es mayor a 1000
                if monto > 1000:
                    comision = monto * 0.0002
                    saldo -= comision
                    print(f"Comisión de ${comision:.2f} aplicada. Saldo final: ${saldo:.2f}")
                else:
                    print("No se aplicó comisión.")
            else:
                print("No tiene suficiente saldo para realizar el retiro.")
        else:
            print("El monto debe ser mayor que cero.")

    elif opcion == 3:
        print("\nGracias por usar el sistema bancario. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente nuevamente.")

    # Preguntar si desea continuar
    continuar = input("\n¿Desea realizar otra operación? (s/n): ").lower()
    if continuar != 's':
        print("\nGracias por usar el sistema bancario")
        break