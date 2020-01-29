#Validar una cedula
import re

#Entrada
while True:
    str = input("Escribe una cedula con guiones y presiona enter: ")
    if str.isalnum() == True:
        print("Escribe los guiones")
    for el in str.split("-"):
        if el.isalnum() == False:
            print("Solo letras y numeros")
            break



        

num = re.findall(r'[0-9]+', str)
letr = re.findall(r'[a-z]+', str, re.IGNORECASE)



print(num, letr)
