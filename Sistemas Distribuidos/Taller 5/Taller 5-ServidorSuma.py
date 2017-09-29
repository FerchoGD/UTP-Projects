import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import threading

server=SimpleXMLRPCServer(("localhost",10000))

def Suma(a,b):
	return int(a)+int(b)

server.register_function(Suma)
server.serve_forever()
