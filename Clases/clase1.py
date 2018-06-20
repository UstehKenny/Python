print("Hola mundo")
print('Este es otro mensaje')
print("\"Esta es otra impresion\"\n\n")

#Tipos de datos
#Tipado Dinamico

#Entero 
variable = 3
print(variable)
t = type(variable)
print(t,"\n")

#Flotante

variable2 = 3.4
print(variable2)
t2 = type(variable2)
print(t2,"\n")

#Booleano True/False

variable3 = True
print(variable3)
t3 = type(variable3)
print(t3,"\n")

#String

variable4 = "Esta es una cadena"
print(variable4)
t4 = type(variable4)
print(t4,"\n")


#Operaciones Aritmeticas
num1 = 10
num2 = 3

#Suma

print(num1 + num2) 

#Resta

print(num1 - num2)

#Multiplicacion

print(num1 * num2)

#Potencia

print(num1 ** num2)
print(pow(num1,num2))

#Division
 
print(num1 / num2)

#Comparadores

print(3 > 5) #False
print(3 < 5) #True

print(5 == 5) #True
print(5 == 6) #False

print(5 != 6) #True
print(5 != 5) #False

print("Hola" == "hola")

#Sentencias de control

if(7 > 8):
	print("El 7 es mayor") #Concatenacion: print("El numero" + str(numero1) + "es mayor")
else:
	print("El otro numero es mayor a 7") #Interpolación print("El numero", numero2 ,"es mayor")



