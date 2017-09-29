import socket
import threading

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("",5000))

server.listen(3)

def operacion(*args):

	recibir= args[0].recv(1024)
	operador=str(recibir)

	while True:
		if recibir[0]=="cerrar" or recibir[1]=="cerrar":
			break		

		if operador=="suma":
			a="localhost"
			b="10000"
			direccion=(a,b)
			args[0].send(str(direccion))
			

		elif operador=="resta":
			a="localhost"
			b="15000"
			direccion=(a,b)
			args[0].send(str(direccion))
			

		elif operador=="multiplicacion":
			a="localhost"
			b="20000"
			direccion=(a,b)
			args[0].send(str(direccion))
			

		elif operador=="division":
			a="localhost"
			b="25000"
			direccion=(a,b)
			args[0].send(str(direccion))
			

		elif operador=="potencia":
			a="localhost"
			b="30000"
			direccion=(a,b)
			args[0].send(str(direccion))
			

		elif operador=="logaritmo":
			a="localhost"
			b="35000"
			direccion=(a,b)
			args[0].send(str(direccion))
			

		elif operador=="raiz":
			a="localhost"
			b="40000"
			direccion=(a,b)
			args[0].send(str(direccion))
		break

while True:
	scliente,addr = server.accept()
	threading.Thread(target=operacion,args=(scliente,addr)).start()

print "Cerrando intermedio..."
scliente.close()
server.close()