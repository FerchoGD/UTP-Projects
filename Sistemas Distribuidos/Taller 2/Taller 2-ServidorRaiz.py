import socket
import threading

ServerRaiz=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ServerRaiz.bind(("",40000))

ServerRaiz.listen(3)

def raiz(*args):

	datos=eval(sintermedio.recv(1024))

	result=float(datos[0])**(1.0/float(datos[1]))


	print "Enviando: ", result
	args[0].send(str(result))

while True:
	sintermedio,addr = ServerRaiz.accept()
	threading.Thread(target=raiz,args=(sintermedio,addr)).start()

ServerRaiz.close()
sintermedio.close()