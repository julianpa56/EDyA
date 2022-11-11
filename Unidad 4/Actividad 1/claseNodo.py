class Nodo(object):

    __item= None
    __nodoIzquierdo= None
    __nodoDerecho= None

    def __init__(self):
        self.__item= None
        self.__nodoIzquierdo= None
        self.__nodoDerecho= None

    def obtenerItem(self):
        return self.__item

    def cargarItem(self,xitem):
        self.__item= xitem

    def cargarIzq(self,punt):
        self.__nodoIzquierdo=punt
        return self.__nodoIzquierdo

    def obtenerIzq(self):
        return self.__nodoIzquierdo
    
    def cargarDer(self,punt):
        self.__nodoDerecho=punt
        return self.__nodoDerecho

    def obtenerDer(self):
        return self.__nodoDerecho

    