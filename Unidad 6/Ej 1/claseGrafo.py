
import numpy as np


class Grafo:
    __vertices=None
    __matrizAdyacencia=None
    __matrizPeso=None
    __esAciclico=True

    def __init__(self,vertices:list):
        n=len(vertices) 
        self.__vertices=np.full(n,None)
        for i in range(n):
            self.__vertices[i]=vertices[i]
        self.__matrizAdyacencia= np.full((n,n),None)
        print(self.__matrizAdyacencia)
        self.__esAciclico=True

    def Mostrar(self):
        print(self.__matrizAdyacencia)

    def Buscar(self,v):
        i=0
        b=False
        while not b and i < len(self.__vertices):
            if self.__vertices[i]==v:
                b=not b
            else:
                i+=1
        if i==len(self.__vertices):
            i=-1
        return i

    def NuevaArista(self,u,v):
        i=0
        a=-1
        b=-1
        ambosEncontrados=False
        while not ambosEncontrados and i < len(self.__vertices):
            if self.__vertices[i]==u:
                a=i
            if self.__vertices[i]==v:
                b=i
            
            if a!=-1 and b!=-1:
                ambosEncontrados=True
            i+=1
        
        if a!=-1 and b!=-1:
            self.__matrizAdyacencia[a][b]=True
            # self.__matrizAdyacencia[b][a]=True
            print("Arista agregada")
        else:
            print("Error - un vertice no existe")


    def Adyacentes(self,u):
        ind=0
        b=True
        while ind < len(self.__vertices) and b:
            if self.__vertices[ind]== u:
                b=False
            else:
                ind+=1
        if b:
            print("Error - el elemento no se encontro")
        else:
            n=False
            adyacentes=[]
            for i in range(len(self.__vertices)):
                if self.__matrizAdyacencia[ind][i] != None:
                    adyacentes.append(self.__vertices[i])
                    n=True
        return adyacentes


    def Camino(self,u,v):
        a=self.Buscar(u)
        b=self.Buscar(v)

        if a == -1 and b == -1:
            print("Error - alguno de los vertices no es correcto")
        elif a == b:
            return [self.__vertices[b]]
        else:
            camino=self._Camino(a,b,[])
            return camino
    
    def _Camino(self,a,b,cam:list):
        if self.__vertices[a] == self.__vertices[b]:
            return [self.__vertices[b]]
        else:
            cam.append(self.__vertices[a])
            for nodo in self.Adyacentes(self.__vertices[a]):
                if nodo not in cam:
                    recorrido = self._Camino(self.Buscar(nodo), b, cam)
                    if recorrido != None:
                        return [self.__vertices[a]] + recorrido
            return None
                        
            
    # def CaminoMinimo(self,u,v):
    #     pass

    def Conexo(self):
        respuesta= False
        i=0
        b=True

        while b and i < len(self.__vertices):
            if len(self.REA(self.__vertices[i])) == len(self.__vertices):
                i+=1
            else:
                b=False
        if b:
            respuesta=True
        return respuesta


    def Aciclico(self):
        respuesta=True
        for nodo in self.__vertices:
            for nodo2 in self.Adyacentes(nodo):
                for nodo3 in self.Adyacentes(nodo2):
                    if nodo3 in self.Adyacentes(nodo):
                        respuesta=False
        return respuesta

    def Aciclico2(self):
        self.__esAciclico=True
        i=0
        while self.__esAciclico and i < len(self.__vertices):
            self.REP(self.__vertices[i],[])
            i+=1
        return self.__esAciclico

    def ArbolRecubrimiento(self):
        pass

    def REA(self,nodo):
        conocidos=[]
        cola=[nodo]

        while len(cola)>0:
            nodoConocido= cola.pop(0)
            if conocidos.count(nodoConocido)==0:
                conocidos.append(nodoConocido)
            for n in self.Adyacentes(nodoConocido):
                if conocidos.count(n)==0:
                    cola.append(n)
                    conocidos.append(n)
        return conocidos

    def REP(self,nodo,conocidos=[]):
        conocidos.append(nodo)
        for nodoAdyacente in self.Adyacentes(nodo):
            if conocidos.count(nodoAdyacente)==0:
                self.REP(nodoAdyacente,conocidos)
            else:
                self.__esAciclico=False
        return conocidos