import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import threading

server=SimpleXMLRPCServer(("localhost",15000))

def Resta(a,b):
	return float(a)-float(b)

server.register_function(Resta)
server.serve_forever()