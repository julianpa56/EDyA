
import numpy as np


class ColaSecuencial:
    __cola= None
    __tamanio= 0
    __cantidad=0
    __incremento=1


    def __init__(self) -> None:
        self.__cola= None
        self.__tamanio= 0
        self.__cantidad=0
        self.__incremento=1

    def Crear(self, cantidad):
        self.__cola= np.empty(cantidad)
        self.__tamanio= cantidad
    
    def Vacia(self):
        respuesta= False
        if self.__cantidad==0:
            respuesta= True
        return respuesta
    
    def Insertar(self,elemento):        
        if self.__cantidad==self.__tamanio:
            self.__tamanio+=self.__incremento
            self.__cola.resize(self.__tamanio)
        self.__cola[self.__cantidad]=elemento
        self.__cantidad+=1
    
    def Suprimir(self):
        respuesta= None
        if not self.Vacia():
            respuesta= self.__cola[0]
            i=1
            while i < self.__cantidad:
                self.__cola[i-1]=self.__cola[i]
                i+=1
            self.__cantidad-=1
        return respuesta

    def Recorrer(self):
        
        for i in range(self.__cantidad):
            print("Posicion en la fila: ",i+1," - Elemento: ", self.__cola[i])
