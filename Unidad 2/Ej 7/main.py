import random
from TDAColaSecuencial import ColaSecuencial

if __name__=='__main__':
    colaCajero= ColaSecuencial()
    colaCajero.Crear(5)
    reloj=0
    tiempoSimulacion= int(input("Ingrese tiempo maximo de simulacion: "))
    frecuenciaLlegada= int(input("Ingrese frecuencia de llegada de los clientes: "))
    tiempoAtencion= int(input("Ingrese tiempo de atencion del cajero: "))
    tiempoEsperaAcumulado= 0
    clientesAtendidos= 0
    clienteIngresados= 0
    cajero= 0

    while reloj <= tiempoSimulacion:
        if random.random()<= 1/frecuenciaLlegada :
            colaCajero.Insertar(reloj)
            clienteIngresados+=1
        
        if cajero == 0:

            if (not colaCajero.Vacia()):
                cliente= colaCajero.Suprimir()
                tiempoEsperaAcumulado+= reloj - int(cliente)
                clientesAtendidos+=1
                cajero= tiempoAtencion 
        reloj+=1

        if cajero > 0: 
            cajero-=1
    
    tiempoPromedioEspera = tiempoEsperaAcumulado/clientesAtendidos

    print("Clientes atendidos: ",clientesAtendidos)
    print("Tiempo de espera acumulado: ",tiempoEsperaAcumulado)
    print("Tiempo promedio de espera: ", tiempoPromedioEspera)

