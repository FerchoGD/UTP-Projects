#Jhon Albert Arango Duque
#Dubel Fernando Giraldo Duque

#Sistemas Distribuidos- Gr 2
#UTP

#-----------------------------------------------------------

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from datetime import datetime
import xmlrpclib
import threading
import time
import sys
import random
import os

#Ip del cliente 3
Ip = '127.0.0.1'  
#Puerto del cliente 3  
Port = 5008
#Archivos del Cliente 3
MyFiles=["Apa.txt"]
#-----------------------------------------------------------

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

s = SimpleXMLRPCServer((Ip,Port),
                            requestHandler=RequestHandler)
s.register_introspection_functions()
#-----------------------------------------------------------

# Clase que contiene las funciones de leer,actualizar y borrar.
class Functions:

	def ReadFileL(self,Name):
		FileA=open(Name,"r")
		Content=FileA.read()
		FileA.close()
		return Content
 
	def UpdateFileA(self,Name,Information):
		FileA=open(Name,"w")
		FileA.write(Information)
		FileA.close()
		return 01

	def RemoveFileE(self,Name):
		for FileA in MyFiles:
			if FileA==Name:
				MyFiles.remove(Name)
				os.remove(Name)
				return 01

#-----------------------------------------------------------
# Registro de clase-funciones.
s.register_instance(Functions())

# Hilo.
t = threading.Thread(target=s.serve_forever)
t.start()
#-----------------------------------------------------------

#Coneccion con el servidor principal.
Server = xmlrpclib.ServerProxy('http://localhost:5006')

#registro de cliente y archivos en servidor.
print "Register files .................%"

RegistryClient = Server.RegisterClient(Ip, Port)
if RegistryClient != "Cliente ya registrado":
	for i in MyFiles:
		f=open(i)
		contenido=f.read()
		RegistryFile = Server.RegisterFile(i, Ip, Port,contenido)
		print i
		time.sleep(1)
		
# Principal
while True :
	
#------------------Menu------------------------

	print "                 Digite la operacion a realizar:\n"
	print "1)) Lista de mis archivos"
	print "2)) Lista de archivos Compartidos"
	print "3)) Leer archivo."
	print "4)) Escribir en archivo."
	print "5)) Cerrar cliente"
	Opcion=raw_input("Opcion: ")
	print " "
	print " "
	
#Opcion listar mis archivos.
	
	if Opcion == '1':
		i = 1 
		print "Mis archivos son:"
		for FileM in MyFiles:
			print str(i) + ")) " + FileM
			i += 1
	
#Opcion listar archivos compartidos.

	if Opcion == '2':
		arch = Server.ListFile()
		i = 1
		print "Los archivos compartidos son:"
		for FileM in arch:
			print str(i) + ")) " + FileM
			i += 1
			
#Opcion leer archivos
	if Opcion == '3':
			Ent1 = raw_input("Ingrese el nombre del archivo: ")
			Name=Ent1+".txt"
			Content1 = Server.SearchFileR(Name)
			if Content1 == "Nope":
				print "No se encuentra el archivo"
			else:
				ooo = Server.RegisterAccess(str(Ip),str(Port),Name,"Lectura")
				print "\n",Content1

#Opcion Escribir en archivos.

	if Opcion == '4':
		Ent1 = raw_input("Ingrese el nombre del archivo: ")
		Name=Ent1+".txt"
		AddressE=Ip+":"+str(Port)
		Var,Address = Server.SearchFileW(Name,AddressE)
		if Var == "El archivo no existe":
			print "El archivo no se encuentra"
		if Var == "Locked":
			print "El archivo se encuentra en uso"

		if Var == "No-PerWriting":
			print "No tiene permiso para modificar archivo"
 
		if Var == "Yes":
			ooo = Server.RegisterAccess(str(Ip),str(Port),Name,"Escritura")
			print "Permiso de escritura Establecido."
			print ""
			while True:
				print "***Si termino de editar el archivo por favor colocar READY ***"
				Opc = raw_input()
				if Opc == "READY":
					Server.DLocked(Name)
					Server.UpdateFiles(Name,Address)
					break
	if Opcion == "5":
		S=Server.RemoveFileServer(Ip,Port)
		sys.exit()
	print ""
