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


IP = '127.0.0.1' #Ip del servidor
PORT = 5006		 #Puerto del servidor
#-----------------------------------------------------------
# Definiendo las clases que necesitamos para gestionar los archivos (directorios)


#Clase para el archivo
class FileC:
	def __init__(self,name,ip,port,Datemod):
		self.nombre=name
		self.ipcliente=ip
		self.puertocliente=port
		self.Datemod=Datemod
#-----------------------------------------------------------

#Clase para el cliente
class ClientC:
	def __init__(self,ip,port):
		self.Files=[]
		self.ipAddress=ip
		self.port=port
		
	def AddFileC(self,FileA):
		self.Files.append(FileA)

	def RemoveFileC(self,FileA):
		for arch in self.FileA:
			if arch == FileA:
				self.Files.remove(FileA)

#-----------------------------------------------------------

#Clase para el archivo compartido
class FileSharedC:
	def __init__(self,ip,port,Name,Cont,DateMod):
		self.ip=ip								
		self.port=port
		self.Name=Name
		self.Cont=Cont
		self.PerWriting=[] #Lista de permisos de escritura a los clientes.
		self.PerWriting.append(ip+":"+str(port))
		self.DateMod=DateMod
		
#-----------------------------------------------------------

#Conexion RPC / Registro de Clases
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

s = SimpleXMLRPCServer((IP,PORT),
                            requestHandler=RequestHandler,allow_none=True)
s.register_introspection_functions()

#-----------------------------------------------------------

#Clase que contiene todas las funciones ejecutadas por el servidor
class Functions:
	
	def __init__(self):
		self.Clients=[]
		self.PagControl=[]
		self.Lockedfiles=[]

#-----------------------------------------------------------

	#Funcion que registra cada lectura y escritura realizada por los clientes. (Datos guardados en HistorialAcceso.txt)
	def RegisterAccess(self,Ip,Port,Name,Acct):
		access=open("HistorialAcceso.txt","a")
		access.write("CLiente:"+Ip+":"+Port+"|| Nombre de Archivo:"+Name+"|| Fecha/Hora:"+time.ctime(time.time())+"|| Accion:"+Acct+"\n")
		access.close()
		return 0
		
		
#-----------------------------------------------------------
	
	#Funcion que elimina archivos del servidor,L.compartidos,L.bloqueo ha archivos existentes en clientes que se han cerrado.
	def RemoveFileServer(self,Ip,Port):
		Auxi1=[]
		for N in self.PagControl:
			if N.ip==Ip and N.port==Port:
				Auxi1.append(N.Name)
		for N in self.Lockedfiles:
			if N.ip==Ip and N.port==Port:
				self.Lockedfiles.remove(N)
		for N in self.Clients:
			if N.ipAddress==Ip and N.port==Port:
				self.Clients.remove(N)
		print Auxi1
		for Elem in Auxi1:
			print Elem
			print""
			for date in self.PagControl:
				print Elem
				print date.Name
				if str(Elem) == str(date.Name):
					self.PagControl.remove(date)
					os.remove(date.Name)
		return 0
		
		
#-----------------------------------------------------------

	#Funcion que registra cada cliente que se conecta al servidor y le asigna permisos deacuerdo a los archivos compartidos.
	def RegisterClient(self,ip,port):
		for cl in self.Clients:
			if cl.ipAddress==ip and cl.port==port:
				return "El Cliente ya se encuentra registrado"
		cli=ClientC(ip,port)
		
		#Permisos de escritura aleatorio a clientes que se registran.

		for perm in self.PagControl:
			Typepermi= random.randint(0,1)
			if Typepermi==1:
				perm.PerWriting.append(ip+":"+str(port))
				
		self.Clients.append(cli)
		return "Cliente registrado!"


	def LenCli(self):
		return len(self.Clients)
		
	def listarpermisos(self,port,ip):
		lista=[]
		for n in self.PagControl:
			for m in n.PerWriting:
				dato = ip+":"+str(port)
				if m == dato:
					lista.append(n.Name)
		car=str(lista)
		return car
		
#-----------------------------------------------------------

	#Funcion que genera copias del primer cliente.
	
	def FirstCopy(self,Ip,Port,contenido):
		for Pag in self.Clients[0].Files:
			self.Clients[1].Files.append(Pag)
			for n in self.PagControl:
				if Pag.nombre == n.Name:
					Address = "http://"+Ip+":"+str(Port)
					Link1 = xmlrpclib.ServerProxy(Address)
					op=Link1.UpdateFileA(n.Name,n.Cont)
		return 1
	
	def LRU(self,cliente):
		ip=cliente.ipAddress
		port=cliente.port
		cont=10000000000000000000000000000000000000000000000000
		
		for archivo in cliente.Files:
			if str(archivo.puertocliente) != str(port):
				if archivo.Datemod <= cont:
					cont=archivo.Datemod
					nombre=archivo.nombre
					objetoarchivo=archivo
		cliente.Files.remove(objetoarchivo)
		Address = "http://"+ip+":"+str(port)
		Link1 = xmlrpclib.ServerProxy(Address)
		op=Link1.RemoveFileE(nombre)
		return 0
		
	def clienteRet(self,ip,port):
		for client in self.Clients:
			if client.ipAddress== ip and client.port == port:
				if len(client.Files)>=8:
					self.LRU(client)
		return 0
			
#-----------------------------------------------------------

	#Funcion que registra cada archivo que contiene los clientes registrados.
	def RegisterFile(self, Name, ip, port, Cont,DateMod):
		Fil = FileC(Name, ip, port,DateMod)
		
		for c in self.PagControl:
			if c.Name == Name:
				return "Archivo ya registrado"
				
		for cli in self.Clients:
			if len(cli.Files) < 8:
				cli.AddFileC(Fil)
			else:
				self.LRU(cli)
				cli.AddFileC(Fil)
				
		FileShared = FileSharedC(ip, port, Name, Cont, DateMod)
		
		for p in self.Clients:
			permiso = random.randint(0,1)
			Address = p.ipAddress+":"+str(p.port)
			Address2 = ip+":"+str(port)
			if permiso == 1 and Address != Address2:
				FileShared.PerWriting.append(Address)

		self.PagControl.append(FileShared)
		
		if len(self.Clients) >= 2:
			for cli in self.Clients:
				i=cli.ipAddress
				p=cli.port
				Address = "http://"+i+":"+str(p)
				Link1 = xmlrpclib.ServerProxy(Address)
				op=Link1.UpdateFileA(Name,Cont)
		return 1
		
#-----------------------------------------------------------
	
	#Funcion que retorna la lista con el nombre de los archivos compartidos.
	def ListFile(self):
			listArch = []
			for i in self.PagControl:
				listArch.append(i.Name)
				
			return listArch
			
#-----------------------------------------------------------

	#Funcion que permite leer archivos al cliente.
	def SearchFileR (self, Name):
			for Conte in self.PagControl:
				if Conte.Name == Name:
					return Conte.Cont
			return "Nope"

#-----------------------------------------------------------

	#Funcion que permite editar archivos a los clientes conectados.
	def SearchFileW (self, Name,AddressE):
				for Lock in self.Lockedfiles:
					if Lock.Name == Name:
						return "Locked",0,0
				for Conte in self.PagControl:
					if Conte.Name == Name:
						if AddressE in Conte.PerWriting:
							self.Lockedfiles.append(Conte)						
							print "Permiso de escritura Establecido"
							Address = "http://"+Conte.ip+":"+str(Conte.port)
							return "Yes",Address, Conte.Cont
						else:
							return "No-PerWriting",0,0
						
						
						
							
#-----------------------------------------------------------

	#Funcion que actualiza los archivos editados al cliente que los contiene.
	def UpdatePagControl(self,Name,Contenido):
		horamodifico=time.time()		
		for archiv in self.PagControl:
			if archiv.Name == Name:
				archiv.Cont=Contenido
				archiv.DateMode=horamodifico
		for client in self.Clients:
			for fil in client.Files:
				if Name == fil.nombre:
					Add="http://"+client.ipAddress+":"+str(client.port)
					Link1 = xmlrpclib.ServerProxy(Add)
					solo=Link1.UpdateFileA(Name,Contenido)
					fil.DateMode=horamodifico
					
		
		return 0
		
#-----------------------------------------------------------

	#Funcion que elimina un archivo de la lista de bloqueados
	def DLocked(self, Name):
		for f in self.PagControl:
			if f.Name == Name:
				self.Lockedfiles.remove(f)
				return 0
							

#-----------------------------------------------------------

t = threading.Thread(target=s.serve_forever)
s.register_instance(Functions())
#-----------------------------------------------------------

t.start()


