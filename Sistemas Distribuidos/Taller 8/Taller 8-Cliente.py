import socket

socketC=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketC.connect(("localhost",10000))

    
while True:
    
    grupo=input("Digite el nombre del grupo al que quiere acceder: ")
    print("Digite una de las siguientes opciones: \n")
    print("1.Crear\n2.Modificar\n3.Eliminar\n4.Enviar")
    Operacion=input("Digite la operacion a realizar: ")
    if Operacion=="Enviar":
        mensaje=input("Digite el mensaje a enviar: ")
        envioOp=(grupo,Operacion,mensaje)
    else:
        envioOp=(grupo,Operacion)
    socketC.send(str(envioOp).encode())
    texto=""
    data = socketC.recv(1024)
    break

print ("Resultado de la operacion enviada por servidor Intermedio: \n", data)

socketC.close()
