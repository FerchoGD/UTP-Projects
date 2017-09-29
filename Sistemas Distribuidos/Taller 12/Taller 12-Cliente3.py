import xmlrpc.server
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
import threading
import time
import sys
import random


IP = '127.0.0.1'
PORT = 8007
#-----------------------------------------------------------

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

s = SimpleXMLRPCServer((IP,PORT),
                            requestHandler=RequestHandler)
s.register_introspection_functions()
#-----------------------------------------------------------

def VerificarCapacidad(n):
	cargapc = random.randint(0,100)
	if cargapc >= n:
		return 1
	else:
		return 0

def Operacion(x,y):
	return (x + y)


#-----------------------------------------------------------

s.register_function(Operacion)
s.register_function(VerificarCapacidad)
t = threading.Thread(target=s.serve_forever)

#-----------------------------------------------------------

portlist = [8006,8006,8006]
t.start()
n=0
CargaProceso=4

while True :
	while n<3:
		time.sleep(3)
		try:
			s1 = xmlrpc.client.ServerProxy("http://127.0.0.1:"+str(portlist[n]))
			verif = s1.VerificarCapacidad(CargaProceso) 
			print (verif)
			if verif==1:
				result = s1.Operacion(numero1,numero2)
				print (result)
				
		except:
			pass

		n+=1
	n = 0
sys.exit()
