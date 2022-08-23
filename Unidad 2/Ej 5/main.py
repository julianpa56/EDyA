from claseTorre import Torre
import os


if __name__=='__main__':
    nroDiscos=int(input("Ingrese la cantidad de discos que desea utilizar: "))
    nuevaTorre=Torre(nroDiscos)
    nroJugadas=0
    os.system("cls")
    b= True
    while b:
        nuevaTorre.mostrarEstado()
        print("________________________________")
        desde=int(input("--- INGRESE TORRE PARA SACAR UN DISCO (1 - 2 - 3)"))
        hacia=int(input("--- INGRESE TORRE PARA PONER UN DISCO (1 - 2 - 3)"))
        if (desde == 1 or desde == 2 or desde == 3) and (hacia == 1 or hacia == 2 or hacia == 3):
            desde-=1
            hacia-=1
            print(nuevaTorre.moverDisco(desde,hacia))
            nuevaTorre.mostrarEstado()
            nroJugadas+=1
        else:
            print("ALGUNA OPCION INGRESADA ES INCORRECTA")
        
        op=int(input("DESEA REALIZAR OTRO MOVIMIENTO? 1 - SI | 2 - NO"))
        if op==2:
            b=False
        os.system("cls")

    print("Numero de jugadas: ",nroJugadas)
    print("Numero minimo de jugadas: ",(2**nroDiscos-1))




