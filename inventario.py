#Modulo de inventario
import os

lista = []

class Articulo:
    def __init__(self, id):
        self.id = id

    def add(self, id, precio, cantidad):
        lista.append({"id" : self.id, "precio" : precio, "cantidad" : cantidad})

    def busqueda(self):
        try:
            z = [lista.index(i) for i in lista if i["id"] == self.id][0]
        except:
            z = -1
        return z

    def eliminar(self):
        i = self.busqueda()
        if i >= 0:
            lista.pop(i)
        else:
            print("Articulo no encontrado")

    def modificar(self):
        i = self.busqueda()
        if i >= 0 :
            lista[i] = input("Nuevo nombre del articulo: ")
        else:
            print("Articulo no encontrado")


def interfaz():
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Buscar articulos")
    print ("2. Agregar articulos")
    print ("3. Eliminar articulos")
    print ("4. Modificar articulos")
    print ("5. Guardar y Salir")
    print (67 * "-")

if __name__ == "__main__":


    while True:
        interfaz()

        try:
            op = int(input("Entre el numero de una opcion [1-5]: "))
        except:
            op = 6

        os.system('cls')

        if op <= 5 and op > 0:
            if op == 1:

                print (30 * "-" , "BUSCAR ARTICULO" , 30 * "-")
                art = input("\n Articulo que desea buscar: ")
                obj = Articulo(art)
                z = obj.busqueda()

                if z >= 0 :
                    print("Objeto encontrado")
                    print(lista[z])
                else:
                    print("Objeto no encontrado")

                input("\nPresione enter para continuar ")
                os.system('cls')

            elif op == 2:
                print (30 * "-" , "AGREGAR ARTICULO" , 30 * "-")
                art = input("\nNuevo articulo: ")
                precio = input("\nPrecio: ")
                cantidad = input("\nCantidad: ")
                obj = Articulo(art)
                obj.add(art, precio, cantidad)
                input("\nPresione enter para continuar ")
                os.system('cls')

            elif op == 3:
                print (30 * "-" , "ELIMINAR ARTICULO" , 30 * "-")
                print(lista)
                art = input("\nArt. por Eliminar: ")
                obj = Articulo(art)
                obj.eliminar()
                input("\nPresione enter para continuar ")
                os.system('cls')

            elif op == 4:
                print(lista)
                print (30 * "-" , "MODIFICAR ARTICULO" , 30 * "-")
                art = input("\nArticulo por modificar: ")
                obj = Articulo(art)
                obj.modificar()
                input("\nPresione enter para continuar ")
                os.system('cls')

            elif op == 5:
                f = open('inventario.txt','w')
                for el in lista:
                    f.write(el + "\n")
                f.close()
                break
        else:
            input("\nOpcion invalida. Presione enter para continuar ")
            os.system('cls')
