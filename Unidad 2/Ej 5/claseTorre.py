

class Torre:
    __torres=[[],[],[]]
    __nroDiscos=0
    
    def __init__(self,nroDiscos) -> None:
        self.__torres[0]= ['|']*(int(nroDiscos))
        self.__torres[1]= ['|']*(int(nroDiscos))
        self.__torres[2]= ['|']*(int(nroDiscos))
        self.__nroDiscos=nroDiscos

        for i in range(nroDiscos-1,-1,-1):
            self.__torres[0][nroDiscos-1-i]=i+1

    def mostrarEstado(self):
        print("T1 --- T2 --- T3")
        for i in range(self.__nroDiscos-1,-1,-1):
            print("{}.....{}.....{}".format(self.__torres[0][i],self.__torres[1][i],self.__torres[2][i]))

    def moverDisco(self,desde,hacia):
        respuesta=""
        if str(self.__torres[desde][0])!= '|':
            if str(self.__torres[hacia][self.__nroDiscos-1])=='|':
                i=self.buscarDisco(desde)
                j=self.buscarDisco(hacia)
                if j==-1:
                    self.__torres[hacia][0]=self.__torres[desde][i]
                    self.__torres[desde][i]='|'
                    respuesta= "Movimiento realizado con exito"
                else:
                    if self.__torres[desde][i]< self.__torres[hacia][j]:
                        self.__torres[hacia][j+1]=self.__torres[desde][i]
                        self.__torres[desde][i]='|'
                        respuesta= "Movimiento realizado con exito"
                    else:
                        respuesta= "El ultimo disco de la torre {} es menor que el disco que se desea mover de la torre {}".format(hacia+1,desde+1)
            else: 
                respuesta="La torre {} esta llena".format(hacia+1)
            
        else:
            respuesta=("No es posible realizar el movimiento porque la torre {} esta vacia".format(desde+1))
        
        return respuesta

    def buscarDisco(self,torre):
        indice=self.__nroDiscos-1
        b= True
        while indice >= 0 and b:
            if str(self.__torres[torre][indice]) == '|':
                indice-=1
            else:
                b= False
        print('------------',indice)
        return indice

