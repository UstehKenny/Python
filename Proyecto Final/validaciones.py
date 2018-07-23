"""
Codigo para pruebas
import getpass
passw = input("Ingresa la contrasenia: ")
if len(passw) >= 8:
    print("Es mayor a 8")
    if passw.isupper() == False:
        print("Tiene mayusculas")
        if passw.islower() == False:
            print("Tiene minusculas")
            if passw.isdigit() == False:
                print("Tiene numero")
                if passw.isalnum() == False:
                    print("Tiene un caracter")
                    if passw.isspace() == False:
                        print("No tiene espacios\nCONTRASENIA VALIDA")
                    else:
                        print("Tiene espacios\nCONTRASENIA INVALIDA")
                else:
                    print("No tiene caracteres")
            else:
                print("No tiene numero")
        else:
            print("No tiene minusculas")
    else:
        print("No tiene mayusculas")
else:
    print("Menor a 8")

"""
usuarios = {}
unaLista = []
        
for loquesea in range(3):
    username = input("Nombre de usuario: ") #Se pide el nombre de usuario
    password = input("Contrasenia: ") #Se pide una contrasenia
    unaLista.append(password) #0
    nombre = input("Ingresa nombre: ")
    unaLista.append(nombre) #1
        
    apellido = input("Ingresa apellido: ")
    unaLista.append(apellido) #2
       
    edad = input("Ingresa edad: ")
    unaLista.append(edad) #3
    """       
    numTarj = input("Ingresa numero de tarjeta: ")
    unaLista.append(numTarj) #4
        
    pp = []
    paypalCorreo = input("Ingresa correo de PayPal: ")
    pp.append(paypalCorreo) #5.0
    paypalContrasenia = input("Ingresa contrasenia de PayPal")
    pp.append(paypalContrasenia) #5.1

    unaLista.append(pp) #5 """
    usuarios[username] = unaLista

#articulo = input(" askk")
#print(usuarios[articulo])

for elemento in usuarios:
    print(elemento) #Llave
    print(usuarios[elemento][0]) #Valor de la lista en la posicion 0