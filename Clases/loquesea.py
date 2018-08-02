#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:14:02 2018

@author: carokennedy
"""

#Diccionarios (HashMap)

diccionario = {"Llave":5,"Llave2":"Hola","Llave3":True,"Llave4":3.5}
#print(diccionario["Llave4"])

#Para recorrer un diccionario
for elemento in diccionario:
	print(elemento) #Nos muestra las llaves
	print(diccionario[elemento]) #Accedemos al valor de las llaves

for llave,valor in diccionario.items():
	print("El nombre de la llave es: ",llave," y su valor es ",valor)

arregloUsuarios = ["Gekko","Gforce","DrGoku"]
diccionariosUsuarios = dict.fromkeys(arregloUsuarios,"VALOR")
print(diccionariosUsuarios)

#Agregar elementos al diccionario

diccionario["Llave5"] = "Nuevo elemento"
#diccionario.get("Llave5") == diccionario["Llave5"]
print(diccionario)

#Validar si la llave existe

if diccionariosUsuarios.has_key("Llave2"):
	print("Si existe esa llave")
else:
	print("No existe esa llave")