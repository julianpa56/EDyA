
from Binario import convertirABinario


if __name__=='__main__':
    decimal=int(input("Ingrese un numero decimal: "))
    print("----- \n El valor binario de {} es: {}".format(decimal,convertirABinario(decimal)))