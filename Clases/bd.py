import psycopg2
import pprint
import sys

def main():
	#Informacion para la conexion
	cadenaConexion = "host ='localhost' dbname='Tienda' user='postgres' password='1q2w3e4r'"
	#Conexion de la base de datos
	obj=psycopg2.connect(cadenaConexion)
	#Cursor para el manejo de las consultas
	objCursor=obj.cursor()
	#Ejecutar instruccion SQL
	objCursor.execute("INSERT INTO comprador(nombre,apellido,edad,tarjetaCredito,correpaypal,password,username,pass) VALUES('Gerardo'.'Castillo',21,'123-232-111-232','ferrari_gerardo@live.com.mx','1q2w3e4r','Gekko','1q2w3e4r') ")
	obj.commit()
	#Leer Datos
	objCursor.execute("SELECT * FROM comprador")
	#Mandarlo a imprimir
	registros = objCursor.fetchall()
	pprint.pprint(registros)
	obj.close()