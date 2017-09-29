import socket

socketC=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketC.connect(("localhost",10000))

	
while True:
	
	archivo=raw_input("Digite el nombre del archivo al que quiere acceder: ")
	Operacion=raw_input("Digite la operacion a realizar: ")
	if Operacion=="Abrir" or Operacion=="Borrar":
		envioOp=(archivo,Operacion)
	else:
		escritura=raw_input("Digite el texto a escribir: ")
		envioOp=(archivo,Operacion,escritura)
	socketC.send(str(envioOp))
	texto=""
	data = socketC.recv(1024)
	while data:
			texto+=data
			data = socketC.recv(1024)
	break

print "Resultado de la operacion enviada por servidor Intermedio: \n", texto

socketC.close()
