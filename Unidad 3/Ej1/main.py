
from TDALista import ListaSecuencial


if __name__=='__main__':
    lista= ListaSecuencial()
    lista.Crear(5)
    lista.mostrar()
    lista.Insertar(3,1)
    lista.Insertar(3,2)
    lista.Insertar(4,2)
    lista.mostrar()

