import xmlrpc.server
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import os


class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths=('/RPC2',)
	
server = SimpleXMLRPCServer(("localhost",5000),requestHandler=RequestHandler)


def Ejecutar(op,archivo,texto):
	while True:
		respuesta="nula"
		if op=="Abrir":
			respuesta="exitosa"
			f=open(archivo)
			contenido=f.read()
			f.close()
			resultado=open("log.txt","a+")
			resultado.write("\n"+op+"\n")
			resultado.write(respuesta+"\n")
			resultado.close()
			return contenido			
		elif op=="Borrar":
			os.remove(archivo)
			respuesta="exitosa"
			resultado=open("log.txt","a+")
			resultado.write("\n"+op+"\n")
			resultado.write(respuesta+"\n")
			resultado.close()
			return("El archivo fue borrado exitosamente")
		elif op=="Escribir":
			f=open(archivo,"a")
			f.write(texto)
			f.close()
			respuesta="exitosa"	
			resultado=open("log.txt","a+")
			resultado.write("\n"+op+"\n")
			resultado.write(respuesta+"\n")
			resultado.close()
			return("Se escribio en el archivo con exito")
		break
		
server.register_function(Ejecutar)
server.serve_forever()


