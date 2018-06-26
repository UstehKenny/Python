#Archivos
#Lectura
"""
archivo = open('archivo.txt','r')
contenido = archivo.readlines() #readline ; readlines
for linea in contenido:
    print(linea)
print(contenido)"""
#Escritura
archivo2 = open('archivo3.txt','r+')
print(archivo2.read())
cadena = "Este es mi archivo dos"
archivo2.write("Primera cadena: " + cadena)
#Append
#archivo2 = open('archivo3.txt','r+') #'a';'w+';'r+'
cadena = "Linea2"
cadena2 = "\nLinea3"
archivo2.write("\nSegundas cadena: " + cadena)
arregloCadenas = ["\nLinea4","\nLinea5"]
archivo2.write(cadena2)
archivo2.writelines(arregloCadenas)
archivo2.close()