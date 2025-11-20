import client
import ventas
import utils

def run():

    
    utils._welcome()
    comand = input("ingrese el comando: ").upper()

    if comand == '1':
        client._inicialite_client()
        client._welcome_client()
        comand_c = input("ingrese la opcion: ").upper()
        client.opciones(comand_c)
        client._save_cliente_in_stoarge()
    elif comand == '2':
        client._inicialite_client()
        ventas._inicialite_ventas()
        ventas._welcome_ventas()
        comand_v = input("ingrese la opcion: ").upper()
        ventas.opciones(comand_v)
        ventas._save_ventas_in_stoarge()

        
    else:
        print('Saliendo...')
    

if __name__ == "__main__":
    run()