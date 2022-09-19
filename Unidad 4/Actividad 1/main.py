
import os
from claseArbolBinario import ArbolBinario



if __name__=='__main__':
    arbol= ArbolBinario()
    os.system('cls')
    arbol.insertar(70)
    arbol.insertar(92)
    arbol.insertar(83)
    arbol.insertar(79)
    arbol.insertar(100)
    arbol.insertar(47)
    arbol.insertar(35)
    arbol.insertar(68)
    arbol.inOrden()