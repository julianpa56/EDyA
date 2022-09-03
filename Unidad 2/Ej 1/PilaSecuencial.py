
class Pila:
    __elementos= []
    __apuntador= None
    __tope=None

    def __init__(self) -> None:
        pass

    def vacia(self):
        return (self.__tope == -1)

    def insertar(self,elemento):
        respuesta= False
        if self.__apuntador <= self.__tope:
            self.__elementos[self.__apuntador]=elemento
            self.__apuntador+=1
            respuesta= True
        return respuesta

    def suprimir(self):
        respuesta= False
        if not self.vacia() and self.__apuntador-1 >= 0:
            self.__apuntador-=1
            self.__elementos[self.__apuntador]=None
            respuesta= True
        return respuesta
            

    def mostrar(self):
        if not self.vacia():
            for i in range(self.__tope+1):
                print("Elemento {}: - {}".format(i+1,self.__elementos[i]))

    def Crear(self,cantidad):
        self.__tope=cantidad-1
        self.__elementos=[None]*cantidad
        self.__apuntador=0
                


