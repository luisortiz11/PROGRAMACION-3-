#Autenticacion rudimentaria
#Luis Ortiz
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
    while True:
        usr = input("Nuevo usuario: ")
        pasw = getpass.getpass("Nueva contraseña: ")
        z = 0
        for el in list(usr_list.keys()):
            if el == usr:
                print("Usuario existente. Entre otro usuario.")
            else:
                z +=1
        if z == len(list(usr_list.keys())):
            usr_list[usr] = pasw
            z = 0
            break

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
                for i, j in usr_list.items():
                    f.write("User: " + str(i) + ", Password: " + str(j) + "\n")
                f.close()
                break
            else:
                input("\nNo existen usuarios. Presione enter para continuar")
                os.system('cls')
        else:
            input("\nOpcion invalida. Presione enter para continuar ")
            os.system('cls')
