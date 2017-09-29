import socket

mi_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mi_socket.connect(("localhost",5000))


while True:
	primero=raw_input("Digite el primer numero: ")
	segundo=raw_input("Digite el segundo numero: ")
	if primero=="cerrar" or segundo=="cerrar":
		break
	op=raw_input("Digite le operacion a realizar: ")
	numeros=(primero,segundo)
	mi_socket.send(op)
	servidor=eval(mi_socket.recv(1024))
	servidoroperacion=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	servidoroperacion.connect((str(servidor[0]), int(servidor[1])))
	servidoroperacion.send(str(numeros))
	dato=servidoroperacion.recv(1024)
	break

print "Resultado enviado por servidor: ", dato
print "Cerrando conexion..."
mi_socket.close()