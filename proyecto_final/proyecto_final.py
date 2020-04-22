#Autenticacion rudimentaria
import getpass
import os

usr_list = {}

def print_menu():
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Crear credenciales")
    print ("2. Validar credenciales")
    print ("3. Salir")
    print (67 * "-")

def print_menu_cred():
    print (30 * "-" , "CREAR CREDENCIALES" , 30 * "-")
    usr = input("Nuevo usuario: ")
    pasw = getpass.getpass("Nueva contraseña: ")
    usr_list[usr] = pasw
    os.system('cls')

def print_menu_auth():
    print (30 * "-" , "AUTENTICACION" , 30 * "-")
    musr = input("Usuario: ")
    mpasw = getpass.getpass("Contraseña: ")

    a = 0
    for key, value in usr_list.items():
        if key == musr:
            if value == mpasw:
                print("\nvalido.")
            else:
                print("\ncontraseña invalida.")
        else:
            a += 1
            if a == len(usr_list):
                print("\nusuario invalido")
    input("\nPresione enter para continuar. ")
    os.system('cls')

if __name__ == "__main__":

    while True:
        print_menu()

        try:
            op = int(input("Entre el numero de una opcion [1-3]: "))
        except:
            op = 4

        if op <= 3 and op > 0:
            if op == 1:
                os.system('cls')
                print_menu_cred()
            elif op == 2 and len(usr_list) != 0:
                os.system('cls')
                print_menu_auth()
            elif op == 3:
                f = open('creds.txt','w')
                for usr, pass in usr_list.items():
                    f.write("User: " + str(usr) + ", Password: " + str(pass) + "\n")
                f.close()
                break
            else:
                input("\nNo existen usuarios. Presione enter para continuar")
                os.system('cls')
        else:
            input("\nOpcion invalida. Presione enter para continuar ")
            os.system('cls')
