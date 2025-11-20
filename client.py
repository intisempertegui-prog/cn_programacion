import csv
import os
import sys
import utils

clients = []
FILE_PATH = '.client.csv'
SCHEMA = ['name','lastname','company','email','position']


def _inicialite_client():
    with open(FILE_PATH, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=SCHEMA)
        for row in reader:
            clients.append(row)
      

def _save_cliente_in_stoarge():
    client_table_tmp = f'{FILE_PATH}.tmp'
    with open(client_table_tmp, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=SCHEMA)
        writer.writerows(clients)
        os.remove(FILE_PATH)
        f.close()
        os.rename(client_table_tmp, FILE_PATH)


def _welcome_client():
    print('*' * 50)
    print("""
    Elige una opcion?
    [C] Crear cliente
    [R] Listar clientes
    [D] Eliminar cliente
    [U] Actualizar cliente
    [S] Buscar cliente
    [E] Salir
    
""")
    


def create_client(client):
    """ Funcion para crear clientes\n 
        cluients es un parametro
    """
    global clients
    for existing_client in clients:
        if existing_client['email']  == client['email']:
            print('El cliente ya existe en el sistema')
            break
    clients.append(client)


def update_client(client_id, client_new):
    global clients
    if len(clients) - 1 >= client_id and client_id>=0:
        clients[client_id] = client_new
    else:
        pass
   

def delete_client(client_id):
    global clients
    if len(clients) - 1 >= client_id and client_id>=0:
        clients.pop(client_id)
    else:
        pass


def search_client(client_name):
    global clients
    for client in clients:
        if client['name'] != client_name:
           continue
        else:
            print(f'El cliente {client_name} existe')


def search_client_id(client_id):
    global clients
    for uid, clint in enumerate(clients):

        if uid != int(client_id):
            continue
        else:
            return [clint["name"], clint['lastname']]    
    


def list_clients():    
    global clients
    print("uid  | name | lastname | company | email | position")
    print('*' * 50)
    for idx, client in enumerate(clients):
        print(f'[{idx}] | {client['name']} | {client["lastname"]} | {client["company"]} | {client["email"]} | {client["position"]}')



def opciones(opcion):
    if opcion == 'C':
        new_client = {
                'name': utils._get_client_field('nombre', 'cliente'),
                'lastname': utils._get_client_field('apellido', 'cliente'),
                'company': utils._get_client_field('empresa', 'cliente'),
                'email': utils._get_client_field('email', 'cliente'),
                'position': utils._get_client_field('puesto', 'cliente')
        }
        create_client(new_client)
    elif opcion == 'R':
        list_clients()
    elif opcion == 'D':
        client_id = int(utils._get_client_field('id', 'cliente'))
        delete_client(client_id)
    elif opcion == 'U':
        client_id = int(utils._get_client_field('id', 'cliente'))
        new_client = {
                'name': utils._get_client_field('nombre', 'cliente'),
                'lastname': utils._get_client_field('apellido', 'cliente'),
                'company': utils._get_client_field('empresa', 'cliente'),
                'email': utils._get_client_field('email', 'cliente'),
                'position': utils._get_client_field('puesto', 'cliente')
        }
        update_client(client_id, new_client)
    elif opcion == 'S':
        client_name = utils._get_client_field('nombre', 'cliente')
        search_client(client_name)