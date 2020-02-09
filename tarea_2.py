#Validar una cedula
import re
#Lista de provincias en orden adecuado, (indice en lista = numpro -1)
prov = ["1-Bocas del Toro","2-Coclé", "3-Colón", "4-Chiriquí","5-Darién","6-Herrera","7-Los Santos",
"8-Panamá", "9-Veraguas", "10-Guna Yala", "11-Emberá Wounaan","12-Ngäbe-Buglé","13-Panamá Oeste"]
#Ciclo que se rompe cuando la entrada es una cedula valida
while True:
    str = input("Escribe una cedula con guiones y presiona enter: ") #Entrada: cualquier string

    if re.fullmatch(r'^\d{1,2}(pi|av|)-\d{1,4}-\d{1,5}$', str, re.I) != None: #regex que coincide con el formato de cedula tipo regular o poblacion indigena o antes de vigencia
        num = re.findall(r'\d{1,5}', str) #metodo que encuentra elementos formados por 1 a 6 digitos y crea un lista de strings con los elementos
        letr = re.findall(r'pi|av', str, re.I) #metodo que encuentra elementos formados por 1 a 2 letras alfabeticas y crea un lista de strings con los elementos

        if int(num[0])<=13 and int(num[0])>0: #check si el numero de provincia coincide con un elemento real
            print("cedula valida") #mensaje de salida
            if not letr:
                print("tipo de cedula: Regular") #
            elif letr[0].lower() =="pi":
                print("tipo de cedula:"+ letr[0] + " Poblacion indigena") #
            else:
                print("tipo de cedula:"+ letr[0] +" Antes de la vigencia") #
            print("provincia: " + prov[int(num[0])-1] + " tomo: " + num[1] + " asiento: " + num[2]) #
            break
        else:
            print("provincia invalida") #Mensaje de error

    elif re.fullmatch(r'^(n|pe)-\d{1,4}-\d{1,5}$|^e-\d{1,4}-\d{1,6}$', str, re.I) != None: #regex que coincide con el formato de cedula tipo naturalizado,extranjero, panameño nacido exterior
        num = re.findall(r'\d{1,6}', str) #metodo que encuentra elementos formados por 1 a 6 digitos y crea un lista de strings con los elementos
        letr = re.findall(r'n|pe|e', str, re.I) #metodo que encuentra elementos formados por 1 a 2 letras alfabeticas y crea un lista de strings con los elementos

        print("cedula valida") #mensaje de salida
        if letr[0].lower() =="n":
            print("tipo de cedula: Naturalizado") #
        elif letr[0].lower() =="pe":
            print("tipo de cedula: Panameño nacido en el extranjero") #
        else:
            print("tipo de cedula: Extranjero") #
        print("tomo: " + num[0] + " asiento: " + num[1]) #
        break
    else:
        print("cedula invalida") #Mensaje de error
