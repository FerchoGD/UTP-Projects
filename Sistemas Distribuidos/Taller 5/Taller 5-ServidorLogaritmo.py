import math
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import threading

server=SimpleXMLRPCServer(("localhost",35000))

def Logaritmo(a,b):
	return math.log(float(a),float(b))

server.register_function(Logaritmo)
server.serve_forever()