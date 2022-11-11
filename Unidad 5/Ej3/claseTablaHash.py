import numpy as np
from claseNodo import Nodo



class TablaHash:
    __elementos = None
    __cantidad= 0
    __cantElementos= 0

    def __init__(self,cantidad,cantElementos) -> None:
        self.__elementos= np.full(int(cantidad),None)
        self.__cantidad=int(cantidad)
        self.__cantElementos=cantElementos

    def insertar(self,elemento):
        listaElemento= str(elemento)
        aux1=int(listaElemento[3]+listaElemento[4])
        aux2=int(listaElemento[1]+listaElemento[2])
        aux3=int(listaElemento[0])
        plegado=(aux1+aux2+aux3)%self.__cantidad
        if self.__elementos[plegado]==None:
            self.__elementos[plegado]= Nodo(elemento)
        else:
            ultimo=self.__elementos[plegado]
            while ultimo.getSiguiente()!=None:
                ultimo=ultimo.getSiguiente()
            ultimo.setSiguiente(Nodo(elemento))

    def buscar(self,elemento):
        listaElemento= str(elemento)
        aux1=int(listaElemento[3]+listaElemento[4])
        aux2=int(listaElemento[1]+listaElemento[2])
        aux3=int(listaElemento[0])
        plegado=(aux1+aux2+aux3)%self.__cantidad
        if self.__elementos[plegado].getDato()==elemento:
            print("Elemento encontrado en la posicion ",plegado)
        else:
            nodoBuscar=self.__elementos[plegado]
            i=0
            while nodoBuscar.getSiguiente()!=None and nodoBuscar.getSiguiente().getDato()!= elemento:
                nodoBuscar = nodoBuscar.getSiguiente()
                i+=1
            if nodoBuscar.getSiguiente()!=None:
                print("Elemento encontrado en la posicion ",plegado," en el subindice ",i)
            else:
                print("Elemento no encontrado")

    def mostrar(self):
        mayoresPromedio=0
        for i in range(self.__cantidad):
            j=0
            print("-- Lista ",i+1)
            sig=self.__elementos[i]
            while sig != None:
                print(sig.getDato())
                sig=sig.getSiguiente()
                j+=1
            print("-- Longitud: ",j)
            print("--------------")
            if (j)<=3 and (j)>self.__cantElementos/self.__cantidad:
                mayoresPromedio+=1
        print("--- Promedio: ",(self.__cantElementos/self.__cantidad))
        print("--- MAYORES AL PROMEDIO: ",mayoresPromedio)
            