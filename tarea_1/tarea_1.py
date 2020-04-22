#Validar un nombre

#Lista de nombres prohibidos
nompro = ["x","xx", "xxx"]

def validador(nombre):
    #centinela
    z = 0
    #comparar entrada "nombre" con cada elemento de lista "nompro"
    for x in nompro:
        #busca si existe por lo menos una coincidencia entre "nombre" y algun elemento de lista "nompro"
        if x == nombre:
            #Indicador de coincidencia entre "nombre" y algun elemento de "nompro"
            z = 1
    return z


if __name__ == "__main__":

    #ciclo while, si no se cumplen condiciones de validacion repite el ciclo
    while True:
        #Entrada: cualquier string
        nombre = input("Escribe un nombre y presiona enter: ")
        #Llama a la funcion validador para determinar si la entrada es validada o no
        z = validador(nombre)
        if z == 0:
            print("\nValidado\n")
            break
        else:
            print("\nNO se aceptan palabra prohibidas\n")
