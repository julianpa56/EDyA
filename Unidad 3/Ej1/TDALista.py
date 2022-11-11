


class ListaSecuencial:
    __lista= []
    __tamanio= 0
    __ultimo= 0

    def __init__(self) -> None:
        self.__lista=[]
        self.__ultimo=0

    def Insertar(self,elemento,pos):
        if pos-1== self.__ultimo and self.__ultimo==0:
            self.__lista[0]=elemento
            self.__ultimo+=1
        elif pos-1 == self.__ultimo:
            self.__lista[pos-1]=elemento
            self.__ultimo+=1  
        elif pos-1>=0 and pos-1 <= self.__ultimo-1:
            actual=self.__lista[pos-1]
            siguiente= self.Siguiente(pos-1)
            
            
    def Suprimir(self,pos):
        respuesta= False
        if pos-1 <= self.__ultimo and pos-1 > -1:
            while pos-1 < self.__ultimo:
                self.__lista[pos-1]=self.__lista[pos]
                pos+=1
            self.__ultimo-=1
            respuesta= True
        return respuesta

    def Recuperar(self,L,p):
        pass

    def Buscar(self,X,L):
        pass

    def Primer_elemento(self):
        respuesta=-1
        if not self.Vacia():
            respuesta=self.__lista[0]
        return respuesta

    def Ultimo_elemento(self):
        respuesta=-1
        if self.__ultimo> -1:
            respuesta= self.__lista[self.__ultimo]
        return respuesta

    def Siguiente(self,pos):
        respuesta=-1
        if pos-1 < self.__ultimo+1:
            respuesta= self.__lista[pos]
        return respuesta

    def Anterior(self,pos):
        respuesta=-1
        if pos-1 <= self.__ultimo and pos-1 > 0:
            respuesta= self.__lista[pos-2]
        return respuesta

    def Recorrer(self,L):
        pass

    def Crear(self,lon):
        self.__lista=[None]*int(lon)
        self.__ultimo=0

    def Vacia(self):
        return (self.__lista[0] == None)

    def mostrar(self):
        print(self.__lista)
