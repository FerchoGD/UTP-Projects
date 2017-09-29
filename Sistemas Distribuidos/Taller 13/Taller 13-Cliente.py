import xmlrpc.client

s=xmlrpc.client.ServerProxy('http://localhost:5000')


while True:
	
	archivo=input("Digite el nombre del archivo al que quiere acceder: ")
	Operacion=input("Digite la operacion a realizar: ")
	escritura="Nada"
	if Operacion=="Escribir":
		escritura=input("Digite el texto a escribir: ")		
		
	resultado=str(s.Ejecutar(Operacion,archivo,escritura))
	print ("Resultado: "+ resultado)		
	break
	

print ("Operacion finalizada...")