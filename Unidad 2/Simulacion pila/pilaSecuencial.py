import numpy as np


class Pila:
    __pila= None
    __apuntador= 0
    __tope=0

    def __init__(self) -> None:
        self.__pila= None
        self.__apuntador= 0
        self.__tope=0

    def vacia(self):
        return (self.__apuntador==0)

    def insertar(self,elemento):
        respuesta= False
        if self.__apuntador <= self.__tope:
            self.__pila[self.__apuntador]=elemento
            self.__apuntador+=1
            respuesta= True
        return respuesta

    def suprimir(self):
        respuesta= None
        if not self.vacia() and self.__apuntador > 0:
            self.__apuntador-=1
            respuesta=self.__pila[self.__apuntador]
            self.__pila[self.__apuntador]=None
        return respuesta
            

    def mostrar(self):
        if not self.vacia():
            for i in range(self.__tope+1):
                print("Elemento {}: - {}".format(i+1,self.__pila[i]))

    def Crear(self,cantidad):
        self.__pila= np.empty(cantidad,dtype= str)
        self.__tope=cantidad
        self.__apuntador=0