personas = []

num = int(float(input("Cuántos usuarios quiere ingresar? ")))

if type(num) == int:   
    con = 0
    while con < num:
        n = input("Nombre: ")
        personas.append(n)
        a = input("Apellidos: ")
        personas.append(a)
        e = input("Edad: ")
        personas.append(e)
        con+=1
else:
    print("Inválido")
    


for usuario in personas:
	print(usuario)
    

