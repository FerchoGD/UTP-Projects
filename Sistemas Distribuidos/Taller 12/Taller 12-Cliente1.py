import xmlrpc.server
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
import threading
import time
import sys
import random


IP = '127.0.0.1'
PORT = 8005
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
	return x + y


#-----------------------------------------------------------

s.register_function(Operacion)
s.register_function(VerificarCapacidad)
t = threading.Thread(target=s.serve_forever)

#-----------------------------------------------------------

portlist = [8005,8006,8007]
t.start()
n=0
CargaProceso=4
print (portlist[n])

print ("Suma")
print ("     ")
numero1=input("Digite el primer numero: ")
numero2=input("Digite el segundo numero: ")

Op = True

while True:
	while n < 3 and Op:
		time.sleep(2)
		try:
			s1 = xmlrpc.client.ServerProxy("http://127.0.0.1:"+str(portlist[n]))
			print (portlist[n])
			verif = s1.VerificarCapacidad(CargaProceso) 
			if verif == 1:
				print("Casi que no...")
				result = s1.Operacion(int(numero1),int(numero2))
				print ("Resultado del proceso: ")
				print (result)
				Op = False
			else:
				print ("Excede carga")
			print ("")
			n+=1
			
		except:
			pass
	n=0
sys.exit()
