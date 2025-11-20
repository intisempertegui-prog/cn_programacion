import csv
import utils
import os
import client

ventas = []
FILE_PATH = '.ventas.csv'
SCHEMA = ["name", "categoria", "cantidad", "precio", "total" , "client_name"]

def _inicialite_ventas():
    with open(FILE_PATH, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=SCHEMA)
        for row in reader:
            ventas.append(row)
      

def _save_ventas_in_stoarge():
    ventas_table_tmp = f'{FILE_PATH}.tmp'
    with open(ventas_table_tmp, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=SCHEMA)
        writer.writerows(ventas)
        os.remove(FILE_PATH)
        f.close()
        os.rename(ventas_table_tmp, FILE_PATH)


def create_vent(vent):
    global ventas
    # for existing_vent in ventas:
    #     if existing_client['email']  == client['email']:
    #         print('El cliente ya existe en el sistema')
    #         break
    ventas.append(vent)


def _welcome_ventas():
    print('*' * 50)
    print("""
    Elige una opcion?
    [C] Crear venta
    [R] Listar ventas
    [D] Eliminar ventas
    [U] Actualizar ventas
    [S] Buscar ventas
    [E] Salir
    
""")

def list_ventas():    
    global ventas
    print("uid  | name | categoria | cantidad | precio | total | client_name")
    print('*' * 50)
    for idx, vent in enumerate(ventas):
        (name_client, lastname )= client.search_client_id(vent['client_name'])
        print(f'[{idx}] | {vent['name']} | {vent["categoria"]} | {vent["cantidad"]} | {vent["precio"]} | {name_client} {lastname}')


def opciones(opcion):
    if opcion == 'C':
        new_vent = {
                'name': utils._get_client_field('nombre', 'producto'),
                'categoria': utils._get_client_field('categoria', 'producto'),
                'cantidad': utils._get_client_field('cantidad', 'producto'),
                'precio': utils._get_client_field('precio', 'producto'),
                'total': utils._get_client_field('total', 'producto'),
                'client_name': utils._get_client_field('id', 'cliente')
        }
        create_vent(new_vent)
    elif opcion == 'R':
         list_ventas()
    #  elif opcion == 'D':
    #     client_id = int(utils._get_client_field('id'))
    #     delete_client(client_id)
    # elif opcion == 'U':
    #     client_id = int(utils._get_client_field('id'))
    #     new_client = {
    #             'name': utils._get_client_field('nombre', 'producto'),
    #             'lastname': utils._get_client_field('categoria', 'producto'),
    #             'company': utils._get_client_field('cantidad', 'producto'),
    #             'email': utils._get_client_field('precio', 'producto'),
    #             'position': utils._get_client_field('total', 'producto'),
    #             'position': utils._get_client_field('Nombre', 'cliente')
    #     }
    #     }
    #     update_client(client_id, new_client)
    # elif opcion == 'S':
    #     client_name = utils._get_client_field('nombre')
    #     search_client(client_name)
