#Autenticacion rudimentaria
import re
import os
import time

def print_menu():       ## Your menu design here
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Crear credenciales")
    print ("2. Validar credenciales")
    print ("3. Salir")
    print (67 * "-")

usr_list = []
pasw_list = []


while True:
    a = 0
    print_menu()    ## Displays menu
    choice = int(input("Entre el numero de una opcion [1-3]: "))
    os.system('cls')
    if choice==1:
        print (30 * "-" , "CREAR CREDENCIALES" , 30 * "-")
        usr = input("Nuevo usuario: ")
        usr_list.append(usr)
        pasw = input("Nueva contraseña: ")
        pasw_list.append(pasw)
        os.system('cls')
    elif choice==2 and len(usr_list) !=0:
        print (30 * "-" , "AUTENTICACION" , 30 * "-")
        musr = input("usuario: ")
        mpasw = input("contraseña: ")

        for el in usr_list:
            if el == musr:
                if mpasw == pasw_list[usr_list.index(el)]:
                    print("valido.")
                else:
                    print("contraseña invalida.")
            else:
                a+=1
                print(len(usr_list))
                if a == len(usr_list):
                    print("usuario invalido")
        time.sleep(3)
        os.system('cls')
    elif choice==3:
        break
    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("Error!")
