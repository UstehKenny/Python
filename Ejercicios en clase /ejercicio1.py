print("------------------------------")
# a)Edad
print("\nEjercicio 1: Edad para entrar al antro\n")
edad = int(input("Edad?\n"))
if edad > 18: #Si la persona tiene más de 18 años
	print("Puedes entrar\n")
elif edad == 18: #Si la persona tiene 18 años
	print("Presenta INE\n")
else: #Se asume que es menor de 18 años
	print("No puedes entrar\n")


print("------------------------------")
# b)Invertir el valor de dos variables
print("\nEjercicio 2: Invertir valores\n")
#Se dan por defecto dos números a las variables a y b
a = 90
b = 91
#Le damos a conocer al usuario los valores de cada variable
print("Valor inicial de a: ", a, "\nValor inicial de b: ", b)
#Para invertir los valores de ambas 
a = a + b #Sumamos el valor de 'b' a 'a'.
b = a - b #Le restamos a 'b' el valor de 'a' para así invertir la primera variable.
a = a - b #Como el valor de 'a' es mayor al que se le asignó inicialmente, le restamos 'b' para regresar al valor inicial.
print("*************************")
#Se imprimen las variables con valor invertido
print("Valor de a: ", a,"\nValor de b: ", b)



print("\n------------------------------")
# c) Fórmula General
import math #Nos sirve para obterner la raíz cuadrada
print ("\nEjercicio 3: Fórmula General\n")

#Pediremos al usuario el término cuadrático, lineal e independiente.

A = int(input("Ingresa el valor de a:  ")) 
B = int(input("Ingresa el valor de b:  "))
C = int(input("Ingresa el valor de c:  "))

#Comprobamos que sea una ecuación cuadrática
if A != 0:
#Obtenemos el discriminante para saber el resultado de las raíces
	d = B*B-4*A*C
	if d < 0: #Si es menor a 0, sabemos que las raíces son imaginarias
		print("No tiene soluciones reales")
	else:
		x1 = (-B+(math.sqrt(d)))/(2*A)
		x2 = (-B-(math.sqrt(d)))/(2*A)
		if x1 == x2: #Asimismo, cuando el discriminante es igual a 0, las raíces son las mismas
			print("Misma solución real para ambas raíces: ", x1)
		else: #Cuando el discriminante es mayor a 0, tiene dos raíces diferentes
			print("Tiene 2 soluciones: \nx1 = ", x1, "\tx2 = ", x2)
else: #Como A = 0, asumimos que no es una ecuación cuadrática y que puede ser ec. lineal o constante.
	print("No es una ecuación cuadrática")

print("\n------------------------------")

