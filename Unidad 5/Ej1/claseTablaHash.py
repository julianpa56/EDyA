import os
import numpy as np



import numpy as np



class TablaHash:
    __elementos : object
    __cantidad : int

    def __init__(self,cantidad) -> None:
        self.__elementos= np.empty(cantidad,dtype=object)
        self.__cantidad= int(cantidad) 

    def getElementos(self):
        return self.__elementos

    def insertar(self,elemento):
        aux = elemento % self.__cantidad
        if self.__elementos[aux] == None:
            self.__elementos[aux]= elemento
        else:
            aux2= ((aux+1) % self.__cantidad)
            while self.__elementos[aux2]!=None and aux2 != aux:
                if aux2 == self.__cantidad:
                    aux2= 0
                else:
                    aux2+=1
            
            if aux2 == aux:
                print("la tabla esta llena")
            else:
                self.__elementos[aux2]=elemento

    def buscar(self,elemento):
        aux= elemento % self.__cantidad
        if self.__elementos[aux] == elemento:
            print("elemento encontrado en la pos ",aux)
        else:
            aux2= ((aux+1) % self.__cantidad)+1
            while self.__elementos[aux2]!= elemento and aux2 != aux:
                if aux2 == self.__cantidad:
                    aux2= 0
                else:
                    aux2+=1
            
            if aux2 == aux:
                print("elemento no encontrado")
            else:
                print("elemento encontrado en la pos: ",aux2," ELEMENTO: ",self.__elementos[aux2])
            




if __name__=='__main__':
    os.system("cls")
    tabla= TablaHash(10)

    tabla.insertar(5)
    tabla.insertar(15)
    tabla.insertar(6)
    tabla.insertar(16)
    tabla.insertar(8)
    tabla.insertar(9)
    tabla.insertar(10)
    tabla.insertar(2)
    tabla.insertar(3)
    tabla.insertar(1)

    print(tabla.getElementos())
    tabla.buscar(16)