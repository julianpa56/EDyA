import numpy as np
from tkinter import *

class Reina():
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y


class Tablero(Tk):
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.tab= np.full((n,n),0)
        self.geometry("{}x{}".format(80*n,80*n))
        self.tablero= Canvas(self)
        self.tablero.pack(fill="both",expand=1)
    def cuadrado(self):
        for i in range(n):
            for j in range(n):
                if(i+j)%2==0:
                    self.tablero.create_rectangle(i*80,j*80,(i+1)*80,(j+1)*80,fill="brown")
                else:
                    self.tablero.create_rectangle(i*80,j*80,(i+1)*80,(j+1)*80,fill="orange")
    def dibujarReinas(self):
        for i in range(n):
            for j in range(n):
                if self.tab[j][i]==1:
                    self.tablero.create_oval(i*80+20,j*80+20,(i+1)*80-20,(j+1)*80-20,fill="white")
    def colocarReina(self,reinas,x,y):
        if x<=n and y<=n: # PREGUNTA SI LAS COORDENADAS ESTAN DENTRO DEL TABLERO DE ORDEN NxN
            nuevaReina= Reina(x,y)
            if self.verificarReina(reinas,nuevaReina): # SI NO HAY COLISION AGREGA LA REINA EN LA TABLA Y EN LA LISTA DE REINAS
                reinas.append(nuevaReina)
                self.tab[x-1][y-1]=1
            else:
                print("Colision de reinas")
        else:
            print("Error - coordenadas erroneas")

    def verificarReina(self,reinas,aux):
        resp=True
        b=True
        i=len(reinas)-1
        while b and i>-1:
            if (aux.getX()!= reinas[i].getX())and(aux.getY()!= reinas[i].getY()): # VERIFICA QUE NO ESTEN EN LA MISMA FILA O COLUMNA
                if abs(aux.getX()+aux.getY())!= abs(reinas[i].getX()+reinas[i].getY()): # VERIFICA QUE NO ESTEN EN LA MISMA DIAGONAL POSITIVA
                    if abs(aux.getX()-aux.getY())!= abs(reinas[i].getX()-reinas[i].getY()): # VERIFICA QUE NO ESTEN EN LA MISMA DIAGONAL NEGATIVA
                        i-=1
                    else:
                        b=False
                else:
                    b=False
            else:
                b=False
        if not b:
            resp=False
        return resp   



if __name__=='__main__':
    n=6 # ORDEN DEL TABLERO NxN
    reinas=[]
    app=Tablero()

    app.colocarReina(reinas,1,1)
    app.colocarReina(reinas,4,3)
    app.colocarReina(reinas,2,6)
    app.cuadrado()
    app.dibujarReinas()
    app.mainloop()