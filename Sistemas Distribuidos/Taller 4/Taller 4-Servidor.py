import socket
import threading
import os

socketS=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketS.bind(("localhost",10000))
socketS.listen(3)

def archivo(*args):
	datos=eval(args[0].recv(1024))
	archivo=str(datos[0])
	op=datos[1]
	ipcliente=str(args[1][0])
	

	while True:
		respuesta="nula"
		if op=="Abrir":
			respuesta="exitosa"
			f=open(archivo)
			contenido=f.read()
			args[0].send(contenido)
			print "El archivo se envio correctamente"
			f.close()
		elif op=="Borrar":
			os.remove(archivo)
			respuesta="exitosa"
			args[0].send("El archivo fue borrado exitosamente")
		elif op=="Escribir":
			texto=datos[2]
			f=open(archivo,"a")
			f.write(texto)
			f.close()
			args[0].send("Se escribio en el archivo con exito")
			respuesta="exitosa"		

		resultado=open("log.txt","a+")
		resultado.write(op+"\n")
		resultado.write(respuesta+"\n")
		resultado.write(ipcliente+"\n")
		resultado.close()
		print op+"\n"+respuesta+"\n"+ipcliente
		break
		


while True:
	cliente,addr=socketS.accept()
	threading.Thread(target=archivo,args=(cliente,addr)).start()
	

cliente.close()
socketS.close()
