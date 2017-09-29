import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import threading

server=SimpleXMLRPCServer(("localhost",25000))

def Division(a,b):
	return float(a)/float(b)

server.register_function(Division)
server.serve_forever()