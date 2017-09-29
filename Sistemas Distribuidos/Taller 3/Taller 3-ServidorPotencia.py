import socket
import threading

ServerP=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ServerP.bind(("",30000))

ServerP.listen(3)

def potencia(*args):

	datos=eval(sintermedio.recv(1024))

	result=pow(float(datos[0]),float(datos[1]))

	print "Enviando: ", result
	args[0].send(str(result))

while True:
	sintermedio,addr = ServerP.accept()
	threading.Thread(target=potencia,args=(sintermedio,addr)).start()

ServerP.close()
sintermedio.close()