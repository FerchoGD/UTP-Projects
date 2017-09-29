import socket
import threading
import os

socketS=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketS.bind(("localhost",10000))
socketS.listen(3)


listasockets=[]
def archivo(*args):
	datos=eval(args[0].recv(1024))
	nombregrupo=str(datos[0])
	op=datos[1]
	ipcliente=args[1][0]
	cliente=(args[0],ipcliente)
	listasockets.append(cliente)
	

	while True:
		if op=="Crear":
			f=open(nombregrupo,"a+")
			f.write(ipcliente+"\n")
			print ("El grupo se creo correctamente")
			msj="Grupo creado"
			args[0].send(msj.encode())
			f.close()
		elif op=="Eliminar":
			os.remove(nombregrupo)
			print("Archivo borrado con exito")
			msj="El archivo fue borrado exitosamente"
			args[0].send(msj.encode())
		elif op=="Modificar":
			f=open(nombregrupo,"r")
			lineas=f.readlines()
			print (lineas)
			f.close()
			f=open(nombregrupo,"w+")
			encontrado=False
			for linea in lineas:

				if linea!=ipcliente+"\n":
					f.write(linea)
				else:
					encontrado=True
			if encontrado:
				msj="Se borro del grupo exitosamente"
			else:
				f.write(ipcliente+"\n")
				msj="Se anadio al grupo exitosamente"

			args[0].send(msj.encode())
			f.close()
		else:
			msj=datos[2]
			f=open(nombregrupo,"r")
			lineas=f.readlines()
			f.close()
			for cli in listasockets:
				ipcliente=cli[1]
				for linea in lineas:
					if linea==ipcliente+"\n":
						cli[0].send(msj.encode())		
		break
		


while True:
	cliente,addr=socketS.accept()
	threading.Thread(target=archivo,args=(cliente,addr)).start()
	

cliente.close()
socketS.close()

