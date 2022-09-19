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
        elif (arbol.obtenerItem() < aux.obtenerItem()):
            # print('A: ',arbol.obtenerItem(),' - B: ',aux.obtenerItem())
            if arbol.obtenerIzq()==None:
                arbol.cargarIzq(aux)
            else:
                self._insertar(arbol.obtenerIzq(),aux)

        elif (arbol.obtenerItem() > aux.obtenerItem()):
            # print('A: ',arbol.obtenerItem(),' - B: ',aux.obtenerItem())
            if arbol.obtenerDer()==None:
                arbol.cargarDer(aux)
            else:
                self._insertar(arbol.obtenerDer(),aux)
        else:
            print("Error en la insercion")
            return None

    def _buscar(self,item):
        aux= self.raiz()

        while aux != None and aux.obtenerItem() != item:
            if aux.obtenerItem() < item:
                aux= aux.obtenerIzq()
            else:
                aux= aux.obtenerDer()
        return aux

    def hijo(self,hijo,padre):
        respuesta= False
        aux= self._buscar(padre)
        if aux == None:
            print("Error - Padre no encontrado")
            respuesta= False
        elif aux.obtenerDer() != None and aux.obtenerDer().obtenerItem() == hijo:
            respuesta= True
        elif aux.obtenerIzq() != None and aux.obtenerIzq().obtenerItem() == hijo:
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
            print()
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
