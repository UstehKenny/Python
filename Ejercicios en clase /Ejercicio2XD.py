#Capturar nombres, apellidos y edad. Los datos se tienen que guardar en una lista y además  puede ingresar los usuarios que quiera

personas = []


while True:
	num = input("Cuántos usuarios quiere ingresar? ")
	try:
		num=int(num)
		return num
	except ValueError:
		print("Inválido")

con = 0

while con < num:
	n = input("Nombre: ")
	personas.append(n)
	a = input("Apellidos: ")
	personas.append(a)
	e = input("Edad: ")
	personas.append(e)
	con+=1

for usuario in personas:
	print(usuario)

