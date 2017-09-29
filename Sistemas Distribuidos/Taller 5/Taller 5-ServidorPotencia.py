import math
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import threading

server=SimpleXMLRPCServer(("localhost",30000))

def Potencia(a,b):
	return pow(float(a),float(b))

server.register_function(Potencia)
server.serve_forever()

	