#Para importar el modulo
import FuncionesAritmeticas
#from FuncionesAritmeticas import Suma,Resta,resultado
#print(Suma(3,8))
#print(Resta(5,2))
#print(FuncionesAritmeticas.Suma(3,8))
#print(FuncionesAritmeticas.Resta(5,2))

def Menu():
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion ")
    x = int(input("Que desea hacer?"))
    if x == 1:
        x = int(float(input("Dame el primer numero: ")))
        y = int(float(input("Dame el segundo numero: ")))
        print("Suma: ")
        print(FuncionesAritmeticas.Suma(x,y))    
    elif x == 2:
        x = int(float(input("Dame el primer numero: ")))
        y = int(float(input("Dame el segundo numero: ")))
        print("Resta: ")
        print(FuncionesAritmeticas.Resta(x,y))
    elif x == 3: 
        x = int(float(input("Dame el primer numero: ")))
        y = int(float(input("Dame el segundo numero: ")))
        print("Multiplicacion: ")
        print(FuncionesAritmeticas.Multiplicacion(x,y))
    else:
        print("Valor invalido")

Menu()
#print(resultado)