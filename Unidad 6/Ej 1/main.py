import os

from claseGrafo import Grafo




if __name__=='__main__':
    os.system("cls")
    grafo= Grafo(['A','B','C','D'])
    grafo.NuevaArista('A','B')
    grafo.NuevaArista('B','C')
    grafo.NuevaArista('C','D')
    grafo.Mostrar()
    print("-------")
    print(grafo.Aciclico2())
