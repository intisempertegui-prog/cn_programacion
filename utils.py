def _welcome():
    print('*' * 58)
    print('\tBienvenidos al sistema de ventas Cenestur')
    print('*' * 58)
    print('Elige una opcion')
    print('*' * 58)
    print("""[1] Clientes
[2] Ventas
[3] Calcular Ventas
[4] Promedio de ventas por cliente
[5] Salir de clientes""")
    print('*' * 58)

def _get_client_field(field_name, opcion):
    """ Esta es la funcion para solictar clientes """
    field_value = None
    while not field_value:
        field_value = input(f'Ingrese el {field_name} del {opcion}: ')
        if field_value == 'exit':
            field_value = None
            break
    if not field_value:
        print('Saliendo...')
        sys.exit()

    return field_value
