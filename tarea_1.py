#Validar un nombre
import re

#Lista de nombres prohibidos
nompro = ["x","xx", "xxx"]

#ciclo while, si no se cumplen condiciones de validacion repite el ciclo
while True:
    z = 0
    #Entrada: nombres
    nombre = input("Escribe un nombre y presiona enter: ")
    #Condicion que limita el formato de nombre a validar
    if nombre.isalnum() == True:
        #comparar entrada "nombre" con cada elemento de lista "nompro"
        for elemento in nompro:
            #busca si existe por lo menos una coincidencia entre "nombre" y algun elemento de lista "nompro"
            if elemento == nombre:
                #Indicador de por lo menos 1 coincidencia entre "nombre" y algun elemento de "nompro"
                z = 1
                #Mensaje de coincidencia
                print("NO se aceptan palabra prohibidas")
                break
        #Si no se encontró ninguna coincidencia, nombre validado
        if z == 0:
            #mensaje de validacion
            print("Validado")
            #condicion del ciclo
            break
    elif nombre.isspace == True or nombre =="":
        print("No puede estar vacio")
    else:
        print("NO se aceptan numeros")
