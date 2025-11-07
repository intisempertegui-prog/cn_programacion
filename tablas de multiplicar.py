# PROGRAMA: TABLAS DE MULTIPLICAR PERSONALIZADAS

while True:
    print("Menu tablas de multiplicar:")
    print("1. Generar varias tablas")
    print("2. Generar una tabla específica")
    print("3. Salir")
    
    opcion = input("Seleccione una opción 1-3:")
    
    if opcion == "1":
        n_tablas = int(input("¿Cuántas tablas quieres generar?:"))
        limite = int(input("¿Hasta qué número quieres multiplicar?:"))
        
        for i in range(1, n_tablas + 1):
            print(f"\nTabla del {i}:")
            for j in range(1, limite + 1):
                print(f"{i} x {j} = {i * j}")

    elif opcion == "2":
        tabla = int(input("¿Qué tabla quieres generar?:"))
        limite = int(input("¿Hasta qué número quieres multiplicar?:"))
        
        print(f"\nTabla del {tabla}:")
        for j in range(1, limite + 1):
            print(f"{tabla} x {j} = {tabla * j}")

    elif opcion == "3":
        print("Gracias por usar el programa")
        break

    else:
        print("Opción inválida. Intente nuevamente")