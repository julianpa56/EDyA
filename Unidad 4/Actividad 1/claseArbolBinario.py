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

    def hijo(self,hijo,padre):
        respuesta= False
        aux= self.raiz()
        while aux != None and aux.obtenerItem() != padre:
            if aux.obtenerItem() < padre:
                aux= aux.obtenerIzq()
            else:
                aux= aux.obtenerDer()
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

    def _buscar(self,item):
        aux= self.raiz()

        while aux != None and aux.obtenerItem() != item:
            if aux.obtenerItem() < item:
                aux= aux.obtenerIzq()
            else:
                aux= aux.obtenerDer()
        return aux


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
