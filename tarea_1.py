#Validar un nombre
import re

#Lista de nombres prohibidos, fuente: http://fffff.at/googles-official-list-of-bad-words/
nompro = ["x","xx", "xxx"]
#variable para ciclo while
run = True
z = 0
#ciclo while, si no se cumplen condiciones de validacion repite el ciclo
while run == True:
    z=0
    #Entrada: nombres
    nombre = input("Escribe un nombre y presiona enter: ")
    #Condicion que limita el formato de nombre a validar
    if nombre.isalpha() == True:
        #Ciclo para comparar entrada "nombre" con cada elemento de lista "nompro"
        for elemento in nompro:
            #Expresion regular que busca si existe por lo menos una coincidencia entre "nombre" y algun elemento de lista "nompro"
            if re.search(rf"\b(?=\w){nombre}\b(?!\w)", elemento, re.IGNORECASE) != None:
                #Indicador de por lo menos 1 coincidencia entre "nombre" y algun elemento de "nompro"
                z = 1
                #Mensaje de coincidencia
                print("NO se aceptan palabra prohibidas")
        #Si no se encontró ninguna coincidencia, nombre validado
        if z == 0:
            #mensaje de validacion
            print("Validado")
            #condicion del ciclo
            run = False
    elif nombre.isspace == True or nombre =="":
        print("No puede estar vacio")
    else:
        print("NO se aceptan numeros")
