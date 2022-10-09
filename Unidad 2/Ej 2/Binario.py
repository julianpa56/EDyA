from pila import Pila


def convertirABinario(numero):
    
    pilaBinaria= Pila()
    pilaBinaria.Crear()

    while numero != 0:
        modulo= numero % 2
        cociente= numero // 2
        pilaBinaria.Insertar(modulo)
        numero= cociente
        print("Cociente : {} - modulo: {}".format(cociente,modulo))
    
    binario=''
    while not pilaBinaria.Vacia():
        binario+= str(pilaBinaria.Suprimir())
    return binario
