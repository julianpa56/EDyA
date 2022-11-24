from pilaSecuencial import Pila


if __name__=='__main__':
    pila=Pila()
    pila.Crear(5)

    expresion='{[(A-B]*C)+D}'
    i=0
    rango= len(expresion)
    error= False


    while i < rango and not error: 
        X= expresion[i]
        if X == '{' or X == '[' or X == '(':
            pila.insertar(X)
        
        if X == '}' or X == ']' or X == ')': 
            aux= pila.suprimir() 
            print("Aux: ",aux," - X: ",X)

            if not error:
                
                if (X == '}' and aux != '{') or (X == ']' and aux != '[') or (X == ')' and aux != '('):
                    print("Error")
                    error = True
        
        i+=1

    if not pila.vacia() or error:
        print ("Error de correspondencia")
    else:
        print("Correspondencia ")