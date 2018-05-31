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

#Ip del cliente 2
Ip = '127.0.0.1' 
#Puerto del cliente 2
Port = 5005 
#Archivos del Cliente 2
MyFiles=["Kerr.txt", "James.txt","Juan.txt","Coco.txt"] 

#-----------------------------------------------------------

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

s = SimpleXMLRPCServer((Ip,Port),
                            requestHandler=RequestHandler,allow_none=True)
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
print "Register pag .................%"

RegistryClient = Server.RegisterClient(Ip, Port)
if RegistryClient != "Cliente ya registrado":
	
	for i in MyFiles:
		f=open(i)
		contenido=f.read()
		DateMod = int(time.time())
		RegistryFile = Server.RegisterFile(i, Ip, Port,contenido,DateMod)
		print i
		time.sleep(1)
	Longitud=Server.LenCli()
	if Longitud == 2:
		Server.FirstCopy(Ip,Port,contenido)
		

		
# Principal
while True :
	
#------------------Menu------------------------

	print "                 Digite la operacion a realizar:\n"
	print "1)) Lista de mis paginas"
	print "2)) Leer Pagina."
	print "3)) Modificar Pagina."
	print "4)) Permisos Asignados"
	Opcion=raw_input("Opcion: ")
	print " "
	print " "

#-----------------------------------------------------------
#Opcion listar mis archivos.
	
	if Opcion == '1':
		i = 1 
		print "Mis paginas son:"
		for FileM in MyFiles:
			print str(i) + ")) " + FileM
			i += 1
	

#-----------------------------------------------------------
#Opcion leer archivos
	if Opcion == '2':
			Ent1 = raw_input("Ingrese el nombre del archivo: ")
			Name=Ent1+".txt"
			Content1 = Server.SearchFileR(Name)
			if Content1 == "Nope":
				print "No se encuentra el archivo"
			else:
				print Content1



#-----------------------------------------------------------
#Opcion Escribir en archivos.

	if Opcion == '3':
		Ent1 = raw_input("Ingrese el nombre del archivo: ")
		Name=Ent1+".txt"
		AddressE=Ip+":"+str(Port)
		Var,Address, original = Server.SearchFileW(Name,AddressE)
		
		if Var == "El archivo no existe":
			print "El archivo no se encuentra"
			
		if Var == "Locked":
			print "Pagina en uso"
			
		if Var == "No-PerWriting":
			print "Fallo de pagina"
		
		elif Var == "Yes":
			print "Acceso Permitido."
			if os.path.isfile(Name):
				os.remove(Name)
			else:
				op = Server.clienteRet(Ip,Port)

			time.sleep(4)
			f=open(Name,"w")
			f.write(original)
			f.close()
			opa="C:\\Program Files (x86)\\Geany"+" "+Name
			os.system(opa)
			print ""
			while True:
				print"***Si termino de editar el archivo por favor colocar READY ***"
				Opc = raw_input()
				if Opc == "READY":
					Server.DLocked(Name)
					Link1 = xmlrpclib.ServerProxy(Address)
					f=open(Name)
					Text1=f.read()
					solo=Link1.UpdateFileA(Name,Text1)
					Server = xmlrpclib.ServerProxy('http://localhost:5006')	
					nada=Server.UpdatePagControl(Name,Text1)
					break

#Opcion en archivos.

	if Opcion == '4':
			print "Permisos"
			v=Server.listarpermisos(Port,Ip)
			print v
#---------------------------------------------------------
