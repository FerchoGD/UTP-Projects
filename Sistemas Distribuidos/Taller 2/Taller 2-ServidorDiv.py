import socket
import threading

ServerD=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ServerD.bind(("",25000))

ServerD.listen(3)

def division(*args):	

	datos=eval(sintermedio.recv(1024))

	result=float(datos[0])/float(datos[1])

	print "Enviando: ", result
	args[0].send(str(result))

while True:
	sintermedio,addr = ServerD.accept()
	threading.Thread(target=division,args=(sintermedio,addr)).start()

ServerD.close()
sintermedio.close()