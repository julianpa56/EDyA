

import os
from claseTablaHash import TablaHash





if __name__=='__main__':
    os.system("cls")
    tabla= TablaHash(10)

    tabla.insertar(5)
    tabla.insertar(15)
    tabla.insertar(6)
    tabla.insertar(16)
    tabla.insertar(8)
    tabla.insertar(9)
    tabla.insertar(10)
    tabla.insertar(2)
    tabla.insertar(3)
    tabla.insertar(1)

    print(tabla.getElementos())
    tabla.buscar(16)









