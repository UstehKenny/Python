#Listas

listaNombre = ["Gerardo","Damian","Cesar"]
print(listaNombre)
print(len(listaNombre))
#Agregar elementos a una lista
listaNombre.append("Kenny")
listaNombre.append("Rodrigo")
listaNombre.append("Carlos")
print(listaNombre)
#Agregar elementos en una posición exacta
listaNombre.insert(1,"Juan")
listaNombre.insert(3,"Irais")
print(listaNombre)
#Borrar elementos de la lista
listaNombre.remove("Juan")
print(listaNombre)
#Ordenar mi lista
listaNumeros = [4,14,8,2,0,1,7,9]
print(sorted(listaNumeros))
nuevaLista = sorted(listaNombre)
print(nuevaLista)
#Ver un elemento de la lista [0...n] [n...-1]
#print(listaNombre[-4])
#Copia de una lista
#newLista = listaNombre[0:6:4]
#print(newLista)
#Buscar el índice de un elemento de la lista
#print(listaNombre.index("Carlos"))

#Tuplas: inmutables. No se pueden modificar.

#tuplaNombres = ("Gerardo", "Cesar")
#print(tuplaNombres)
#print(tuplaNombres[1])