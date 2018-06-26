# -*- coding: UTF-8 -*-

#Modulos que nos van a permitir enviar correos

import smtplib, getpass, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
#Autenticacion
user = input("Cuenta gmail: ")
password = getpass.getpass("Contraseña: ")
#Datos del correo
remitente = user
destinatario = input("Para, ejemplo <correoGmail>")
asunto = input("Asunto: ")
mensaje = input("Mensaje: ")
archivo = input("Adjuntar archivo: ")
#Protocolo y puerto
gmail = smtplib.SMTP("smtp.gmail.com",587)
#Certificado de seguridad
gmail.starttls()
#Ingresar
gmail.login(user,password)
gmail.set_debuglevel(1)
#Ingresamos pero falta llenar la informacion
header["Subject"]=asunto
header["From"]=remitente
header["To"]=destinatario
#Convertimos a HTML
mensaje = MIMEText(mensaje,"html")
header.attach(mensaje)
#Comprobar que el archivo exista
#Comprobando que el archivo exista
if(os.path.isfile(archivo)):
	adjunto = MIMEBase("application","octet-stream")
	adjunto.set_payload(open(archivo,"rb").read())
	encode_base64(adjunto)
	adjunto.add_header('Content-Disposition', 'attachment; filename="%s"'%os.path.basename(archivo))
	header.attach(adjunto)

#Enviar email
gmail.sendmail(remitente,destinatario,header.as_string())
#Cerrar sesion
gmail.quit()












