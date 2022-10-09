import numpy as np


class Pila:
    __elementos = []
    __cantidad= 0
    __tope= 1

    def Crear(self):
        self.__elementos= np.empty(1,dtype=object)
        self.__cantidad= 0
        self.__tope= 1

    def Insertar(self,elem):
        if self.__tope == self.__cantidad:
            self.__tope+=1
            self.__elementos.resize(self.__tope)
        self.__elementos[self.__cantidad]=elem
        self.__cantidad+=1

    def Vacia(self):
        return (self.__cantidad==0)

    def Suprimir(self):
        resp= None
        if not self.Vacia():
            resp= self.__elementos[self.__cantidad-1]
            self.__elementos[self.__cantidad-1]=None
            self.__cantidad-=1
        return resp