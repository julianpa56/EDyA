from claseNodo import Nodo


class ArbolBinario:
    
    __raiz: Nodo

    def __init__(self):
        self.__raiz= None

    def vacio(self):
        return (self.__raiz == None)

    def raiz(self):
        return self.__raiz

    def mostrarRaiz(self):
        return self.__raiz.obtenerItem()

    def insertar(self,item):
        aux= Nodo()
        aux.cargarItem(item)
        aux.cargarIzq(None)
        aux.cargarDer(None)
        if self.vacio():
            self.__raiz=aux
        else:
            self._insertar(self.raiz(),aux)

    def _insertar(self, arbol: Nodo, aux: Nodo):

        if(arbol == None):
            return aux
        elif (arbol.obtenerItem() == aux.obtenerItem()):
            print("Error - Elemento ya existente")
            return None
        elif (arbol.obtenerItem() > aux.obtenerItem()):
            # print('A: ',arbol.obtenerItem(),' - B: ',aux.obtenerItem())
            if arbol.obtenerIzq()==None:
                arbol.cargarIzq(aux)
            else:
                self._insertar(arbol.obtenerIzq(),aux)

        elif (arbol.obtenerItem() < aux.obtenerItem()):
            # print('A: ',arbol.obtenerItem(),' - B: ',aux.obtenerItem())
            if arbol.obtenerDer()==None:
                arbol.cargarDer(aux)
            else:
                self._insertar(arbol.obtenerDer(),aux)
        else:
            print("Error en la insercion")
            return None

    def suprimir(self, item):
        if self.vacio():
            print("Error - Arbol vacio")
        elif self.__raiz.obtenerItem() == item:
            if self.__raiz.obtenerIzq()== None and self.__raiz.obtenerDer() == None:
                self.__raiz=None
                print("Raiz eliminada")
            elif self.__raiz.obtenerIzq()== None or self.__raiz.obtenerDer() == None:
                if self.__raiz.obtenerIzq()== None:
                    self.__raiz= self.__raiz.obtenerDer()
                    print("Nuevo nodo raiz: Hijo derecho")
                else:
                    self.__raiz= self.__raiz.obtenerIzq()
                    print("Nuevo nodo raiz: Hijo izquierdo")
            else:
                aux= self.raiz().obtenerIzq()
                anterior2= aux
                while aux.obtenerDer() != None:
                    anterior= aux
                    aux= aux.obtenerDer()
                anterior.cargarDer(aux.obtenerIzq())
                self.__raiz.cargarItem=aux.obtenerItem()
                aux=None
        else:
            aux= self.raiz()
            anterior= aux
            b=True
            while aux != None and b:
                if aux.obtenerItem() < item:
                    anterior=aux
                    aux= aux.obtenerDer()
                elif aux.obtenerItem() > item:
                    anterior=aux
                    aux= aux.obtenerIzq()
                else:
                    b= False
            print("Aqui anterior: ",anterior.obtenerItem())
            print("Aqui aux: ",aux.obtenerItem())
            if not b:
                if aux.obtenerDer()!= None: # Si posee elementos a su derecha
                    print("entra---")
                    aux2= aux.obtenerDer()
                    anterior2=aux2
                    while aux2.obtenerIzq() != None:
                        anterior2= aux2
                        aux2= aux2.obtenerIzq()
                    print("Aqui anterior2: ",anterior2.obtenerItem())
                    print("Aqui aux2: ",aux2.obtenerItem())
                    if aux2.obtenerItem() != anterior2.obtenerItem():
                        anterior2.cargarIzq(aux2.obtenerDer())
                        aux.cargarItem(aux2.obtenerItem())
                        aux2=None
                    else:
                        aux.cargarItem(aux2.obtenerItem())
                        aux.cargarDer(aux2.obtenerDer())
                else:
                    anterior.cargarDer(None)
            else:
                print("Error - elemento no encontrado")


    def _buscar(self,item):
        aux= self.raiz()

        while aux != None and aux.obtenerItem() != item:
            if aux.obtenerItem() < item:
                aux= aux.obtenerDer()
            else:
                aux= aux.obtenerIzq()
        return aux

    def hijo(self,hijo,padre):
        respuesta= False
        aux= self._buscar(padre)
        if aux == None:
            print("Error - Padre no encontrado")
            respuesta= False
        elif aux.obtenerIzq().obtenerItem() == hijo or aux.obtenerDer().obtenerItem() == hijo:
            respuesta= True
        else:
            respuesta= False
        return respuesta

    def padre(self,padre,hijo):
        return self.hijo(hijo,padre)

    def buscar(self,item):
        aux= self._buscar(item)

        if aux == None:
            print("No se encontro el elemento")
        else:
            print("El elemento {} tiene los hijos {} y {}".format(item,aux.obtenerDer().obtenerItem(),aux.obtenerIzq().obtenerItem()))
    
    def hoja(self,item):
        respuesta= False
        aux= self._buscar(item)
        if aux == None:
            print("Error - Elemento no encontrado")
        elif aux.obtenerIzq() == None and aux.obtenerDer() == None:
            respuesta= True
        else:
            respuesta= False
        return respuesta

    def camino(self,nodoA,nodoB):
        aux= self._buscar(nodoA)
        aux2= self._buscar(nodoB)
        if aux==None or aux2==None:
            print("Error - El primer item no existe")
        else:
            b=True
            while aux !=None and b:
                if aux.obtenerItem() == nodoB:
                    b= False
                elif aux.obtenerItem() < nodoB:
                    aux= aux.obtenerIzq()
                else:
                    aux= aux.obtenerDer()
            if b:
                print("No existe camino entre ",nodoA," y el nodo ",nodoB)
            else:
                print("Existe camino entre ",nodoA," y el nodo ",nodoB)

    def inOrden(self):
        aux= self.raiz()
        self._inOrden(aux)

    def _inOrden(self,nodo):
        if nodo!=None:
            self._inOrden(nodo.obtenerDer())
            print(nodo.obtenerItem())
            self._inOrden(nodo.obtenerIzq())

    def preOrden(self):
        aux= self.raiz()
        self._preOrden(aux)
    def _preOrden(self,nodo):
        if nodo!=None:
            print(nodo.obtenerItem())
            self._preOrden(nodo.obtenerIzq())
            self._preOrden(nodo.obtenerDer())

    def postOrden(self):
        aux= self.raiz()
        self._postOrden(aux)
    def _postOrden(self,nodo):
        if nodo!=None:
            self._postOrden(nodo.obtenerIzq())
            self._postOrden(nodo.obtenerDer())
            print(nodo.obtenerItem())

    def altura(self):
        aux= self.raiz()
        return(self._altura(aux))
    def _altura(self, nodo: Nodo, i=0):
        if nodo!=None:
            aux1=self._altura(nodo.obtenerIzq(),i+1)
            aux2=self._altura(nodo.obtenerDer(),i+1)
            return max(aux1,aux2)
        else:
            return i

    def nivel(self,elem):
        resp=-1
        aux= self.raiz()
        aux2= self._buscar(elem)
        if aux2!= None:
            resp=self._nivel(aux,elem,0)
        return resp
    def _nivel(self,nodo:Nodo,elem,i=0):
        if nodo!=None and nodo.obtenerItem()==elem:
            return i
        else:
            if nodo.obtenerItem() < elem:
                aux=self._nivel(nodo.obtenerDer(),elem,i+1)
            else:
                aux=self._nivel(nodo.obtenerIzq(),elem,i+1)
            return aux