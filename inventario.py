#Modulo de inventario
import os

lista = []

class articulo:
    def __init__(self, id):
        self.id = id

    def add(self):
        lista.append(self.id)


def interfaz():
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Buscar articulos")
    print ("2. Agregar articulos")
    print ("3. Eliminar articulos")
    print ("4. Modificar articulos")
    print ("5. Guardar y Salir")
    print (67 * "-")

def busqueda():
    z = 0
    art = input("Entre articulo a buscar: ")

    for e in lista:
        if e == art:
            print("Articulo encontrado")
            z = 1
            break
    if z == 0:
        print("Articulo no encontrado")


def agregar():
    print (30 * "-" , "AGREGAR ARTICULO" , 30 * "-")
    art = input("\nNuevo articulo: ")
    objeto = articulo(art)
    objeto.add()
    os.system('cls')



def eliminar():
    print (30 * "-" , "ELIMINAR ARTICULO" , 30 * "-")
    print(lista)
    art = input("\nArt. por Eliminar: ")
    i = 0
    z = 0
    for e in lista:
        if e == art:
            lista.pop(i)
            z = 1
            break
        i += 1
    if z == 0:
        print("Articulo no encontrado")


def modificar():
    print(lista)
    print (30 * "-" , "MODIFICAR ARTICULO" , 30 * "-")
    art = input("\nArticulo por modificar: ")
    i = 0
    z = 0
    for e in lista:
        if e == art:
            z = 1
            lista[i] = input("Nuevo nombre del articulo: ")
            break
        i += 1
    if z == 0:
        print("Articulo no encontrado")

def data_txt():
    f = open('inventario.txt','w')
    for el in lista:
        f.write(el + "\n")
    f.close()


if __name__ == "__main__":


    while True:
        interfaz()

        try:
            op = int(input("Entre el numero de una opcion [1-5]: "))
        except:
            op = 6

        if op <= 5 and op > 0:
            if op == 1:
                os.system('cls')
                busqueda()
            elif op == 2:
                os.system('cls')
                agregar()
            elif op == 3:
                os.system('cls')
                eliminar()
            elif op == 4:
                os.system('cls')
                modificar()
            elif op == 5:
                data_txt()
                break
        else:
            input("\nOpcion invalida. Presione enter para continuar ")
            os.system('cls')
