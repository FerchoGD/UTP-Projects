import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import threading

server=SimpleXMLRPCServer(("localhost",10000))

def Calcular(a,b):
	return int(a)+int(b)

server.register_function(Calcular)
server.serve_forever()
