from PilaSecuencial import Pila



if __name__=='__main__':
    nuevaPila= Pila()
    nuevaPila.Crear(10)
    print("--- Creacion de la pila con cantidad 10")
    nuevaPila.mostrar()
    nuevaPila.insertar('hola')
    nuevaPila.insertar('hola2')
    nuevaPila.insertar(3)
    nuevaPila.insertar(4)
    nuevaPila.insertar('hola5')
    print("--- Insercion de 5 elementos a la pila")
    nuevaPila.mostrar()
    nuevaPila.suprimir()
    nuevaPila.suprimir()
    print("--- Suprecion de 2 elementos de la pila")
    nuevaPila.mostrar()