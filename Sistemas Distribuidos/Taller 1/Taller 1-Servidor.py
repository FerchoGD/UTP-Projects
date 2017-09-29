import socket

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("",5000))

server.listen(1)

scliente,addr = server.accept()

sum=0

while True:

	recibir= eval(scliente.recv(1024))

	if recibir[0]=="cerrar" or recibir[1]=="cerrar":
		break

	print str(addr[0]) + " dice: ", recibir
	sum=int(recibir[0])+int(recibir[1])
	print "Enviando: ", sum
	scliente.send(str(sum))


print "Cerrando..."
scliente.close()
server.close()