import socket
import threading

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("",5000))

server.listen(3)

def operacion(*args):

	recibir= eval(args[0].recv(1024))
	numeros=(recibir[0],recibir[1])
	operador=str(recibir[2])

	while True:
		if recibir[0]=="cerrar" or recibir[1]=="cerrar":
			break		

		serverop=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		if operador=="suma":
			serverop.connect(("localhost",10000))
			serverop.send(str(numeros))

		elif operador=="resta":
			serverop.connect(("localhost",15000))
			serverop.send(str(numeros))

		elif operador=="multiplicacion":
			serverop.connect(("localhost",20000))
			serverop.send(str(numeros))

		elif operador=="division":
			serverop.connect(("localhost",25000))
			serverop.send(str(numeros))

		elif operador=="potencia":
			serverop.connect(("localhost",30000))
			serverop.send(str(numeros))

		elif operador=="logaritmo":
			serverop.connect(("localhost",35000))
			serverop.send(str(numeros))

		elif operador=="raiz":
			serverop.connect(("localhost",40000))
			serverop.send(str(numeros))
		break


	resultado=serverop.recv(1024)
	print "Enviando al cliente: ", resultado
	args[0].send(str(resultado))



while True:
	scliente,addr = server.accept()
	threading.Thread(target=operacion,args=(scliente,addr)).start()

print "Cerrando..."
scliente.close()
server.close()