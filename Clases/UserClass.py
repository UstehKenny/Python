class UserClass:
    #Atributos
    contrasenia = ""
    nombre = ""
    apellido = ""
    edad = ""
    tarjeta = ""
    correoPP = ""
    contraseniaPP = ""

    #Constructor
    def __init__(self,contrasenia,nombre,apellido,edad,tarjeta,correoPP,contraseniaPP):
        self.contrasenia = contrasenia
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.tarjeta = tarjeta
        self.correoPP = correoPP
        self.contraseniaPP = contraseniaPP
    
def Registro(self):
    contrasenia = input("Contrasenia ")
    nombre = input("Nombre ")
    apellido = input("Apellido ")
    edad = input("Edad ")
    tarjeta = input("Tarjeta ")
    correoPP = input("CorreoPP")
    contraseniaPP = input("ContraseniaPP")
    
    return contrasenia,nombre,apellido,edad,tarjeta,correoPP,contraseniaPP

nuevoUsuario = UserClass()
print(nuevoUsuario.contrasenia)
