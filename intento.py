import datetime

class Sistema:
    def __init__(self):
      self.__lista_pacientes = {}

    def VerficarExiste(self,Cedula):
        return Cedula in self.__lista_pacientes
    
    def ingresarPaciente(self, paciente):
            self.__lista_pacientes[paciente.verCedula()] = paciente
            return True

    def EliminarPaciente(self,Cedula):
        del  self.__lista_pacientes[Cedula]

    def RecuperarPaciente(self,Cedula):
            paciente_encontrado = self.__lista_pacientes[Cedula]
            print("Nombre: " + paciente_encontrado.verNombre())
            print("Cedula: " + str(paciente_encontrado.verCedula()))
            print("Genero: " + paciente_encontrado.verGenero())
            print("Servicio: " + paciente_encontrado.verVisitas())

class Persona:

    def __init__(self):
      self.__nombre = ""
      self.__cedula = 0
      self.__genero = ""
      self.__Visitas = {}
      
    def verNombre(self):
        return self.__nombre
    def verVisitas(self):
        return self.__Visitas
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarVisitas(self,s):
        self.__Visitas = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Visita:

    def __init__(self):
        self.__fecha = ""
        self.__registro = ""
        self.__notas = ""
        self.__indices = {}
    
    def verFecha(self):
        return self.__fecha
    def verRegistro(self):
        return self.__registro
    def verNotas(self):
        return self.__notas
    def verIndice(self):
        return self.__indices
    
    def asignarFecha(self,f):
        self.__fecha = f
    def asignarRegistro(self,r):
        self.__registro = r
    def asignarNotas(self,o):
        self.__notas = o
    def asignarIndice(self,i):
        self.__indices = i

"""
class Indices:
"""

def main():
    MiSitema = Sistema()
    while True:
        opcion = int(input("1. Nuevo paciente\n - 2. Editar paciente\n - 3. Eliminar paciente\n - 4. Cargar pacientes en la base de datos:  \n - 5. Salir:  \n"))
        if opcion == 1:
                print("Hola")

        elif opcion == 5:
                break

if __name__ == "__main__":
    main()
