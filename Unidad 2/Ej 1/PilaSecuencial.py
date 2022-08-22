
class Pila:
    __elementos= []
    __apuntador= None
    __tope=None
    __cantidad=0

    def __init__(self) -> None:
        self.__elementos=[]
        self.__apuntador=0
        self.__tope=0
        self.__cantidad=0

    def vacia(self):
        return self.__tope == 0

    def insertar(self,elemento):
        self.__elementos.append(elemento)
        self.__tope+=1
        self.__cantidad+=1
        self.__apuntador=elemento

    def suprimir(self):
        x=0
        if self.__cantidad>0:
            x = self.__elementos.pop()
            self.__cantidad-=1
            self.__tope-=1
            if self.__cantidad>0:
                self.__apuntador=self.__elementos[-1]
            else:
                self.__apuntador=None
        return x

    def mostrar(self):
        if not self.vacia():
            for i in range(self.__cantidad):
                print(self.suprimir())
                


