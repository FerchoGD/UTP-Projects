import math
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import threading

server=SimpleXMLRPCServer(("localhost",35000))

def Calcular(a,b):
	return math.log(float(a),float(b))

server.register_function(Calcular)
server.serve_forever()