import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(("localhost", 5000),
                            requestHandler=RequestHandler)

def operacion(op):

	while True:		

		if op=="suma":
			return "http://localhost:10000"

		elif op=="resta":
			return "http://localhost:15000"

		elif op=="multiplicacion":
			return "http://localhost:20000"

		elif op=="division":
			return "http://localhost:25000"

		elif op=="potencia":
			return "http://localhost:30000"

		elif op=="logaritmo":
			return "http://localhost:35000"

		elif op=="raiz":
			return "http://localhost:40000"
		break

server.register_function(operacion,"redireccionar")
server.serve_forever()