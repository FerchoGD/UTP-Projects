import time
import xmlrpc.server
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths=('/RPC2',)
	
server = SimpleXMLRPCServer(("localhost",5000),requestHandler=RequestHandler)


def Tiempo():
	tiempo_seg=time.time()
	print(tiempo_seg)
	return tiempo_seg


server.register_function(Tiempo)
server.serve_forever()

