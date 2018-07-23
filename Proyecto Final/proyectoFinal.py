import getpass
#Dos tipos de usuarios: Compradores y Vendedores
#Se usaran diccionarios para guardar la informacion de los usuarios y las listas son el valor de cada uno de los diccionarios
compradores = {}
vendedores = {}
listaCompradores = []
listaVendedores = []
#Diccionarios de los articulos 
#Se declaran de manera global para poder acceder a la informacion
articulos = {}
listaArticulos = []

def validarContrasenia(passw):
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
                            return True
                        else:
                            return False
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

def validarUsuario(bname):
    if len(bname) >= 8:
        print("Es mayor a 8")
        if bname.isupper() == False:
            print("Tiene mayusculas")
            if bname.islower() == False:
                print("Tiene minusculas")
                if bname.isdigit() == False:
                    print("Tiene numero")
                    if bname.isspace() == False:
                        return True
                    else:
                        return False
                else:
                    print("Contrasenia invalida")
            else:
                print("Contrasenia invalida")
        else:
            print("Contrasenia invalida")
    else:
        print("Usuario menor a 6 caracteres")

#Ambos usuarios tendran la opcion de registrarse e ingresar
def Ingresar():
    print("Ingresar")
    print("Login: ")
    #Especificar que tipo de perfil va a ingresar 
    wahl = input("Ingresar como: \n + Vendedor (v)\n + Comprador (c)\n Ingrese la opcion:")
    if wahl=='v' or wahl=='V' or wahl=='c' or wahl=='C':
        user = input("Usuario: ")
        passw = getpass.getpass("Contrasenia: ")
        #Conprobamos que el usuario se encuentre en el diccionario
        if wahl=='v' or wahl=='V':
            if user in vendedores:
                if vendedores[user][0] == passw:
                    print("Bienvenido..."+user)
                else:
                    print("Contrasenia incorrecta ")
            else:
                print("Usuario no registrado")
        elif wahl=='c' or wahl=='C':
            if user in compradores:
                if compradores[user][0] == passw:
                    print("Bienvenido..."+user)
                else:
                    print("Contrasenia incorrecta ")
            else:
                print("Usuario no registrado ")
        else:
            print("Opcion invalida")
    else:
        print("Opcion invalida")

def Registrar():
    print("Registro")
    #Especificar que tipo de usuario va a registrar 
    wahl = input("Registrarse como: \n + Vendedor (v)\n + Comprador (c)\n + Ambos (a)\n Ingrese la opcion: ")
    #Comprobar que la opcion que ingrese el usuario sea la correcta para continuar con el registro
    if wahl=='v' or wahl=='V' or wahl=='c' or wahl=='C' or wahl=='a' or wahl=='A':

        bname = input("Nombre de usuario: ") #Se pide el nombre de usuario. Llave del diccionario

        passwort = getpass.getpass("Contrasenia: ") #0
        validarContrasenia(passwort)
        nombre = input("Ingresa nombre: ") #1
        apellido = input("Ingresa apellido: ") #2
        edad = input("Ingresa edad: ") #3
        numTarj = input("Ingresa numero de tarjeta: ") #4
        pp = [] #5
        paypalCorreo = input("Ingresa correo de PayPal: ") #5.0
        pp.append(paypalCorreo)
        paypalContrasenia = getpass.getpass("Ingresa contrasenia de PayPal") #5.1
        pp.append(paypalContrasenia)

        if wahl=='v' or wahl=='V':
            #Vendedores
            listaVendedores.append(passwort) #0
            listaVendedores.append(nombre) #1
            listaVendedores.append(apellido) #2
            listaVendedores.append(edad) #3
            listaVendedores.append(numTarj) #4
            listaVendedores.append(pp) #5
            vendedores[bname] = listaVendedores
        elif wahl=='c' or wahl=='C':
            #Compradores
            listaCompradores.append(passwort) #0
            listaCompradores.append(nombre) #1
            listaCompradores.append(apellido) #2
            listaCompradores.append(edad) #3
            listaCompradores.append(numTarj) #4
            listaCompradores.append(pp) #5
            compradores[bname] = listaCompradores
        elif wahl=='a' or wahl=='A':
            #Vendedores
            listaVendedores.append(passwort) #0
            listaVendedores.append(nombre) #1
            listaVendedores.append(apellido) #2
            listaVendedores.append(edad) #3
            listaVendedores.append(numTarj) #4
            listaVendedores.append(pp) #5
            vendedores[bname] = listaVendedores
            #Compradores
            listaCompradores.append(passwort) #0
            listaCompradores.append(nombre) #1
            listaCompradores.append(apellido) #2
            listaCompradores.append(edad) #3
            listaCompradores.append(numTarj) #4
            listaCompradores.append(pp) #5
            compradores[bname] = listaCompradores
        else:
            print("Opcion invalida")
    else:
        print("Opcion invalida")

def subirArticulo():
    print("Vendedor\n Subir Articulos:")
    nombreArticulo = input("Nombre del articulo: ")
    descrip = input("Descripcion del articulo: ")
    precio = float(input("Precio del articulo: "))
    numInventario = int(float(input("Disponibles en el inventario: ")))

    listaArticulos.append(descrip) #0
    listaArticulos.append(precio) #1
    listaArticulos.append(numInventario) #2

    articulos[nombreArticulo] = listaArticulos

    print("Operacion aceptada")

def comprarArticulo():
    print("Articulos: ")
        




    """
  


    """