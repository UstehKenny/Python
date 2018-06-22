def Registro():
	respuesta = 's'
	while respuesta == 's':
		username = input("Nombre de usuario: ")
		password = input("Contraseña: ")
		usuarios = {}
        
		usuarios[username] = password
		listaUsuario = []
		nombre = input("Ingresa nombre: ")
		listaUsuario = listaUsuario.append(nombre)
		appellido = input("Ingresa appellido: ")
		listaUsuario = listaUsuario.append(appellido)
		edad = input("Ingresa edad: ")
		listaUsuario = listaUsuario.append(edad)
		numTarj = input("Ingresa numero de tarjeta: ")
		listaUsuario = listaUsuario.append(numTarj)
		paypal = input("Ingresa cuenta de PayPal: ")
		listaUsuario = listaUsuario.append(paypal)
		
		respuesta = input("¿Deseas hacer otro registro? s/n ")
    return usuarios


def Loggin(**dicc):
    user = input("Usuario: ")
    passw = input("Contraseña: ")
    if user in dicc:
		if passw in dicc:
			print("Bienvenido")
		else:
			print("Contraseña incorrecta")
	else: 
		print("Usuario no registrado")


#Menú 
print("1) Registrarse")
print("2) Ingresar")
x = input("¿Qué desea hacer?")
if x == 1:
	dicc = Registro()
elif x == 2:
	Loggin(dicc)


	



