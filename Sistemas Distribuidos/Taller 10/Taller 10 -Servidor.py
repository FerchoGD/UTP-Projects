import time
import xmlrpc.server
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths=('/RPC2',)
	
server = SimpleXMLRPCServer(("localhost",5000),requestHandler=RequestHandler)
cont=0
horaservidor=0

def Tiempo(horacliente):
	global cont, horaservidor
	cont+=1
	horaservidor+=horacliente
	print(time.ctime(horaservidor/cont))
	return horaservidor/cont


server.register_function(Tiempo)
server.serve_forever()

