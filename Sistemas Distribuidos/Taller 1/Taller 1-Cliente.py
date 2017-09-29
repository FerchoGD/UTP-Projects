import socket

mi_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mi_socket.connect(("localhost",5000))


while True:
	primero=raw_input("Digite el primer numero: ")
	segundo=raw_input("Digite el segundo numero: ")
	data=(primero,segundo)
	mi_socket.send(str(data))

	if primero=="cerrar" or segundo=="cerrar":
		break

print "Cerrando conexion..."

mi_socket.close()