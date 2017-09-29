import xmlrpclib

s= xmlrpclib.ServerProxy('http://localhost:5000')

while True:
	primero=raw_input("Digite el primer numero: ")
	segundo=raw_input("Digite el segundo numero: ")
	if primero=="cerrar" or segundo=="cerrar":
		break
	op=raw_input("Digite le operacion a realizar: ")
	serveroperacion=s.redireccionar(op)
	s= xmlrpclib.ServerProxy(serveroperacion)
	print "Resultado: "+ str(s.Calcular(primero,segundo))
	break

print "Mensaje recibido..."