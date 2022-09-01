import random
from TDAColaSecuencial import ColaSecuencial

if __name__=='__main__':
    colaCajero= ColaSecuencial()
    estadoCajero= True
    cantidadAtendidos= 0
    tiempoAcumulado=0
    i=1
    aux=0

    cantidadClientes=0

    frecuenciaLlegada= int(input("Ingrese frecuencia de llegada de los clientes: "))
    tiempoAtencion= int(input("Ingrese tiempo de atencion del cajero: "))
    tiempoSimulacion= int(input("Ingrese tiempo maximo de simulacion: "))
    reloj=0

    tiempoAt=0

    while reloj <= tiempoSimulacion:
        if random.randint(0,1)==1:
            colaCajero.Insertar(i)
            cantidadClientes+=1
            i+=1
        
        if estadoCajero:
            
            if not colaCajero.Vacia():
                colaCajero.Suprimir()
                aux+=1
                tiempoAcumulado+= (aux + tiempoAt)
                tiempoAt= tiempoAtencion
                cantidadAtendidos+=1
                estadoCajero= False
        else:
            estadoCajero= True
        reloj+=frecuenciaLlegada
    tiempoPromedio= tiempoAcumulado // cantidadAtendidos

    print("Cantidad de clientes que llegaron: ",cantidadClientes)
    print("Cantidad de clientes atendidos: ",cantidadAtendidos)
    print("Tiempo total acumulado: ",tiempoAcumulado)
    print("Tiempo promedio de espera: ", round(tiempoPromedio,ndigits=1), " min")

