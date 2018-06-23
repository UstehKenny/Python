#Menu principal: Pide al usuario seleccionar una opcion y dependiendo de esta, va a llevar a dos funciones
def Menu():
    print("1) Registrarse")
    print("2) Ingresar")
    print("3) Salir ")
    x = int(input("Que desea hacer?"))
    dicc = {}

    if x == 1:
        print("Registro")
        dicc = Registro()
        print(dicc)
    elif x == 2:
        
        print("Login")
        Login(dicc)
    else: 
        print("Hasta luego")

#Funcion de Login
def Login(dicc):
    #Se pide usuario 
    # y contrasenia
    user = input("Usuario: ")
    passw = input("Contrasenia: ")
    print("Login: ",dicc)
    #Si el usuario esta en el diccionario, comparara posteriormente la contrasenia para ver si son correctos
    if user in dicc:
        if  dicc[user[0]] == passw: #Si el usuario y contrasenia son correctos, dejara entrar al usuario
            print("Bienvenido")
        else:
            print("Contrasenia incorrecta") #Si el usuario es correcto pero la contrasenia es incorrecta, no dejara loggearse
    else: #Si el usuario no coincide en el diccionario, imprimira lo siguiente:
        print("Usuario no registrado")

def Registro():
        usuarios = {} #Creamos un diccionario en donde, como llave, guardara el nombre del usuario y ,como valor, guardara la informacion del usuario que se pedira a continuacion
        listaUsuarios = [] #Creamos la lista en donde se van a guardar los datos del usuario
        username = input("Nombre de usuario: ") #Se pide el nombre de usuario
        password = input("Contrasenia: ") #Se pide una contrasenia
        listaUsuarios.append(password)
        usuarios[username] = listaUsuarios #Aqui definimos la llave y el valor del diccionario de usuarios
        nombre = input("Ingresa nombre: ")
        listaUsuarios.append(nombre)
        apellido = input("Ingresa apellido: ")
        listaUsuarios.append(apellido)
        edad = input("Ingresa edad: ")
        listaUsuarios.append(edad)
        numTarj = input("Ingresa numero de tarjeta: ")
        listaUsuarios.append(numTarj)
        pp = []
        paypalCorreo = input("Ingresa correo de PayPal: ")
        pp.append(paypalCorreo)
        paypalContrasenia = input("Ingresa contrasenia de PayPal")
        pp.append(paypalContrasenia)

        listaUsuarios = listaUsuarios.append(pp)
        usuarios[username] = listaUsuarios

        respuesta = input("Deseas hacer otro registro? s/n ")
        if respuesta == 'n':
            Menu()
        elif respuesta == 's':
            Registro()
        else:
            print("Opcion invalida")
        return usuarios


Menu()