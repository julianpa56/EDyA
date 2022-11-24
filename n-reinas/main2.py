import numpy as np
import os 


def f():
    global solu
    solu=None
    global confli
    confli=100

def RyP(reinas:list,a=0,cont=0):
    global confli
    global solu
    if a < len(reinas):
        for i in range(len(reinas)):
            if verificar(reinas,a,i):
                reinas[a]=i
                RyP(reinas,a+1,cont)
            else:
                cont+=1
    else:
        print("\n\nTiene solucion",reinas,)
        print("Cantidad de conflictos anteriores: ",cont)
        tablero=np.full((n,n),'-')
        for i in range(n):
            tablero[i][reinas[i]]='R'
        print("\n",tablero)
        if cont < confli:
            confli=cont
            solu=tablero

def verificar(reinas,fil,col):
    resp=True
    b=True
    i=fil-1
    while b and i>=0:
        if reinas[i]!= col:
            if (i+reinas[i]) != (fil+col):
                if (i-reinas[i]) != (fil-col):
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
    os.system("cls")
    f()
    n=4 # ORDEN DEL TABLERO NxN
    reinas=np.full(n,-1)
    RyP(reinas)
    print("\n-------------------\nMejor solucion: \n",solu)
    print("Cantidad de conflictos anteriores: ", confli)
