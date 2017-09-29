import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import threading

server=SimpleXMLRPCServer(("localhost",40000))

def Calcular(a,b):
	return float(a)**(1.0/float(b))

server.register_function(Calcular)
server.serve_forever()