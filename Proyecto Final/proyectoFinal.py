# -*- coding: UTF-8 -*-
import getpass

#Modulos que nos van a permitir enviar correos
import smtplib, getpass, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64

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


def menuInicio():
    print("Bienvenido: ")
    print("1) Registrarse")
    print("2) Ingresar")
    print("3) Salir ")
    x = int(input("Que desea hacer?"))

    if x == 1:
        print("Registrarse")
        Registrar()
    elif x == 2:       
        print("Ingresar")
        Ingresar()
    else: 
        print("Hasta luego")  

def menuVendedor():
    print("**Tienda de ropa**")
    x = input("Subir articulo? s/n \n m-> salir")
    if x=='s' or x=='S':
        subirArticulo()
    elif x=='n' or x=='N':
        menuVendedor()
    elif x=='m' or x=='M':
        menuInicio()


def enviarCorreo(nombre_Articulo):
    #Autenticacion
    user = ("lolusuariouno@gmail.com")
    password = ("notengoContrasenia12")
    #Datos del correo
    remitente = user
    destinatario = input("Ingrese su correo para confirmar su compra: ")
    asunto = ("Compra en linea de ropa")
    mensaje = ("Articulo comprado: "+nombre_Articulo+"\nDescripcion: "+articulos[nombre_Articulo][0]+"\nPrecio: "articulos[nombre_Articulo][1])
    #archivo = input("Adjuntar archivo: ")
    #Protocolo y puerto
    gmail = smtplib.SMTP("smtp.gmail.com",587)
    #Certificado de seguridad
    gmail.starttls()
    #Ingresar
    gmail.login(user,password)
    gmail.set_debuglevel(1)
    #Ingresamos pero falta llenar la informacion
    header["Subject"]=asunto
    header["From"]=remitente
    header["To"]=destinatario
    #Convertimos a HTML
    mensaje = MIMEText(mensaje,"html")
    header.attach(mensaje)
    #Comprobar que el archivo exista
    #Comprobando que el archivo exista
    if(os.path.isfile(archivo)):
	    adjunto = MIMEBase("application","octet-stream")
	    adjunto.set_payload(open(archivo,"rb").read())
	    encode_base64(adjunto)
	    adjunto.add_header('Content-Disposition', 'attachment; filename="%s"'%os.path.basename(archivo))
	    header.attach(adjunto)

    #Enviar email
    gmail.sendmail(remitente,destinatario,header.as_string())
    #Cerrar sesion
    gmail.quit()


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
                            print("Intente de nuevo")
                            Registrar()
                    else:
                        print("No tiene caracteres.Intente de nuevo")
                        Registrar()
                else:
                    print("No tiene numero.Intente de nuevo")
                    Registrar()
            else:
                print("No tiene minusculas.Intente de nuevo")
                Registrar()
        else:
            print("No tiene mayusculas.Intente de nuevo")
            Registrar()
    else:
        print("Menor a 8.Intente de nuevo")
        Registrar()


def validarUsuario(bname):
    if len(bname) >= 8:
        #print("Es mayor a 8")
        if bname.isupper() == False:
            #print("Tiene mayusculas")
            if bname.islower() == False:
                #print("Tiene minusculas")
                if bname.isdigit() == False:
                    #print("Tiene numero")
                    if bname.isspace() == False:
                        return True
                    else:
                        print("Intente de nuevo")
                        Registrar()
                else:
                    print("Contrasenia invalida.Intente de nuevo")
                    Registrar()
            else:
                print("Contrasenia invalida.Intente de nuevo")
                Registrar()
        else:
            print("Contrasenia invalida.Intente de nuevo")
            Registrar()
    else:
        print("Usuario menor a 6 caracteres.Intente de nuevo")
        Registrar()

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
                    menuVendedor()

                else:
                    print("Contrasenia incorrecta ")
            else:
                print("Usuario no registrado")
        elif wahl=='c' or wahl=='C':
            if user in compradores:
                if compradores[user][0] == passw:
                    print("Bienvenido..."+user)
                    comprarArticulo(user)

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
        validarUsuario(bname)

        passwort = getpass.getpass("Contrasenia: ") #0
        validarContrasenia(passwort)

        nombre = input("Ingresa nombre: ") #1
        apellido = input("Ingresa apellido: ") #2
        edad = input("Ingresa edad: ") #3
        correo = input("Ingresa correo: ")#4
        numTarj = input("Ingresa numero de tarjeta: ") #5
        pp = [] #6
        paypalCorreo = input("Ingresa correo de PayPal: ") #6.0
        pp.append(paypalCorreo)
        paypalContrasenia = getpass.getpass("Ingresa contrasenia de PayPal") #6.1
        pp.append(paypalContrasenia)

        if wahl=='v' or wahl=='V':
            #Vendedores
            listaVendedores.append(passwort) #0
            listaVendedores.append(nombre) #1
            listaVendedores.append(apellido) #2
            listaVendedores.append(edad) #3
            listaVendedores.append(correo)#4
            listaVendedores.append(numTarj) #5
            listaVendedores.append(pp) #6
            vendedores[bname] = listaVendedores
        elif wahl=='c' or wahl=='C':
            #Compradores
            listaCompradores.append(passwort) #0
            listaCompradores.append(nombre) #1
            listaCompradores.append(apellido) #2
            listaCompradores.append(edad) #3
            listaCompradores.append(correo) #4
            listaCompradores.append(numTarj) #5
            listaCompradores.append(pp) #6
            compradores[bname] = listaCompradores
        elif wahl=='a' or wahl=='A':
            #Vendedores
            listaVendedores.append(passwort) #0
            listaVendedores.append(nombre) #1
            listaVendedores.append(apellido) #2
            listaVendedores.append(edad) #3
            listaVendedores.append(correo) #4
            listaVendedores.append(numTarj) #5
            listaVendedores.append(pp) #6
            vendedores[bname] = listaVendedores
            #Compradores
            listaCompradores.append(passwort) #0
            listaCompradores.append(nombre) #1
            listaCompradores.append(apellido) #2
            listaCompradores.append(edad) #3
            listaCompradores.append(correo) #4
            listaCompradores.append(numTarj) #5
            listaCompradores.append(pp) #6
            compradores[bname] = listaCompradores
        else:
            print("Opcion invalida")
    else:
        print("Opcion invalida")


def subirArticulo():
    print("Vendedor\n Subir Articulos:")
    nombreArticulo = input("Nombre del articulo: ")
    descrip = input("Descripcion del articulo: ") #0
    precio = float(input("Precio del articulo: "))#1
    numInventario = int(float(input("Disponibles en el inventario: ")))#2

    listaArticulos.append(descrip) #0
    listaArticulos.append(precio) #1
    listaArticulos.append(numInventario) #2

    articulos[nombreArticulo] = listaArticulos

    print("Operacion aceptada")
    menuVendedor()


def comprarArticulo(user):
    print("Ropa disponible en la tienda: ")
    for prenda in articulos:
        print("* *"+prenda+"* *") #Llaves
        print("Descripcion\n"+articulos[prenda][0])
        print("Precio:\n"+articulos[prenda][1])
        print("En inventario: "+articulos[prenda][2])

    antwort=input("Desea comprar algo de nuestro catalogo? s/n ")
    if antwort=='s' or antwort=='S':
        nombre_Articulo = input("Nombre del articulo (tal cual se muestra en el catalogo): ")
        print("Descripcion\n"+articulos[nombre_Articulo][0])
        print("Precio:\n"+articulos[nombre_Articulo][1])
        print("En inventario: "+articulos[nombre_Articulo][2])
        s = input("Ingrese correo de PayPal para proceder con la compra: ")
        if compradores[user][6][0] == s: 
            conf = input("Confirmar compra s/n: ")
            if conf=='s' or antwort=='S':
                enviarCorreo(nombre_Articulo)
                articulos[nombre_Articulo][2] -= 1
            elif conf=='n' or conf=='N':
                print("Lamentamos oir eso! \nVuelva pronto...")
                comprarArticulo(user)
            else:
                print("Opcion invalida")
                comprarArticulo(user)
        else:
            print("Correo incorrecto. Intente de nuevo... ")
            comprarArticulo(user)
    elif antwort=='n' or antwort=='N':
        print("Hasta luego ")
        menuInicio()
    else:
        print("Opcion invalida ")
        comprarArticulo(user)


menuInicio()        



