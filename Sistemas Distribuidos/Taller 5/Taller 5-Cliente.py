import xmlrpclib

s= xmlrpclib.ServerProxy('http://localhost:5000')

while True:
	primero=raw_input("Digite el primer numero: ")
	segundo=raw_input("Digite el segundo numero: ")
	if primero=="cerrar" or segundo=="cerrar":
		break
	op=raw_input("Digite le operacion a realizar: ")
	print "El resultado es: "+ str(s.calcular(primero,segundo,op))
	break

print "Mensaje recibido..."