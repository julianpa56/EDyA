


class Paciente:
    __nombre=''
    __dni=0
    __especialidad=''

    def __init__(self,nom,dni,esp):
        self.__nombre=nom
        self.__dni=dni
        self.__especialidad=esp

    def __str__(self) -> str:
        return ("Nombre: ",self.__nombre," DNI: ",self.__dni," Especialidad: ",self.__especialidad)