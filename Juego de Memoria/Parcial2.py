import os,sys
import pygame

BLANCO = [250,250,250]
NEGRO = [0,0,0]
ROJO = [250,0,0]
VERDE= [0,250,0]
AZUL = [0,0,250]


Ancho=900
Alto=900

class boton (pygame.sprite.Sprite):
	def __init__(self,archivo,xi,yi,nombre):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(archivo).convert_alpha()
		self.rect = self.image.get_rect()
		self.nombre = nombre
		self.rect.x = xi
		self.rect.y = yi
		self.con=3


class BotonAdivinanza (pygame.sprite.Sprite):
	def __init__(self,archivo,xi,yi):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(archivo).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = xi
		self.rect.y = yi


class Cuadro(pygame.sprite.Sprite):
	def __init__(self,archivo,xi,yi):
		pygame.sprite.Sprite.__init__(self)
		self.image  = pygame.image.load(archivo).convert_alpha()
		self.rect = self.image.get_rect()
		self.click = False
		self.rect.x = xi
		self.rect.y = yi
		self.id = 0

	def update(self,surface):
		if self.click :
			self.rect.center = pygame.mouse.get_pos()
		surface.blit(self.image,self.rect)

def DibujarMarco():
	matriz1=[[150,200],[250,200],[350,200],[450,200],[550,200],[650,200],[750,200]]
	matriz2=[[150,600],[250,600],[350,600],[450,600],[550,600],[650,600],[750,600]]
	matriz3=[[150,200],[150,300],[150,400],[150,500],[150,600]]
	matriz4=[[750,200],[750,300],[750,400],[750,500],[750,600]]
	for i in range (0,7): #Lineas Verticales
		pygame.draw.line(pantalla,AZUL,matriz1[i],matriz2[i],1)
	for i in range(0,5): #Lineas Horizontales
		pygame.draw.line(pantalla,AZUL,matriz3[i],matriz4[i],1)

def MatrizLlena(matriz):
	cont=0
	for i in range(4):
		for j in range(6):
			if matriz[i][j]!=0:
				cont+=1
	if cont==24:
		return True
	else:
		return False

def TernaIgual(terna):
	r=False
	if len(terna)==3:
		if terna[0]==terna[1] and terna[0]==terna[2] :
			r=True
	return r





if __name__ == "__main__":
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.init()
	pantalla = pygame.display.set_mode((Ancho,Alto))
	fondo=pygame.image.load('Fondo.png')
	final_image=pygame.image.load('Final.png')
	limpiar=pygame.image.load('limpiar.png')
	perdiste=pygame.image.load('Final2.png')
	final=False

	

	matrizcasillas=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
	matrizrespuestas=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
	#CajaAdivinar = boton("cajita.png",0,0,"Adivinar")
	Caja1 = boton("balon1.png",40,Alto-100,"caja1")
	Caja2 = boton("balon2.png",140,Alto-100,"caja2")
	Caja3 = boton("balon3.png",240,Alto-100,"caja3")
	Caja4 = boton("balon4.png",340,Alto-100,"caja4")
	Caja5 = boton("balon5.png",440,Alto-100,"caja5")
	Caja6 = boton("balon6.png",540,Alto-100,"caja6")
	Caja7 = boton("balon7.png",640,Alto-100,"caja7")
	Caja8 = boton("balon8.png",740,Alto-100,"caja8") # 8 imagenes para formar ternas.

	listatodos = pygame.sprite.Group()
	listabotones= pygame.sprite.Group()
	listacasillas = pygame.sprite.Group()
	lista_adivinar = pygame.sprite.Group()

	listabotones.add(Caja1)
	listabotones.add(Caja2)
	listabotones.add(Caja3)
	listabotones.add(Caja4)
	listabotones.add(Caja5)
	listabotones.add(Caja6)
	listabotones.add(Caja7)
	listabotones.add(Caja8)

	listatodos.add(Caja1)
	listatodos.add(Caja2)
	listatodos.add(Caja3)
	listatodos.add(Caja4)
	listatodos.add(Caja5)
	listatodos.add(Caja6)
	listatodos.add(Caja7)
	listatodos.add(Caja8)

	contador_respuestas=0 #Para ir comprobando que se estan formando las ternas
	ternatemporal=[] #Para ir guardando la casilla que anteriormente se abrio
	barrido=True
	Vamosbien=True


	reloj = pygame.time.Clock()

	while 1:
		segundos=pygame.time.get_ticks()/1000
		fuente = pygame.font.Font("Juego.ttf", 50)
		textiempo = fuente.render("Tiempo: " + str(segundos) + " Seg (Limite: 240) " , 0, (0, 0, 0))

		if not MatrizLlena(matrizcasillas):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:

					if event.pos[0]>=800 and event.pos[0]<=900 and event.pos[1]>=0 and event.pos[1]<=100: #Casilla de limpiar matriz, para ordenarla adecuadamente
								for casillita in listacasillas:
									listacasillas.remove(casillita)
									listatodos.remove(casillita)
									matrizcasillas=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
								for boton in listabotones:
									boton.con=3

					for boton in listabotones:
						if boton.rect.collidepoint(event.pos):
							if boton.con>0:
								if boton.nombre=="caja1" :
									CajaCasilla=Cuadro("balon1.png",0,0)
									CajaCasilla.id=1
									Caja1.con-=1

								elif boton.nombre=="caja2" :
									CajaCasilla=Cuadro("balon2.png",0,0)
									CajaCasilla.id=2
									Caja2.con-=1

								elif boton.nombre=="caja3":
									CajaCasilla=Cuadro("balon3.png",0,0)
									CajaCasilla.id=3
									Caja3.con-=1

								elif boton.nombre=="caja4":
									CajaCasilla=Cuadro("balon4.png",0,0)
									CajaCasilla.id=4
									Caja4.con-=1

								elif boton.nombre=="caja5":
									CajaCasilla=Cuadro("balon5.png",0,0)
									CajaCasilla.id=5
									Caja5.con-=1

								elif boton.nombre=="caja6":
									CajaCasilla=Cuadro("balon6.png",0,0)
									CajaCasilla.id=6
									Caja6.con-=1

								elif boton.nombre=="caja7":
									CajaCasilla=Cuadro("balon7.png",0,0)
									CajaCasilla.id=7
									Caja7.con-=1

								elif boton.nombre=="caja8":
									CajaCasilla=Cuadro("balon8.png",0,0)
									CajaCasilla.id=8
									Caja8.con-=1


							col = True
							while col:
								col = False
								colision = pygame.sprite.spritecollide(CajaCasilla,listacasillas,False)
								for bl in colision:
									if CajaCasilla.id != bl.id:
										CajaCasilla.rect.left = bl.rect.right
										col = True
							listatodos.add(CajaCasilla)
							listacasillas.add(CajaCasilla)

					for casilla in listacasillas:
						if casilla.rect.collidepoint(event.pos):#condiciones por si se posiciona sobre una casilla en especifico
							if casilla.rect.x>=150 and casilla.rect.x<=250 and casilla.rect.y>=200 and casilla.rect.y<=300 and matrizcasillas[0][1]!=casilla.id and matrizcasillas[1][0]!=casilla.id:
								casilla.rect.center=[200,250]
								px=0
								py=0
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=251 and casilla.rect.x<=350 and casilla.rect.y>=200 and casilla.rect.y<=300 and matrizcasillas[0][0]!=casilla.id and matrizcasillas[1][1]!=casilla.id and matrizcasillas[0][2]!=casilla.id:
								casilla.rect.center=[300,250]
								px=0
								py=1
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=351 and casilla.rect.x<=450 and casilla.rect.y>=200 and casilla.rect.y<=300 and matrizcasillas[0][1]!=casilla.id and matrizcasillas[1][2]!=casilla.id and matrizcasillas[0][3]!=casilla.id:
								casilla.rect.center=[400,250]
								px=0
								py=2
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=451 and casilla.rect.x<=550 and casilla.rect.y>=200 and casilla.rect.y<=300 and matrizcasillas[0][2]!=casilla.id and matrizcasillas[1][3]!=casilla.id and matrizcasillas[0][4]!=casilla.id:
								casilla.rect.center=[500,250]
								px=0
								py=3
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=551 and casilla.rect.x<=650 and casilla.rect.y>=200 and casilla.rect.y<=300 and matrizcasillas[0][3]!=casilla.id and matrizcasillas[1][4]!=casilla.id and matrizcasillas[0][5]!=casilla.id:
								casilla.rect.center=[600,250]
								px=0
								py=4
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=651 and casilla.rect.x<=750 and casilla.rect.y>=200 and casilla.rect.y<=300 and matrizcasillas[0][4]!=casilla.id and matrizcasillas[1][5]!=casilla.id:
								casilla.rect.center=[700,250]
								px=0
								py=5
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=150 and casilla.rect.x<=250 and casilla.rect.y>=301 and casilla.rect.y<=400 and matrizcasillas[0][0]!=casilla.id and matrizcasillas[1][1]!=casilla.id and matrizcasillas[2][0]!=casilla.id:
								casilla.rect.center=[200,350]
								px=1
								py=0
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=251 and casilla.rect.x<=350 and casilla.rect.y>=301 and casilla.rect.y<=400 and matrizcasillas[0][1]!=casilla.id and matrizcasillas[1][0]!=casilla.id and matrizcasillas[2][1]!=casilla.id and matrizcasillas[1][2]!=casilla.id:
								casilla.rect.center=[300,350]
								px=1
								py=1
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=351 and casilla.rect.x<=450 and casilla.rect.y>=301 and casilla.rect.y<=400 and matrizcasillas[0][2]!=casilla.id and matrizcasillas[1][1]!=casilla.id and matrizcasillas[2][2]!=casilla.id and matrizcasillas[1][3]!=casilla.id:
								casilla.rect.center=[400,350]
								px=1
								py=2
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=451 and casilla.rect.x<=550 and casilla.rect.y>=301 and casilla.rect.y<=400 and matrizcasillas[0][3]!=casilla.id and matrizcasillas[1][2]!=casilla.id and matrizcasillas[2][3]!=casilla.id and matrizcasillas[1][4]!=casilla.id:
								casilla.rect.center=[500,350]
								px=1
								py=3
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=551 and casilla.rect.x<=650 and casilla.rect.y>=301 and casilla.rect.y<=400 and matrizcasillas[0][4]!=casilla.id and matrizcasillas[1][3]!=casilla.id and matrizcasillas[1][5]!=casilla.id and matrizcasillas[2][4]!=casilla.id:
								casilla.rect.center=[600,350]
								px=1
								py=4
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=651 and casilla.rect.x<=750 and casilla.rect.y>=301 and casilla.rect.y<=400 and matrizcasillas[0][5]!=casilla.id and matrizcasillas[1][4]!=casilla.id and matrizcasillas[2][5]!=casilla.id:
								casilla.rect.center=[700,350]
								px=1
								py=5
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=150 and casilla.rect.x<=250 and casilla.rect.y>=401 and casilla.rect.y<=500 and matrizcasillas[1][0]!=casilla.id and matrizcasillas[2][1]!=casilla.id and matrizcasillas[3][0]!=casilla.id:
								casilla.rect.center=[200,450]
								px=2
								py=0
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=251 and casilla.rect.x<=350 and casilla.rect.y>=401 and casilla.rect.y<=500 and matrizcasillas[2][0]!=casilla.id and matrizcasillas[1][1]!=casilla.id and matrizcasillas[3][1]!=casilla.id and matrizcasillas[2][2]!=casilla.id:
								casilla.rect.center=[300,450]
								px=2
								py=1
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=351 and casilla.rect.x<=450 and casilla.rect.y>=401 and casilla.rect.y<=500 and matrizcasillas[2][1]!=casilla.id and matrizcasillas[1][2]!=casilla.id and matrizcasillas[3][2]!=casilla.id and matrizcasillas[2][3]!=casilla.id:
								casilla.rect.center=[400,450]
								px=2
								py=2
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=451 and casilla.rect.x<=550 and casilla.rect.y>=401 and casilla.rect.y<=500 and matrizcasillas[2][2]!=casilla.id and matrizcasillas[3][3]!=casilla.id and matrizcasillas[1][3]!=casilla.id and matrizcasillas[2][4]!=casilla.id:
								casilla.rect.center=[500,450]
								px=2
								py=3
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=551 and casilla.rect.x<=650 and casilla.rect.y>=401 and casilla.rect.y<=500 and matrizcasillas[2][3]!=casilla.id and matrizcasillas[1][4]!=casilla.id and matrizcasillas[3][4]!=casilla.id and matrizcasillas[2][5]!=casilla.id:
								casilla.rect.center=[600,450]
								px=2
								py=4
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=651 and casilla.rect.x<=750 and casilla.rect.y>=401 and casilla.rect.y<=500 and matrizcasillas[2][4]!=casilla.id and matrizcasillas[1][5]!=casilla.id and matrizcasillas[3][5]!=casilla.id:
								casilla.rect.center=[700,450]
								px=2
								py=5
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=150 and casilla.rect.x<=250 and casilla.rect.y>=501 and casilla.rect.y<=600 and matrizcasillas[3][1]!=casilla.id and matrizcasillas[2][0]!=casilla.id:
								casilla.rect.center=[200,550]
								px=3
								py=0
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=251 and casilla.rect.x<=350 and casilla.rect.y>=501 and casilla.rect.y<=600 and matrizcasillas[2][1]!=casilla.id and matrizcasillas[3][0]!=casilla.id and matrizcasillas[3][2]!=casilla.id:
								casilla.rect.center=[300,550]
								px=3
								py=1
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=351 and casilla.rect.x<=450 and casilla.rect.y>=501 and casilla.rect.y<=600 and matrizcasillas[3][1]!=casilla.id and matrizcasillas[2][2]!=casilla.id and matrizcasillas[3][3]!=casilla.id:
								casilla.rect.center=[400,550]
								px=3
								py=2
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=451 and casilla.rect.x<=550 and casilla.rect.y>=501 and casilla.rect.y<=600 and matrizcasillas[3][2]!=casilla.id and matrizcasillas[2][3]!=casilla.id and matrizcasillas[3][4]!=casilla.id:
								casilla.rect.center=[500,550]
								px=3
								py=3
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=551 and casilla.rect.x<=650 and casilla.rect.y>=501 and casilla.rect.y<=600 and matrizcasillas[3][3]!=casilla.id and matrizcasillas[2][4]!=casilla.id and matrizcasillas[3][5]!=casilla.id:
								casilla.rect.center=[600,550]
								px=3
								py=4
								matrizcasillas[px][py]=casilla.id

							elif casilla.rect.x>=651 and casilla.rect.x<=750 and casilla.rect.y>=501 and casilla.rect.y<=600 and matrizcasillas[2][5]!=casilla.id and matrizcasillas[3][4]!=casilla.id:
								casilla.rect.center=[700,550]
								px=3
								py=5
								matrizcasillas[px][py]=casilla.id

							else :
								casilla.click=True
								casilla.update(pantalla)



				elif event.type == pygame.MOUSEBUTTONUP:
					for casilla in listacasillas:
						casilla.update(pantalla)
						casilla.click = False
						col = True

						while col:
							col = False
							colision =pygame.sprite.spritecollide(casilla,listacasillas,False)
							for e in colision:
								if casilla.id != e.id:
									casilla.rect.left = e.rect.right
									col = True


				elif event.type == pygame.QUIT:
						print (matrizcasillas)
						pygame.quit(); sys.exit()

		if MatrizLlena(matrizcasillas):

			if barrido:
				for casilla in listacasillas:
					listatodos.remove(casilla)
				barrido=False

			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:

					if contador_respuestas<3:

						if pygame.mouse.get_pos()[0]>=150 and pygame.mouse.get_pos()[0]<=250 and pygame.mouse.get_pos()[1]>=200 and pygame.mouse.get_pos()[1]<=300:
							if matrizcasillas[0][0]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",150+10,200+10)
								matrizrespuestas[0][0]=1
								ternatemporal.append(1)

							elif matrizcasillas[0][0]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",150+10,200+10)
								matrizrespuestas[0][0]=2
								ternatemporal.append(2)

							elif matrizcasillas[0][0]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",150+10,200+10)
								matrizrespuestas[0][0]=3
								ternatemporal.append(3)

							elif matrizcasillas[0][0]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",150+10,200+10)
								matrizrespuestas[0][0]=4
								ternatemporal.append(4)

							elif matrizcasillas[0][0]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",150+10,200+10)
								matrizrespuestas[0][0]=5
								ternatemporal.append(5)

							elif matrizcasillas[0][0]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",150+10,200+10)
								matrizrespuestas[0][0]=6
								ternatemporal.append(6)

							elif matrizcasillas[0][0]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",150+10,200+10)
								matrizrespuestas[0][0]=7
								ternatemporal.append(7)

							elif matrizcasillas[0][0]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",150+10,200+10)
								matrizrespuestas[0][0]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=251 and pygame.mouse.get_pos()[0]<=350 and pygame.mouse.get_pos()[1]>=200 and pygame.mouse.get_pos()[1]<=300:
							if matrizcasillas[0][1]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",250+10,200+10)
								matrizrespuestas[0][1]=1
								ternatemporal.append(1)

							elif matrizcasillas[0][1]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",250+10,200+10)
								matrizrespuestas[0][1]=2
								ternatemporal.append(2)

							elif matrizcasillas[0][1]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",250+10,200+10)
								matrizrespuestas[0][1]=3
								ternatemporal.append(3)

							elif matrizcasillas[0][1]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",250+10,200+10)
								matrizrespuestas[0][1]=4
								ternatemporal.append(4)

							elif matrizcasillas[0][1]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",250+10,200+10)
								matrizrespuestas[0][1]=5
								ternatemporal.append(5)

							elif matrizcasillas[0][1]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",250+10,200+10)
								matrizrespuestas[0][1]=6
								ternatemporal.append(6)

							elif matrizcasillas[0][1]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",250+10,200+10)
								matrizrespuestas[0][1]=7
								ternatemporal.append(7)

							elif matrizcasillas[0][1]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",250+10,200+10)
								matrizrespuestas[0][1]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=351 and pygame.mouse.get_pos()[0]<=450 and pygame.mouse.get_pos()[1]>=200 and pygame.mouse.get_pos()[1]<=300:
							if matrizcasillas[0][2]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",350+10,200+10)
								matrizrespuestas[0][2]=1
								ternatemporal.append(1)

							elif matrizcasillas[0][2]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",350+10,200+10)
								matrizrespuestas[0][2]=2
								ternatemporal.append(2)

							elif matrizcasillas[0][2]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",350+10,200+10)
								matrizrespuestas[0][2]=3
								ternatemporal.append(3)

							elif matrizcasillas[0][2]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",350+10,200+10)
								matrizrespuestas[0][2]=4
								ternatemporal.append(4)

							elif matrizcasillas[0][2]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",350+10,200+10)
								matrizrespuestas[0][2]=5
								ternatemporal.append(5)

							elif matrizcasillas[0][2]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",350+10,200+10)
								matrizrespuestas[0][2]=6
								ternatemporal.append(6)

							elif matrizcasillas[0][2]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",350+10,200+10)
								matrizrespuestas[0][2]=7
								ternatemporal.append(7)

							elif matrizcasillas[0][2]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",350+10,200+10)
								matrizrespuestas[0][2]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=451 and pygame.mouse.get_pos()[0]<=550 and pygame.mouse.get_pos()[1]>=200 and pygame.mouse.get_pos()[1]<=300:
							if matrizcasillas[0][3]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",450+10,200+10)
								matrizrespuestas[0][3]=1
								ternatemporal.append(1)

							elif matrizcasillas[0][3]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",450+10,200+10)
								matrizrespuestas[0][3]=2
								ternatemporal.append(2)

							elif matrizcasillas[0][3]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",450+10,200+10)
								matrizrespuestas[0][3]=3
								ternatemporal.append(3)

							elif matrizcasillas[0][3]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",450+10,200+10)
								matrizrespuestas[0][3]=4
								ternatemporal.append(4)

							elif matrizcasillas[0][3]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",450+10,200+10)
								matrizrespuestas[0][3]=5
								ternatemporal.append(5)

							elif matrizcasillas[0][3]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",450+10,200+10)
								matrizrespuestas[0][3]=6
								ternatemporal.append(6)

							elif matrizcasillas[0][3]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",450+10,200+10)
								matrizrespuestas[0][3]=7
								ternatemporal.append(7)

							elif matrizcasillas[0][3]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",450+10,200+10)
								matrizrespuestas[0][3]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=551 and pygame.mouse.get_pos()[0]<=650 and pygame.mouse.get_pos()[1]>=200 and pygame.mouse.get_pos()[1]<=300:
							if matrizcasillas[0][4]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",550+10,200+10)
								matrizrespuestas[0][4]=1
								ternatemporal.append(1)

							elif matrizcasillas[0][4]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",550+10,200+10)
								matrizrespuestas[0][4]=2
								ternatemporal.append(2)

							elif matrizcasillas[0][4]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",550+10,200+10)
								matrizrespuestas[0][4]=3
								ternatemporal.append(3)

							elif matrizcasillas[0][4]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",550+10,200+10)
								matrizrespuestas[0][0]=4
								ternatemporal.append(4)

							elif matrizcasillas[0][4]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",550+10,200+10)
								matrizrespuestas[0][4]=5
								ternatemporal.append(5)

							elif matrizcasillas[0][4]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",550+10,200+10)
								matrizrespuestas[0][4]=6
								ternatemporal.append(6)

							elif matrizcasillas[0][4]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",550+10,200+10)
								matrizrespuestas[0][4]=7
								ternatemporal.append(7)

							elif matrizcasillas[0][4]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",550+10,200+10)
								matrizrespuestas[0][4]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=651 and pygame.mouse.get_pos()[0]<=750 and pygame.mouse.get_pos()[1]>=200 and pygame.mouse.get_pos()[1]<=300:
							if matrizcasillas[0][5]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",650+10,200+10)
								matrizrespuestas[0][5]=1
								ternatemporal.append(1)

							elif matrizcasillas[0][5]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",650+10,200+10)
								matrizrespuestas[0][5]=2
								ternatemporal.append(2)

							elif matrizcasillas[0][5]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",650+10,200+10)
								matrizrespuestas[0][5]=3
								ternatemporal.append(3)

							elif matrizcasillas[0][5]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",650+10,200+10)
								matrizrespuestas[0][5]=4
								ternatemporal.append(4)

							elif matrizcasillas[0][5]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",650+10,200+10)
								matrizrespuestas[0][5]=5
								ternatemporal.append(5)

							elif matrizcasillas[0][5]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",650+10,200+10)
								matrizrespuestas[0][5]=6
								ternatemporal.append(6)

							elif matrizcasillas[0][5]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",650+10,200+10)
								matrizrespuestas[0][5]=7
								ternatemporal.append(7)

							elif matrizcasillas[0][5]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",650+10,200+10)
								matrizrespuestas[0][5]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=150 and pygame.mouse.get_pos()[0]<=250 and pygame.mouse.get_pos()[1]>=301 and pygame.mouse.get_pos()[1]<=400:
							if matrizcasillas[1][0]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",150+10,300+10)
								matrizrespuestas[1][0]=1
								ternatemporal.append(1)

							elif matrizcasillas[1][0]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",150+10,300+10)
								matrizrespuestas[1][0]=2
								ternatemporal.append(2)

							elif matrizcasillas[1][0]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",150+10,300+10)
								matrizrespuestas[1][0]=3
								ternatemporal.append(3)

							elif matrizcasillas[1][0]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",150+10,300+10)
								matrizrespuestas[1][0]=4
								ternatemporal.append(4)

							elif matrizcasillas[1][0]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",150+10,300+10)
								matrizrespuestas[1][0]=5
								ternatemporal.append(5)

							elif matrizcasillas[1][0]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",150+10,300+10)
								matrizrespuestas[1][0]=6
								ternatemporal.append(6)

							elif matrizcasillas[1][0]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",150+10,300+10)
								matrizrespuestas[1][0]=7
								ternatemporal.append(7)

							elif matrizcasillas[1][0]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",150+10,300+10)
								matrizrespuestas[1][0]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=251 and pygame.mouse.get_pos()[0]<=350 and pygame.mouse.get_pos()[1]>=301 and pygame.mouse.get_pos()[1]<=400:
							if matrizcasillas[1][1]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",250+10,300+10)
								matrizrespuestas[1][1]=1
								ternatemporal.append(1)

							elif matrizcasillas[1][1]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",250+10,300+10)
								matrizrespuestas[1][1]=2
								ternatemporal.append(2)

							elif matrizcasillas[1][1]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",250+10,300+10)
								matrizrespuestas[1][1]=3
								ternatemporal.append(3)

							elif matrizcasillas[1][1]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",250+10,300+10)
								matrizrespuestas[1][1]=4
								ternatemporal.append(4)

							elif matrizcasillas[1][1]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",250+10,300+10)
								matrizrespuestas[1][1]=5
								ternatemporal.append(5)

							elif matrizcasillas[1][1]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",250+10,300+10)
								matrizrespuestas[1][1]=6
								ternatemporal.append(6)

							elif matrizcasillas[1][1]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",250+10,300+10)
								matrizrespuestas[1][1]=7
								ternatemporal.append(7)

							elif matrizcasillas[1][1]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",250+10,300+10)
								matrizrespuestas[1][1]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=351 and pygame.mouse.get_pos()[0]<=450 and pygame.mouse.get_pos()[1]>=301 and pygame.mouse.get_pos()[1]<=400:
							if matrizcasillas[1][2]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",350+10,300+10)
								matrizrespuestas[1][2]=1
								ternatemporal.append(1)

							elif matrizcasillas[1][2]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",350+10,300+10)
								matrizrespuestas[1][2]=2
								ternatemporal.append(2)

							elif matrizcasillas[1][2]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",350+10,300+10)
								matrizrespuestas[1][2]=3
								ternatemporal.append(3)

							elif matrizcasillas[1][2]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",350+10,300+10)
								matrizrespuestas[1][2]=4
								ternatemporal.append(4)

							elif matrizcasillas[1][2]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",350+10,300+10)
								matrizrespuestas[1][2]=5
								ternatemporal.append(5)

							elif matrizcasillas[1][2]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",350+10,300+10)
								matrizrespuestas[1][2]=6
								ternatemporal.append(6)

							elif matrizcasillas[1][2]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",350+10,300+10)
								matrizrespuestas[1][2]=7
								ternatemporal.append(7)

							elif matrizcasillas[1][2]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",350+10,300+10)
								matrizrespuestas[1][2]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=451 and pygame.mouse.get_pos()[0]<=550 and pygame.mouse.get_pos()[1]>=301 and pygame.mouse.get_pos()[1]<=400:
							if matrizcasillas[1][3]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",450+10,300+10)
								matrizrespuestas[1][3]=1
								ternatemporal.append(1)

							elif matrizcasillas[1][3]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",450+10,300+10)
								matrizrespuestas[1][3]=2
								ternatemporal.append(2)

							elif matrizcasillas[1][3]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",450+10,300+10)
								matrizrespuestas[1][3]=3
								ternatemporal.append(3)

							elif matrizcasillas[1][3]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",450+10,300+10)
								matrizrespuestas[1][3]=4
								ternatemporal.append(4)

							elif matrizcasillas[1][3]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",450+10,300+10)
								matrizrespuestas[1][3]=5
								ternatemporal.append(5)

							elif matrizcasillas[1][3]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",450+10,300+10)
								matrizrespuestas[1][3]=6
								ternatemporal.append(6)

							elif matrizcasillas[1][3]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",450+10,300+10)
								matrizrespuestas[1][3]=7
								ternatemporal.append(7)

							elif matrizcasillas[1][3]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",450+10,300+10)
								matrizrespuestas[1][3]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=551 and pygame.mouse.get_pos()[0]<=650 and pygame.mouse.get_pos()[1]>=301 and pygame.mouse.get_pos()[1]<=400:
							if matrizcasillas[1][4]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",550+10,300+10)
								matrizrespuestas[1][4]=1
								ternatemporal.append(1)

							elif matrizcasillas[1][4]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",550+10,300+10)
								matrizrespuestas[1][4]=2
								ternatemporal.append(2)

							elif matrizcasillas[1][4]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",550+10,300+10)
								matrizrespuestas[1][4]=3
								ternatemporal.append(3)

							elif matrizcasillas[1][4]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",550+10,300+10)
								matrizrespuestas[1][4]=4
								ternatemporal.append(4)

							elif matrizcasillas[1][4]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",550+10,300+10)
								matrizrespuestas[1][4]=5
								ternatemporal.append(5)

							elif matrizcasillas[1][4]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",550+10,300+10)
								matrizrespuestas[1][4]=6
								ternatemporal.append(6)

							elif matrizcasillas[1][4]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",550+10,300+10)
								matrizrespuestas[1][4]=7
								ternatemporal.append(7)

							elif matrizcasillas[1][4]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",550+10,300+10)
								matrizrespuestas[1][4]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=651 and pygame.mouse.get_pos()[0]<=750 and pygame.mouse.get_pos()[1]>=301 and pygame.mouse.get_pos()[1]<=400:
							if matrizcasillas[1][5]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",650+10,300+10)
								matrizrespuestas[1][5]=1
								ternatemporal.append(1)

							elif matrizcasillas[1][5]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",650+10,300+10)
								matrizrespuestas[1][5]=2
								ternatemporal.append(2)

							elif matrizcasillas[1][5]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",650+10,300+10)
								matrizrespuestas[1][5]=3
								ternatemporal.append(3)

							elif matrizcasillas[1][5]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",650+10,300+10)
								matrizrespuestas[1][5]=4
								ternatemporal.append(4)

							elif matrizcasillas[1][5]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",650+10,300+10)
								matrizrespuestas[1][5]=5
								ternatemporal.append(5)

							elif matrizcasillas[1][5]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",650+10,300+10)
								matrizrespuestas[1][5]=6
								ternatemporal.append(6)

							elif matrizcasillas[1][5]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",650+10,300+10)
								matrizrespuestas[1][5]=7
								ternatemporal.append(7)

							elif matrizcasillas[1][5]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",650+10,300+10)
								matrizrespuestas[1][5]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=150 and pygame.mouse.get_pos()[0]<=250 and pygame.mouse.get_pos()[1]>=401 and pygame.mouse.get_pos()[1]<=500:
							if matrizcasillas[2][0]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",150+10,400+10)
								matrizrespuestas[2][0]=1
								ternatemporal.append(1)

							elif matrizcasillas[2][0]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",150+10,400+10)
								matrizrespuestas[2][0]=2
								ternatemporal.append(2)

							elif matrizcasillas[2][0]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",150+10,400+10)
								matrizrespuestas[2][0]=3
								ternatemporal.append(3)

							elif matrizcasillas[2][0]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",150+10,400+10)
								matrizrespuestas[2][0]=4
								ternatemporal.append(4)

							elif matrizcasillas[2][0]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",150+10,400+10)
								matrizrespuestas[2][0]=5
								ternatemporal.append(5)

							elif matrizcasillas[2][0]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",150+10,400+10)
								matrizrespuestas[2][0]=6
								ternatemporal.append(6)

							elif matrizcasillas[2][0]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",150+10,400+10)
								matrizrespuestas[2][0]=7
								ternatemporal.append(7)

							elif matrizcasillas[2][0]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",150+10,400+10)
								matrizrespuestas[2][0]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=251 and pygame.mouse.get_pos()[0]<=350 and pygame.mouse.get_pos()[1]>=401 and pygame.mouse.get_pos()[1]<=500:
							if matrizcasillas[2][0]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",250+10,400+10)
								matrizrespuestas[2][1]=1
								ternatemporal.append(1)

							elif matrizcasillas[2][1]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",250+10,400+10)
								matrizrespuestas[2][1]=2
								ternatemporal.append(2)

							elif matrizcasillas[2][1]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",250+10,400+10)
								matrizrespuestas[2][1]=3
								ternatemporal.append(3)

							elif matrizcasillas[2][1]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",250+10,400+10)
								matrizrespuestas[2][1]=4
								ternatemporal.append(4)

							elif matrizcasillas[2][1]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",250+10,400+10)
								matrizrespuestas[2][1]=5
								ternatemporal.append(5)

							elif matrizcasillas[2][1]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",250+10,400+10)
								matrizrespuestas[2][1]=6
								ternatemporal.append(6)

							elif matrizcasillas[2][1]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",250+10,400+10)
								matrizrespuestas[2][1]=7
								ternatemporal.append(7)

							elif matrizcasillas[2][1]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",250+10,400+10)
								matrizrespuestas[2][1]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=351 and pygame.mouse.get_pos()[0]<=450 and pygame.mouse.get_pos()[1]>=401 and pygame.mouse.get_pos()[1]<=500:
							if matrizcasillas[2][2]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",350+10,400+10)
								matrizrespuestas[2][2]=1
								ternatemporal.append(1)

							elif matrizcasillas[2][2]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",350+10,400+10)
								matrizrespuestas[2][2]=2
								ternatemporal.append(2)

							elif matrizcasillas[2][2]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",350+10,400+10)
								matrizrespuestas[2][2]=3
								ternatemporal.append(3)

							elif matrizcasillas[2][2]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",350+10,400+10)
								matrizrespuestas[2][2]=4
								ternatemporal.append(4)

							elif matrizcasillas[2][2]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",350+10,400+10)
								matrizrespuestas[2][2]=5
								ternatemporal.append(5)

							elif matrizcasillas[2][2]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",350+10,400+10)
								matrizrespuestas[2][2]=6
								ternatemporal.append(6)

							elif matrizcasillas[2][2]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",350+10,400+10)
								matrizrespuestas[2][2]=7
								ternatemporal.append(7)

							elif matrizcasillas[2][2]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",350+10,400+10)
								matrizrespuestas[2][2]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=451 and pygame.mouse.get_pos()[0]<=550 and pygame.mouse.get_pos()[1]>=401 and pygame.mouse.get_pos()[1]<=500:
							if matrizcasillas[2][3]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",450+10,400+10)
								matrizrespuestas[2][3]=1
								ternatemporal.append(1)

							elif matrizcasillas[2][3]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",450+10,400+10)
								matrizrespuestas[2][3]=2
								ternatemporal.append(2)

							elif matrizcasillas[2][3]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",450+10,400+10)
								matrizrespuestas[2][3]=3
								ternatemporal.append(3)

							elif matrizcasillas[2][3]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",450+10,400+10)
								matrizrespuestas[2][3]=4
								ternatemporal.append(4)

							elif matrizcasillas[2][3]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",450+10,400+10)
								matrizrespuestas[2][3]=5
								ternatemporal.append(5)

							elif matrizcasillas[2][3]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",450+10,400+10)
								matrizrespuestas[2][3]=6
								ternatemporal.append(6)

							elif matrizcasillas[2][3]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",450+10,400+10)
								matrizrespuestas[2][3]=7
								ternatemporal.append(7)

							elif matrizcasillas[2][3]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",450+10,400+10)
								matrizrespuestas[2][3]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=551 and pygame.mouse.get_pos()[0]<=650 and pygame.mouse.get_pos()[1]>=401 and pygame.mouse.get_pos()[1]<=500:
							if matrizcasillas[2][4]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",550+10,400+10)
								matrizrespuestas[2][4]=1
								ternatemporal.append(1)

							elif matrizcasillas[2][4]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",550+10,400+10)
								matrizrespuestas[2][4]=2
								ternatemporal.append(2)

							elif matrizcasillas[2][4]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",550+10,400+10)
								matrizrespuestas[2][4]=3
								ternatemporal.append(3)

							elif matrizcasillas[2][4]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",550+10,400+10)
								matrizrespuestas[2][4]=4
								ternatemporal.append(4)

							elif matrizcasillas[2][4]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",550+10,400+10)
								matrizrespuestas[2][4]=5
								ternatemporal.append(5)

							elif matrizcasillas[2][4]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",550+10,400+10)
								matrizrespuestas[2][4]=6
								ternatemporal.append(6)

							elif matrizcasillas[2][4]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",550+10,400+10)
								matrizrespuestas[2][4]=7
								ternatemporal.append(7)

							elif matrizcasillas[2][4]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",550+10,400+10)
								matrizrespuestas[2][4]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=651 and pygame.mouse.get_pos()[0]<=750 and pygame.mouse.get_pos()[1]>=401 and pygame.mouse.get_pos()[1]<=500:
							if matrizcasillas[2][5]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",650+10,400+10)
								matrizrespuestas[2][5]=1
								ternatemporal.append(1)

							elif matrizcasillas[2][5]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",650+10,400+10)
								matrizrespuestas[2][5]=2
								ternatemporal.append(2)

							elif matrizcasillas[2][5]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",650+10,400+10)
								matrizrespuestas[2][5]=3
								ternatemporal.append(3)

							elif matrizcasillas[2][5]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",650+10,400+10)
								matrizrespuestas[2][5]=4
								ternatemporal.append(4)

							elif matrizcasillas[2][5]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",650+10,400+10)
								matrizrespuestas[2][5]=5
								ternatemporal.append(5)

							elif matrizcasillas[2][5]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",650+10,400+10)
								matrizrespuestas[2][5]=6
								ternatemporal.append(6)

							elif matrizcasillas[2][5]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",650+10,400+10)
								matrizrespuestas[2][5]=7
								ternatemporal.append(7)

							elif matrizcasillas[2][5]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",650+10,400+10)
								matrizrespuestas[2][5]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=150 and pygame.mouse.get_pos()[0]<=250 and pygame.mouse.get_pos()[1]>=501 and pygame.mouse.get_pos()[1]<=600:
							if matrizcasillas[3][0]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",150+10,500+10)
								matrizrespuestas[3][0]=1
								ternatemporal.append(1)

							elif matrizcasillas[3][0]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",150+10,500+10)
								matrizrespuestas[3][0]=2
								ternatemporal.append(2)

							elif matrizcasillas[3][0]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",150+10,500+10)
								matrizrespuestas[3][0]=3
								ternatemporal.append(3)

							elif matrizcasillas[3][0]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",150+10,500+10)
								matrizrespuestas[3][0]=4
								ternatemporal.append(4)

							elif matrizcasillas[3][0]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",150+10,500+10)
								matrizrespuestas[3][0]=5
								ternatemporal.append(5)

							elif matrizcasillas[3][0]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",150+10,500+10)
								matrizrespuestas[3][0]=6
								ternatemporal.append(6)

							elif matrizcasillas[3][0]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",150+10,500+10)
								matrizrespuestas[3][0]=7
								ternatemporal.append(7)

							elif matrizcasillas[3][0]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",150+10,500+10)
								matrizrespuestas[3][0]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=251 and pygame.mouse.get_pos()[0]<=350 and pygame.mouse.get_pos()[1]>=501 and pygame.mouse.get_pos()[1]<=600:
							if matrizcasillas[3][1]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",250+10,500+10)
								matrizrespuestas[3][1]=1
								ternatemporal.append(1)

							elif matrizcasillas[3][1]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",250+10,500+10)
								matrizrespuestas[3][1]=2
								ternatemporal.append(2)

							elif matrizcasillas[3][1]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",250+10,500+10)
								matrizrespuestas[3][1]=3
								ternatemporal.append(3)

							elif matrizcasillas[3][1]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",250+10,500+10)
								matrizrespuestas[3][1]=4
								ternatemporal.append(4)

							elif matrizcasillas[3][1]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",250+10,500+10)
								matrizrespuestas[3][1]=5
								ternatemporal.append(5)

							elif matrizcasillas[3][1]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",250+10,500+10)
								matrizrespuestas[3][1]=6
								ternatemporal.append(6)

							elif matrizcasillas[3][1]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",250+10,500+10)
								matrizrespuestas[3][1]=7
								ternatemporal.append(7)

							elif matrizcasillas[3][1]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",250+10,500+10)
								matrizrespuestas[3][1]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=351 and pygame.mouse.get_pos()[0]<=450 and pygame.mouse.get_pos()[1]>=501 and pygame.mouse.get_pos()[1]<=600:
							if matrizcasillas[3][2]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",350+10,500+10)
								matrizrespuestas[3][2]=1
								ternatemporal.append(1)

							elif matrizcasillas[3][2]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",350+10,500+10)
								matrizrespuestas[3][2]=2
								ternatemporal.append(2)

							elif matrizcasillas[3][2]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",350+10,500+10)
								matrizrespuestas[3][2]=3
								ternatemporal.append(3)

							elif matrizcasillas[3][2]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",350+10,500+10)
								matrizrespuestas[3][2]=4
								ternatemporal.append(4)

							elif matrizcasillas[3][2]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",350+10,500+10)
								matrizrespuestas[3][2]=5
								ternatemporal.append(5)

							elif matrizcasillas[3][2]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",350+10,500+10)
								matrizrespuestas[3][2]=6
								ternatemporal.append(6)

							elif matrizcasillas[3][2]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",350+10,500+10)
								matrizrespuestas[3][2]=7
								ternatemporal.append(7)

							elif matrizcasillas[3][2]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",350+10,500+10)
								matrizrespuestas[3][2]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=451 and pygame.mouse.get_pos()[0]<=550 and pygame.mouse.get_pos()[1]>=501 and pygame.mouse.get_pos()[1]<=600:
							if matrizcasillas[3][3]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",450+10,500+10)
								matrizrespuestas[3][3]=1
								ternatemporal.append(1)

							elif matrizcasillas[3][3]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",450+10,500+10)
								matrizrespuestas[3][3]=2
								ternatemporal.append(2)

							elif matrizcasillas[3][3]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",450+10,500+10)
								matrizrespuestas[3][3]=3
								ternatemporal.append(3)

							elif matrizcasillas[3][3]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",450+10,500+10)
								matrizrespuestas[3][3]=4
								ternatemporal.append(4)

							elif matrizcasillas[3][3]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",450+10,500+10)
								matrizrespuestas[3][3]=5
								ternatemporal.append(5)

							elif matrizcasillas[3][3]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",450+10,500+10)
								matrizrespuestas[3][3]=6
								ternatemporal.append(6)

							elif matrizcasillas[3][3]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",450+10,500+10)
								matrizrespuestas[3][3]=7
								ternatemporal.append(7)

							elif matrizcasillas[3][3]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",450+10,500+10)
								matrizrespuestas[3][3]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=551 and pygame.mouse.get_pos()[0]<=650 and pygame.mouse.get_pos()[1]>=501 and pygame.mouse.get_pos()[1]<=600:
							if matrizcasillas[3][4]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",550+10,500+10)
								matrizrespuestas[3][4]=1
								ternatemporal.append(1)

							elif matrizcasillas[3][4]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",550+10,500+10)
								matrizrespuestas[3][4]=2
								ternatemporal.append(2)

							elif matrizcasillas[3][4]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",550+10,500+10)
								matrizrespuestas[3][4]=3
								ternatemporal.append(3)

							elif matrizcasillas[3][4]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",550+10,500+10)
								matrizrespuestas[3][4]=4
								ternatemporal.append(4)

							elif matrizcasillas[3][4]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",550+10,500+10)
								matrizrespuestas[3][4]=5
								ternatemporal.append(5)

							elif matrizcasillas[3][4]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",550+10,500+10)
								matrizrespuestas[3][4]=6
								ternatemporal.append(6)

							elif matrizcasillas[3][4]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",550+10,500+10)
								matrizrespuestas[3][4]=7
								ternatemporal.append(7)

							elif matrizcasillas[3][4]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",550+10,500+10)
								matrizrespuestas[3][4]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

						elif pygame.mouse.get_pos()[0]>=651 and pygame.mouse.get_pos()[0]<=750 and pygame.mouse.get_pos()[1]>=501 and pygame.mouse.get_pos()[1]<=600:
							if matrizcasillas[3][5]==1:
								CajaAdivinanza=BotonAdivinanza("balon1.png",650+10,500+10)
								matrizrespuestas[3][5]=1
								ternatemporal.append(1)

							elif matrizcasillas[3][5]==2:
								CajaAdivinanza=BotonAdivinanza("balon2.png",650+10,500+10)
								matrizrespuestas[3][5]=2
								ternatemporal.append(2)

							elif matrizcasillas[3][5]==3:
								CajaAdivinanza=BotonAdivinanza("balon3.png",650+10,500+10)
								matrizrespuestas[3][5]=3
								ternatemporal.append(3)

							elif matrizcasillas[3][5]==4:
								CajaAdivinanza=BotonAdivinanza("balon4.png",650+10,500+10)
								matrizrespuestas[3][5]=4
								ternatemporal.append(4)

							elif matrizcasillas[3][5]==5:
								CajaAdivinanza=BotonAdivinanza("balon5.png",650+10,500+10)
								matrizrespuestas[3][5]=5
								ternatemporal.append(5)

							elif matrizcasillas[3][5]==6:
								CajaAdivinanza=BotonAdivinanza("balon6.png",650+10,500+10)
								matrizrespuestas[3][5]=6
								ternatemporal.append(6)

							elif matrizcasillas[3][5]==7:
								CajaAdivinanza=BotonAdivinanza("balon7.png",650+10,500+10)
								matrizrespuestas[3][5]=7
								ternatemporal.append(7)

							elif matrizcasillas[3][5]==8:
								CajaAdivinanza=BotonAdivinanza("balon8.png",650+10,500+10)
								matrizrespuestas[3][5]=8
								ternatemporal.append(8)

							contador_respuestas+=1
							lista_adivinar.add(CajaAdivinanza)
							listatodos.add(CajaAdivinanza)

				elif event.type==pygame.QUIT:
					pygame.quit(); sys.exit()

			while contador_respuestas==3:
				contador_respuestas=0
				if TernaIgual(ternatemporal):
					print ("Vas Bien!")
				else:
					for Cajita in lista_adivinar:
						lista_adivinar.remove(Cajita)
						listatodos.remove(Cajita)
					matrizrespuestas=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
				if MatrizLlena(matrizrespuestas):
					print ("Felicidades, Acabaste")
					final=True
				else:
					print ("Te falta un poco mas")

				for i in range(0,3):
					ternatemporal.pop()			




		pantalla.blit(fondo,[0,0])
		DibujarMarco()
		listatodos.draw(pantalla)
		listatodos.update(pantalla)
		pantalla.blit(textiempo, (300,15))
		if final:
			pantalla.blit(final_image,[0,0])
		if segundos>=240:
			pantalla.blit(perdiste,[0,0])
		pantalla.blit(limpiar,[795,0])
		pygame.display.update()
		reloj.tick(60)
