


def obtenerFactorial(numero):

    listaAnteriores=[]
    for i in range(1,numero):
        listaAnteriores.append(i)

    for j in range(len(listaAnteriores)):
        numero*= listaAnteriores.pop()

    return numero