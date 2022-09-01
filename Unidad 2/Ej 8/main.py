import random

from clasePaciente import Paciente
from TDAColaSecuencial import ColaSecuencial


if __name__=='__main__':
    colaHospital= ColaSecuencial()
    dispEsp=[0,0,0,0]
    dispMedico=[True,True,True,True]
    especialidades=["Ginecologia","Clinica medica","Oftalmologia","Pediatria"]

    cantidadAtendidos= 0
    tiempoAcumulado=0
    cantidadPacientes=0
    noAtendidos=0

    frecuenciaLlegada= 1
    tiempoAtencion= 20
    tiempoSimulacion= 240
    reloj=0

    i=1
    atencion=None

    while reloj <= tiempoSimulacion:
        atencion=random.randint(0,1)
        if atencion==1 : 
            if reloj <= 60: # Si no supera el horario de 7 a 8
                aux=random.randint(1,4)
                esp=''
                if aux==1:
                    esp=especialidades[aux-1]
                elif aux==2:
                    esp=especialidades[aux-1]
                elif aux==3:
                    esp=especialidades[aux-1]
                else:
                    esp=especialidades[aux-1]
                
                if dispEsp[aux-1]<10: # Si quedan turnos disponibles
                    dispEsp[aux-1]+=1
                    nuevoPaciente= Paciente("Paciente {}".format(i),random.randint(20000000,40000000),esp)
                    colaHospital.Insertar(nuevoPaciente)
                    if dispMedico[aux-1]: # Si el medico esta libre
                        if not colaHospital.Vacia():
                            colaHospital.Suprimir()
                            dispMedico[aux-1]= False
                    else: # Si el medico esta ocupado
                        dispMedico[aux-1]= True
                else: # Si no quedan turnos
                    noAtendidos+=1
            else: # Si supera el horario de las 8
                noAtendidos+=1
            i+=1
        
        
        reloj+=frecuenciaLlegada

    for i in range(4):
        tiempoAcumulado=0
        tiempoPromedio=0
        adicional=1
        tiempoAt=0
        for j in range(dispEsp[i]):
            tiempoAcumulado+= (adicional + tiempoAt)
            tiempoAt=tiempoAtencion
            adicional+=1
        print("Especialidad: ",especialidades[i])
        print("Cantidad de atendidos: ",dispEsp[i])
        print("Tiempo acumulado: ",tiempoAcumulado)
        tiempoPromedio= tiempoAcumulado // dispEsp[i]
        print("Tiempo promedio de atencion: ",round(tiempoPromedio,ndigits=1)," min")
    print("---------------------------------------------")
    print("Cantidad de personas no atendidas: ",noAtendidos)
