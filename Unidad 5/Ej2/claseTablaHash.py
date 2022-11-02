import random
import numpy as np



class TablaHash:
    __elementos : object
    __cantidad : int
    __random : int

    def __init__(self,cantidad) -> None:
        self.__elementos= np.empty(cantidad,dtype=object)
        self.__cantidad= int(cantidad) 
        self.__random= random.randint(1,3)

    def getElementos(self):
        return self.__elementos

    def insertar(self,elemento):
        aux = elemento % self.__cantidad
        if self.__elementos[aux] == None:
            self.__elementos[aux]= elemento
            print("elemento insertado")
        elif self.__elementos[aux] == elemento:
            print("elemento ya insertado")
        else:
            aux2=aux
            while aux2 < self.__cantidad and self.__elementos[aux2]!=None and self.__elementos[aux2]!=elemento:
                aux2+=self.__random

            if aux2 < self.__cantidad and self.__elementos[aux2]==None:
                self.__elementos[aux2]=elemento
                print("elemento insertado")
            elif aux2 < self.__cantidad and self.__elementos[aux2]==elemento:
                print("elemento ya insertado")
            else:
                aux2=0
                while aux2 < aux !=None and self.__elementos[aux2] and self.__elementos[aux2]!=elemento:
                    aux2+=self.__random
                if aux2 < aux and self.__elementos[aux2]==None:
                    self.__elementos[aux2]=elemento
                    print("elemento insertado")
                elif aux2 < aux and self.__elementos[aux2]==elemento:
                    print("elemento ya insertado")
                else:
                    print("no se pudo insertar en la tabla")


    def buscar(self,elemento):
        aux= elemento % self.__cantidad
        if self.__elementos[aux] == elemento:
            print("elemento encontrado en la pos ",aux)
        else:
            aux2=aux
            while aux2 < self.__cantidad and self.__elementos[aux2]!=elemento:
                aux2+=self.__random
            if aux2 < self.__cantidad and self.__elementos[aux2]==elemento:
                print("elemento encontrado en la pos ",aux2)
            else:
                aux2=0
                while aux2 < aux and self.__elementos[aux2]!=elemento:
                    aux2+=self.__random
                if aux2 < aux and self.__elementos[aux2]==elemento:
                    print("elemento encontrado en la pos ",aux2)
                else:
                    print("no se pudo encontrar el elemento en la tabla")