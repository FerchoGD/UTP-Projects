import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import threading

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(("localhost", 5000),
                            requestHandler=RequestHandler)

def operacion(uno,dos,op):

	while True:
		if uno=="cerrar" or dos=="cerrar":
			break		

		if op=="suma":
			suma=xmlrpclib.ServerProxy("http://localhost:10000")
			return suma.Suma(uno,dos)

		elif op=="resta":
			resta=xmlrpclib.ServerProxy("http://localhost:15000")
			return resta.Resta(uno,dos)

		elif op=="multiplicacion":
			mult=xmlrpclib.ServerProxy("http://localhost:20000")
			return mult.Multiplicacion(uno,dos)

		elif op=="division":
			div=xmlrpclib.ServerProxy("http://localhost:25000")
			return div.Division(uno,dos)

		elif op=="potencia":
			pot=xmlrpclib.ServerProxy("http://localhost:30000")
			return pot.Potencia(uno,dos)

		elif op=="logaritmo":
			log=xmlrpclib.ServerProxy("http://localhost:35000")
			return log.Logaritmo(uno,dos)

		elif op=="raiz":
			raiz=xmlrpclib.ServerProxy("http://localhost:40000")
			return raiz.Raiz(uno,dos)
		break

server.register_function(operacion,"calcular")
server.serve_forever()