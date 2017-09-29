import socket
import threading

serverS=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverS.bind(("",10000))

serverS.listen(3)

def suma(*args):

	datos=eval(sintermedio.recv(1024))

	result=float(datos[0])+float(datos[1])


	print "Enviando: ", result
	args[0].send(str(result))


while True:
	sintermedio,addr = serverS.accept()
	threading.Thread(target=suma,args=(sintermedio,addr)).start()


serverS.close()
sintermedio.close()
