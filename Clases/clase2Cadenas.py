#Cadena:
#Arreglo de caracteres
cadena = "Este es el Curso de Python"
print(len(cadena))
print(cadena[11:16])
print(cadena[:20]) #Hasta el 20
print(cadena[20:]) #20 en adelante
print(cadena[::]) #Todo
#Formato de cadena
print(cadena.upper()) #Cambia a mayúsculas
print(cadena.lower()) #Cambia a minúsculas
print(cadena.swapcase()) #Invierte mayúsculas con minúsculas y viceversa
print(cadena.title()) #Formato de título
print(cadena.capitalize())
print(cadena.center(35, "-"))
print(cadena.count("Curso"))

#Ciclos
#FOR

listaUsuarios = ["Kenny","Damian","Ricardo","Alberto","Gerardo"]
#Leer de teclado
usuario = input("Ingresa el usuario\n")
listaUsuarios.append(usuario)
for usuario in listaUsuarios: print(usuario)

#Ciclo while
contador = 0
while contador < 10:
	print("El contador tiene valor de: ", contador)
	contador+=1 #contador = contador + 1



