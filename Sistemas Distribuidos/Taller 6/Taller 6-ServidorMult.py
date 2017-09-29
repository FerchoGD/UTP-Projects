import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import threading

server=SimpleXMLRPCServer(("localhost",20000))

def Calcular(a,b):
	return float(a)*float(b)

server.register_function(Calcular)
server.serve_forever()