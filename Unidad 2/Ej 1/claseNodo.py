

class Nodo:
    __datos=None
    __siguiente=None

    def __init__(self,datos) -> None:
        self.__datos=datos
        self.__siguiente=None

    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente
    
    def getSiguiente(self):
        return self.__siguiente

    def getDatos(self):
        return self.__datos