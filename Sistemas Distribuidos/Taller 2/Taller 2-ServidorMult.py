import socket
import threading

ServerM=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ServerM.bind(("",20000))

ServerM.listen(3)

def mult(*args):

	datos=eval(sintermedio.recv(1024))

	result=float(datos[0])*float(datos[1])


	print "Enviando: ", result
	args[0].send(str(result))


while True:
	sintermedio,addr = ServerM.accept()
	threading.Thread(target=mult,args=(sintermedio,addr)).start()

ServerM.close()
sintermedio.close()