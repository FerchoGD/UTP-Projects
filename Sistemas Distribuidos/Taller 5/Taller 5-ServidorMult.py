import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import threading

server=SimpleXMLRPCServer(("localhost",20000))

def Multiplicacion(a,b):
	return float(a)*float(b)

server.register_function(Multiplicacion)
server.serve_forever()