import xmlrpc.server
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
from datetime import datetime
import threading
import time
import sys


def Promedio(horas):
    a = 0
    for i in range(len(horas)):
        a+=horas[i]
    a /=len(horas)
    return a 

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

IP = '127.0.0.1'
PORT = 5001


# Create server
server = SimpleXMLRPCServer((IP,PORT),
                            requestHandler=RequestHandler)
server.register_introspection_functions()


class MyFuncs:
        def getTime(self):
            return time.time()

server.register_instance(MyFuncs())

t = threading.Thread(target=server.serve_forever)

##Cliente 

portlist = [5000,5001,5002]
Hora =[]
Hpromedio = 0
t.start()
n=0
while True :
    while n<3:
        time.sleep(3)
        try:
            s = xmlrpc.client.ServerProxy("http://127.0.0.1:"+str(portlist[n])) 
            Operar = s.getTime()
            Hora.append(Operar)           
        except: 
            pass

        n = n+1
    promedio = Promedio(Hora)
    Hpromedio = time.ctime(promedio)
    print (Hpromedio)
    n = 0
    Hora = []
sys.exit()


# Run the server's main loop