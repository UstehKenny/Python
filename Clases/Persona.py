"""#Herencia
class SerVivo:
    tieneVida = True

    def respirar(self):
        print("Estoy respirando")
    def reproducir(self):
        print("Me estoy reproduciendo")



class Persona(SerVivo):
    #Atributos
    altura = 0.0
    genero = ""
    colorCabello = ""
    tatuajes = False
    complexion = ""

    #Constructor
    def __init__(self,altura,genero,colorCabello,tatuajes,complexion):
        print("Se ejecuta este codigo")
        self.altura = altura
        self.genero = genero
        self.colorCabello = colorCabello
        self.tatuajes = tatuajes
        self.complexion = complexion

    #Metodos
    def correr(self):
        print("Estoy corriendo")
    def escribir(self):
        print("Estoy escribiendo")

class Mujer(Persona):
    def multitask(self):
        print("Ejecutando dos tareas a la vez")

Humano1 = Persona(1.70,"M","Cafe",True,"Ectomorfo")
#print(Humano1)

Humano1.altura = 1.70
Humano1.genero = "M"
Humano1.colorCabello = "Cafe"
Humano1.tatuajes = True
Humano1.complexion = "Ectomorfo"


print(Humano1.altura)
print(Humano1.genero)
print(Humano1.colorCabello)
print(Humano1.correr())
print(Humano1.tieneVida)
print(Humano1.respirar())
print(Humano1.reproducir())

Mujer1 = Mujer(1.70,"M","Cafe",True,"Ectomorfo")
print(Mujer1.tieneVida)

#Polimorfismo

class Gato:
    def rugir(self):
        print("El gato maulla")
class Perro:
    def rugir(self):
        print("El perro ladra")

def rugir(animal):
    animal.rugir()

perro = Perro()
gato = Gato()
rugir(perro)
rugir(gato)
"""
#Encapsulamiento
class Ejemplo:
    def __init__(self):
        self.publico = "variable publica"
        self.__privado = "variable privada"
    def getVariable(self):
        print(self.__privado)

ejemplo = Ejemplo()
#print(ejemplo.publico)
print(ejemplo.getVariable)