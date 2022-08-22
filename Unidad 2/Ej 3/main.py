from Factorial import obtenerFactorial


if __name__=='__main__':
    numero=int(input("Ingrese un numero entero positivo para obtener su factorial: "))
    print("----------------------")
    print("El factorial de {} es: {}".format(numero,obtenerFactorial(numero)))