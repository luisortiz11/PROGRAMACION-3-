#Validar un nombre

import re

antinombre = ["x","xx", "xxx"]
run = True

while run == True:
    z = 0

    nombre = input("Escribe un nombre y presiona enter: ")

    if nombre.isalpha() == True:
        for elemento in antinombre:
            if re.search(rf"\b(?=\w){nombre}\b(?!\w)", elemento, re.IGNORECASE):
                z = 1
                print("NO se aceptan palabra prohibidas")
        if z == 0:
            print("Validado")
            run = False
    else:
        print("NO se aceptan numeros")
