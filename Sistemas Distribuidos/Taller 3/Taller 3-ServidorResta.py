import socket
import threading

ServerR=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ServerR.bind(("",15000))

ServerR.listen(3)

def resta(*args):

	datos=eval(sintermedio.recv(1024))

	result=float(datos[0])-float(datos[1])


	print "Enviando: ", result
	args[0].send(str(result))


while True:
	sintermedio,addr = ServerR.accept()
	threading.Thread(target=resta,args=(sintermedio,addr)).start()


ServerR.close()
sintermedio.close()