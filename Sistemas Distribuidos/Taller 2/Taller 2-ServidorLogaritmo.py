import socket
import math
import threading

ServerL=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ServerL.bind(("",35000))

ServerL.listen(3)

def log(*args):

	datos=eval(sintermedio.recv(1024))

	result=math.log(float(datos[0]),float(datos[1]))


	print "Enviando: ", result
	args[0].send(str(result))

while True:
	sintermedio,addr = ServerL.accept()
	threading.Thread(target=log,args=(sintermedio,addr)).start()

ServerL.close()
sintermedio.close()