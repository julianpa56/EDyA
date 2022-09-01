from TDAColaSecuencial import ColaSecuencial


if __name__=='__main__':
    nuevaCola= ColaSecuencial()
    nuevaCola.Crear()
    if nuevaCola.Vacia():
        print("Cola vacia")
    else: 
        print("Cola posee elementos")
    nuevaCola.Insertar("Elemento 1")
    nuevaCola.Insertar("Elemento 2")
    nuevaCola.Insertar("Elemento 3")
    nuevaCola.Insertar("Elemento 4")
    nuevaCola.Recorrer()
    if nuevaCola.Vacia():
        print("Cola vacia")
    else: 
        print("Cola posee elementos")
    nuevaCola.Suprimir()
    nuevaCola.Suprimir()
    nuevaCola.Recorrer()
