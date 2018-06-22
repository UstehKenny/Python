"""
def HolaMundo():
	print("Hola mundo")

def Mensaje(mensaje):
	print("El mensaje es: ", mensaje)

mensajeMandar = input("Dame el mensaje ")

Mensaje(mensajeMandar)
HolaMundo()

def Suma(numero1,numero2):
	print("La suma total es: ", numero1+numero2)

numero1 = int(input("Dame el valor 1 "))
numero2 = int(input("Dame el valor 2 "))

Suma(numero1,numero2)
"""
def Suma2(*numeros):
	total = 0
	for numero in numeros:
		total+=numero
	return total

sumaTotal = Suma2(3,3,2,6,7,8,1,76,12)
print("La suma total es: ",sumaTotal)

def dicc2(**diccionarios):

	for llave,valor in diccionarios.items():
		print(llave," ",valor)
		


dicc2(llave1="valor1",llave2="valor2")
#print("La suma total es: ",sumaTotal)
