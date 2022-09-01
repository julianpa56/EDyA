


class ColaSecuencial:
    __cola= []


    def __init__(self) -> None:
        pass

    def Crear(self):
        self.__cola=[]
    
    def Vacia(self):
        respuesta= False
        if len(self.__cola)==0:
            respuesta= True
        return respuesta
    
    def Insertar(self,elemento):
        self.__cola.append(elemento)
    
    def Suprimir(self):
        respuesta= -1
        if not self.Vacia():
            respuesta= self.__cola.pop(0)
        return respuesta

    def Recorrer(self):
        i=1
        for elemento in self.__cola:
            print("Posicion en la fila: ",i," - Elemento: ", elemento)
            i+=1
            