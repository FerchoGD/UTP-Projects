# -*- coding: cp1252 -*-
from Library import *

T_PANTALLA = (1000, 600) 

global INCREMENTO_MOV_HOR
INCREMENTO_MOV_HOR = 10

global FPS
global clock
global time_spent

def RelRect(actor, camara):
    return pygame.Rect(actor.rect.x-camara.rect.x, actor.rect.y-camara.rect.y, actor.rect.w, actor.rect.h)

#CLASE PARA CENTRAR LA CAMARA EN EL JUGADOR
class Camara(object): 

    def __init__(self, pantalla, jugador, anchoNivel, largoNivel):
        self.jugador = jugador
        self.rect = pantalla.get_rect()
        self.rect.center = self.jugador.center
        self.mundo_rect = Rect(0, 0, anchoNivel, largoNivel)

    def update(self):
      if self.jugador.centerx > self.rect.centerx + 25:
          self.rect.centerx = self.jugador.centerx - 25
          
      if self.jugador.centerx < self.rect.centerx - 25:
          self.rect.centerx = self.jugador.centerx + 25

      if self.jugador.centery > self.rect.centery + 25:
          self.rect.centery = self.jugador.centery - 25

      if self.jugador.centery < self.rect.centery - 25:
          self.rect.centery = self.jugador.centery + 25
      self.rect.clamp_ip(self.mundo_rect)

    def dibujarSprites(self, pantalla, sprites):
        for s in sprites:
            if s.rect.colliderect(self.rect):
                pantalla.blit(s.image, RelRect(s, self))

#CLASE PARA CREAR OBSTACULOS
class Obstaculo(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Mundo/Obstaculo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y        

    def update(self):
        pass

#CLASE PARA CREAR PUERTA LEVEL 1
class Puerta1(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Mundo/goal.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def update(self):
        pass

#CLASE PARA CREAR PUERTA LEVEL 2
class Puerta2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Mundo/goal.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

#CLASE PARA CREAR LA EXPLOSION
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Explosion/e1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.pausado = False
        self.rect.y = y
        self.contador = 0
        self.avanzar = ["Explosion/e1.png", "Explosion/e1.png",
                        "Explosion/e2.png", "Explosion/e2.png", "Explosion/e2.png",
                        "Explosion/e3.png", "Explosion/e3.png", "Explosion/e3.png",
                        "Explosion/e4.png", "Explosion/e4.png", "Explosion/e4.png",
                        "Explosion/e5.png", "Explosion/e5.png", "Explosion/e5.png"]

    def update(self):
        if self.pausado == False:
            if self.contador <= 13:
                self.image = pygame.image.load(self.avanzar[self.contador])
                self.contador += 1

#CLASE PARA CREAR LA MINIEXPLOSION
class miniExplosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Explosion/me1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pausado = False
        self.contador = 0
        self.avanzar = ["Explosion/me1.png", "Explosion/me1.png",
                        "Explosion/me2.png", "Explosion/me2.png", "Explosion/me2.png",
                        "Explosion/me3.png", "Explosion/me3.png", "Explosion/me3.png",
                        "Explosion/me4.png", "Explosion/me4.png", "Explosion/me4.png",
                        "Explosion/me5.png", "Explosion/me5.png", "Explosion/me5.png"]

    def update(self):
        if self.pausado == False:
            if self.contador <= 13:
                self.image = pygame.image.load(self.avanzar[self.contador])
                self.contador += 1

#CLASE PARA CREAR CALAVERA
class Calavera(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Mundo/C.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

#CLASE PARA CREAR RAYO
class Rayo(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Mundo/rayo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

#CLASE PARA CREAR ESTRELLA
class Estrella(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Mundo/estrella.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

#CLASE PARA CREAR PILDORA
class Pildora(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Mundo/Pildora.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass


#CLASE PARA CREAR CUADRO ROJO
class C_Rojo(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Mundo/c_rojo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

#CLASE PARA EL JUGADOR Y SUS COLISIONES
class Jugador(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pausado = False
        self.nivel = 1
        self.vida = 100
        self.puntaje = 0
        self.ganar = False
        self.movy = 0
        self.movx = 0
        self.balas = 50
        self.laser = 4
        self.inCuadro = False
        self.poder = 20
        self.velocidad = 10
        self.contacto = False
        self.salto = False
        self.image = pygame.image.load('Jugador/b_Verde.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y  
        self.direccion = "D" 
        self.arriba = False
        self.derecha = False
        self.izquierda = False
        self.duracion = 200

    def menosVida1(self):
        self.vida -= 1

    def menosVida2(self):
        self.vida -= 3

    def menosVida3(self):
        self.vida = 0

    def menosVida4(self):
        self.vida -= 5

    def menosVida5(self):
        self.vida -= 7

    def masPuntaje(self):
        self.puntaje += 4
        
    def masPuntaje2(self):
        self.puntaje += 100

    def masPuntaje3(self):
        self.puntaje += 120

    def masPuntaje4(self):
        self.puntaje += self.vida

    def menosPuntaje(self):
        self.puntaje -= 50
        if self.puntaje <= 0:
            self.puntaje = 0

    def menosPuntaje1(self):
        self.puntaje -= 500
        if self.puntaje <= 0:
            self.puntaje = 0
    
    def ir_derecha(self):
        self.derecha = True

    def ir_izquierda(self):
        self.izquierda = True

    def ir_arriba(self):
        self.arriba = True

    def no_arriba(self):
        self.arriba = False

    def no_mover(self):
        self.derecha = False
        self.izquierda = False

    def update(self):
        if self.pausado == False:
            if self.poder == 25:
                if self.duracion > 0:
                    self.duracion -= 2
                else:
                    self.poder = 20
                    self.duracion = 200

            if self.arriba:
                if self.contacto:
                    self.salto = True
                    self.movy -= self.poder
            
            if self.izquierda:
                self.movx = - self.velocidad
                self.direccion = "I" 

            if self.derecha:
                self.movx = + self.velocidad
                self.direccion = "D" 
                self.masPuntaje()

            if not (self.izquierda or self.derecha):
                self.movx = 0
            self.rect.right += self.movx

            self.colision(self.movx, 0, mundo)

            if not self.contacto:
                self.movy += 0.3
                if self.movy > 10:
                    self.movy = 10
                self.rect.top += self.movy

            if self.salto:
                self.movy += 2
                self.rect.top += self.movy
                if self.contacto == True:
                    self.salto = False

            self.contacto = False
            self.colision(0, self.movy, mundo)

    def colision(self, movx, movy, mundo):
        self.contacto = False
        for o in mundo:
            if self.rect.colliderect(o):
                if movx > 0:
                    self.rect.right = o.rect.left

                if movx < 0:
                    self.rect.left = o.rect.right

                if movy > 0:
                    self.rect.bottom = o.rect.top
                    self.movy = 0
                    self.contacto = True

                if movy < 0:
                    self.rect.top = o.rect.bottom
                    self.movy = 0

# CLASE PARA LAS BALAS DEL JUGADOR
class Bala(pygame.sprite.Sprite):
        def __init__(self, x, y, O):
                pygame.sprite.Sprite.__init__(self)
                self.x = x
                self.pausado = False
                self.O = O
                self.velocidad = 20     
                self.image = pygame.image.load('Jugador/b_Jugador.png').convert_alpha()
                self.rect = self.image.get_rect()
                if self.O == "D":
                    self.rect.topleft = [x + 25, y]
                if self.O == "I":
                    self.rect.topleft = [x - 25, y]

        def update(self):
            if self.pausado == False:
                if self.O == "D":
                    self.Derecha()
                if self.O == "I":
                    self.Izquierda()
             
        def Derecha(self):
            self.rect.x += self.velocidad

        def Izquierda(self):
            self.rect.x -= self.velocidad

# CLASE PARA LOS LASER DEL JUGADOR
class Laser(pygame.sprite.Sprite):
        def __init__(self, x, y, O):
                pygame.sprite.Sprite.__init__(self)
                self.x = x
                self.O = O
                self.pausado = False
                self.velocidad = 20
                if O == "D":
                    self.image = pygame.image.load('Jugador/L_derecho.png').convert_alpha()
                else:
                    self.image = pygame.image.load('Jugador/L_izquierdo.png').convert_alpha()
                self.rect = self.image.get_rect()
                if self.O == "D":
                    self.rect.topleft = [x + 25, y]
                if self.O == "I":
                    self.rect.topleft = [x - 25, y]

        def update(self):
            if self.pausado == False:
                if self.O == "D":
                    self.Derecha()
                if self.O == "I":
                    self.Izquierda()
             
        def Derecha(self):
            self.rect.x += self.velocidad

        def Izquierda(self):
            self.rect.x -= self.velocidad

#CLASE PARA EL ENEMIGO 1 Y SUS COLISIONES
class Enemigo1(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.movy = 0
        self.x = x
        self.pausado = False
        self.y = y
        self.contacto = False
        self.salto = False
        self.image = pygame.image.load('Enemigo1/bRoja.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        
    def update(self):
        if self.pausado == False:
            if self.contacto:
                self.salto = True
                self.movy -= 20

            self.colision(0, mundo)

            if not self.contacto:
                self.movy += 0.3
                if self.movy > 10:
                    self.movy = 10
                self.rect.top += self.movy

            if self.salto:
                self.movy += 2
                self.rect.top += self.movy
                if self.contacto == True:
                    self.salto = False

            self.contacto = False
            self.colision(self.movy, mundo)


    def colision(self, movy, mundo):
        self.contacto = False
        for o in mundo:
            if self.rect.colliderect(o):
                if movy > 0:
                    self.rect.bottom = o.rect.top
                    self.movy = 0
                    self.contacto = True

                if movy < 0:
                    self.rect.top = o.rect.bottom
                    self.movy = 0

#CLASE PARA EL ENEMIGO 2 Y SUS COLISIONES
class Enemigo2(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.movy = 0
        self.movx = 0
        self.x = x
        self.y = y
        self.pausado = False
        self.ciclo = False
        self.contacto = False
        self.salto = False
        self.recarga = random.randrange(200, 400)
        self.disparar = False
        self.image = pygame.image.load('Enemigo2/bAzul.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.frame = 0
        self.direccion = "derecha"

    def update(self):
        if self.pausado == False:
            if self.direccion == "izquierda":
                self.movx = - INCREMENTO_MOV_HOR
                
            if self.direccion == "derecha":
                self.movx = + INCREMENTO_MOV_HOR
              
            self.rect.right += self.movx
            self.colision(self.movx, 0, mundo)

            if not self.contacto:
                self.movy += 0.3
                if self.movy > 10:
                    self.movy = 10
                self.rect.top += self.movy

            self.contacto = False
            self.colision(0, self.movy, mundo)

            if self.recarga == 0:
                self.disparar = True
                self.recarga = random.randrange(200, 400)
            else:
                self.recarga -= 1
                self.disparar = False
        
    def colision(self, movx, movy, mundo):
        self.contacto = False
        for o in mundo:
            if self.rect.colliderect(o):
                if movx > 0:
                    self.rect.right = o.rect.left
                    self.direccion = "izquierda"

                if movx < 0:
                    self.rect.left = o.rect.right
                    self.direccion = "derecha"

                if movy > 0:
                    self.rect.bottom = o.rect.top
                    self.movy = 0
                    self.contacto = True

                if movy < 0:
                    self.rect.top = o.rect.bottom
                    self.movy = 0

# CLASE PARA EL ENEMIGO 3
class Enemigo3(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Enemigo3/bNaranja.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 25

    def update(self):
        pass

#CLASE PARA EL ENEMIGO 1 Y SUS COLISIONES
class Enemigo4(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.movy = 0
        self.pausado = False
        self.contacto = False
        self.salto = False
        self.recarga = random.randrange(100, 200)
        self.disparar = False
        self.image = pygame.image.load('Enemigo4/bAmarilla.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        if self.pausado == False:
            if self.contacto:
                self.salto = True
                self.movy -= 20

            self.colision(0, mundo)

            if not self.contacto:
                self.movy += 0.3
                if self.movy > 10:
                    self.movy = 10
                self.rect.top += self.movy

            if self.salto:
                self.movy += 2
                self.rect.top += self.movy
                if self.contacto == True:
                    self.salto = False

            self.contacto = False
            self.colision(self.movy, mundo)

            if self.recarga == 0:
                self.disparar = True
                self.recarga = random.randrange(200, 400)
            else:
                self.recarga -= 1
                self.disparar = False

    def colision(self, movy, mundo):
        self.contacto = False
        for o in mundo:
            if self.rect.colliderect(o):
                if movy > 0:
                    self.rect.bottom = o.rect.top
                    self.movy = 0
                    self.contacto = True

                if movy < 0:
                    self.rect.top = o.rect.bottom
                    self.movy = 0

# CLASE PARA EL ENEMIGO 5
class Enemigo5(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Enemigo5/bMorada.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.pausado = False
        self.rect.x = x
        self.rect.y = y - 25
        self.velocidad = 10
        self.pausado = False
        self.movy = 0
        self.movx = 0
        self.poder = 15
        self.arriba = False
        self.contacto = False
        self.salto = False
        self.derecha = False
        self.mover = False
        self.izquierda = False
        self.recarga = random.randrange(100,200)
        self.disparar = False
        self.direccion = "I"
        self.duracion = 60


    def movimientos(self, jg):
        if jg.rect.x == self.rect.x:
            self.derecha = False
            self.izquierda = False

        if jg.rect.y >= self.rect.y:
            self.arriba = False
        else:
            self.arriba = True

        if jg.rect.x > self.rect.x:
            self.derecha = True
            self.izquierda = False

        if jg.rect.x < self.rect.x:
            self.izquierda = True
            self.derecha = False

    def update(self):
        if self.pausado == False:
            if self.recarga == 0:
                self.disparar = True
                self.recarga = random.randrange(100, 200)
            else:
                self.recarga -= 1
                self.disparar = False

            if self.arriba:
                if self.contacto:
                    self.salto = True
                    self.movy -= self.poder
                
            if self.izquierda:
                self.movx = - self.velocidad
                self.direccion = "I" 

            if self.derecha:
                self.movx = + self.velocidad
                self.direccion = "D" 

            if not (self.izquierda or self.derecha):
                self.movx = 0
            self.rect.right += self.movx

            self.colision(self.movx, 0, mundo)

            if not self.contacto:
                self.movy += 0.3
                if self.movy > 10:
                    self.movy = 10
                self.rect.top += self.movy

            if self.salto:
                self.movy += 2
                self.rect.top += self.movy
                if self.contacto == True:
                    self.salto = False

            self.contacto = False
            self.colision(0, self.movy, mundo)

    def colision(self, movx, movy, mundo):
        self.contacto = False
        for o in mundo:
            if self.rect.colliderect(o):
                if movx > 0:
                    self.rect.right = o.rect.left

                if movx < 0:
                    self.rect.left = o.rect.right

                if movy > 0:
                    self.rect.bottom = o.rect.top
                    self.movy = 0
                    self.contacto = True

                if movy < 0:
                    self.rect.top = o.rect.bottom
                    self.movy = 0


# CLASE PARA EL BOSS
class eBoss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('EnemigoLider/bNegra.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 50
        self.velocidad = 5
        self.pausado = False
        self.vida = 2000
        self.movy = 0
        self.poder = 15
        self.movx = 0
        self.arriba = False
        self.contacto = False
        self.salto = False
        self.derecha = False
        self.mover = False
        self.izquierda = False
        self.escudo = False
        self.recarga = random.randrange(100,200)
        self.disparar = False
        self.direccion = "I"
        self.duracion = 60

    def menosvidaB(self):
        if self.escudo == False:
            self.vida -= 50

    def menosvidaL(self):
        self.vida -= 100

    def movimientos(self, jg):
        if jg.rect.x == self.rect.x:
            self.derecha = False
            self.izquierda = False

        if jg.inCuadro == True:
            self.mover = True
        else:
            self.mover = False

        if jg.rect.y - 10 == self.rect.y:
            self.arriba = False
        else:
            self.arriba = True

        if jg.rect.x > self.rect.x:
            self.derecha = True
            self.izquierda = False

        if jg.rect.x < self.rect.x:
            self.izquierda = True
            self.derecha = False

    def update(self):
        if self.pausado == False:
            if self.mover == True:
                if self.recarga == 0:
                    self.disparar = True
                    self.recarga = random.randrange(100, 200)
                else:
                    self.recarga -= 1
                    self.disparar = False

                if self.escudo == True:
                    self.image = pygame.image.load('EnemigoLider/bNegraD.png').convert_alpha()
                    if self.duracion > 0:
                        self.duracion -= 3
                    else:
                        self.image = pygame.image.load('EnemigoLider/bNegra.png').convert_alpha()
                        self.duracion = False
                        self.duracion = 60
                        self.escudo = False

                if self.arriba:
                    if self.contacto:
                        self.salto = True
                        self.movy -= self.poder
                    
                if self.izquierda:
                    self.movx = - self.velocidad
                    self.direccion = "I" 

                if self.derecha:
                    self.movx = + self.velocidad
                    self.direccion = "D" 

                if not (self.izquierda or self.derecha):
                    self.movx = 0
                self.rect.right += self.movx

                self.colision(self.movx, 0, mundo)

                if not self.contacto:
                    self.movy += 0.3
                    if self.movy > 10:
                        self.movy = 10
                    self.rect.top += self.movy

                if self.salto:
                    self.movy += 2
                    self.rect.top += self.movy
                    if self.contacto == True:
                        self.salto = False

                self.contacto = False
                self.colision(0, self.movy, mundo)

    def colision(self, movx, movy, mundo):
        self.contacto = False
        for o in mundo:
            if self.rect.colliderect(o):
                if movx > 0:
                    self.rect.right = o.rect.left

                if movx < 0:
                    self.rect.left = o.rect.right

                if movy > 0:
                    self.rect.bottom = o.rect.top
                    self.movy = 0
                    self.contacto = True

                if movy < 0:
                    self.rect.top = o.rect.bottom
                    self.movy = 0

def DirBala(jg, eg):
    if(jg.rect.x - eg.rect.x > 0):
        return "D"
    else:
        return "I"

# CLASE PARA LAS BALAS DE LOS ENEMIGOS
class eBala(pygame.sprite.Sprite):
        def __init__(self, x, y, O):
                pygame.sprite.Sprite.__init__(self)
                self.x = x
                self.O = O
                self.pausado = False
                self.velocidad = 20      
                self.image = pygame.image.load('EnemigoLider/b_Enemigos.png').convert_alpha()
                self.rect = self.image.get_rect()
                if self.O == "D":
                    self.rect.topleft = [x + 25, y]
                if self.O == "I":
                    self.rect.topleft = [x - 25, y]

        def update(self):
            if self.pausado == False:
                if self.O == "D":
                    self.Derecha()
                if self.O == "I":
                    self.Izquierda()
             
        def Derecha(self):
            self.rect.x = self.rect.x + self.velocidad

        def Izquierda(self):
            self.rect.x = self.rect.x - self.velocidad

# CLASE PARA LEER EL MAPA Y CREAR EL NIVEL
class Nivel(object): 
    def __init__(self, archivo):
        self.nivel = []
        self.mundo = []
        self.enemigos1 = pygame.sprite.Group()
        self.enemigos2 = pygame.sprite.Group()
        self.enemigos3 = pygame.sprite.Group()
        self.enemigos4 = pygame.sprite.Group()
        self.enemigos5 = pygame.sprite.Group()
        self.muros = pygame.sprite.Group()
        self.ebalas = pygame.sprite.Group()
        self.laser = pygame.sprite.Group()
        self.balas = pygame.sprite.Group()
        self.puertas1 = pygame.sprite.Group()
        self.explosiones = pygame.sprite.Group()
        self.puertas2 = pygame.sprite.Group()
        self.calaveras = pygame.sprite.Group()
        self.rayos = pygame.sprite.Group()
        self.cuadros = pygame.sprite.Group()
        self.pildoras = pygame.sprite.Group()
        self.estrellas = pygame.sprite.Group()
        self.todos = pygame.sprite.Group()
        self.balas = pygame.sprite.Group()
        self.linea = open(archivo, "r")

    def crearNivel(self, x, y):
        for l in self.linea:
            self.nivel.append(l)

        for filas in self.nivel:
            for columnas in filas:
                if columnas == "X":
                    obstaculo = Obstaculo(x, y)
                    self.mundo.append(obstaculo)
                    self.muros.add(obstaculo)
                    self.todos.add(obstaculo)
                if columnas == "P":
                    self.jugador = Jugador(x, y)
                    self.todos.add(self.jugador)
                if columnas == "E":
                    self.enemigo1 = Enemigo1(x, y)
                    self.enemigos1.add(self.enemigo1)
                    self.todos.add(self.enemigo1)
                if columnas == "F":
                    self.enemigo2 = Enemigo2(x, y)
                    self.enemigos2.add(self.enemigo2)
                    self.todos.add(self.enemigo2)
                if columnas == "B":
                    self.enemigo3 = Enemigo3(x, y)
                    self.enemigos3.add(self.enemigo3)
                    self.todos.add(self.enemigo3)
                if columnas == "W":
                    self.enemigo4 = Enemigo4(x, y)
                    self.enemigos4.add(self.enemigo4)
                    self.todos.add(self.enemigo4)
                if columnas == "Y":
                    self.enemigo5 = Enemigo5(x, y)
                    self.enemigos5.add(self.enemigo5)
                    self.todos.add(self.enemigo5)
                if columnas == "T":
                    self.puerta = Puerta1(x, y)
                    self.puertas1.add(self.puerta)
                    self.muros.add(self.puerta)
                    self.todos.add(self.puerta)
                if columnas == "Q":
                    self.puerta = Puerta2(x, y)
                    self.puertas2.add(self.puerta)
                    self.muros.add(self.puerta)
                    self.todos.add(self.puerta)
                if columnas == "C":
                    self.calavera = Calavera(x, y)
                    self.calaveras.add(self.calavera)
                    self.todos.add(self.calavera)
                if columnas == "R":
                    self.rayo = Rayo(x,y)
                    self.rayos.add(self.rayo)
                    self.todos.add(self.rayo)
                if columnas == "V":
                    self.pildora = Pildora(x,y)
                    self.pildoras.add(self.pildora)
                    self.todos.add(self.pildora)
                if columnas == "S":
                    self.cuadro = C_Rojo(x,y)
                    self.cuadros.add(self.cuadro)
                    self.todos.add(self.cuadro)
                if columnas == "N":
                    self.estrella = Estrella(x,y)
                    self.estrellas.add(self.estrella)
                    self.todos.add(self.estrella)
                if columnas == "L":
                    self.enboss = eBoss(x,y)
                    self.todos.add(self.enboss)
                x += 25
            y += 25
            x = 0

    def getSize(self):
        lineas = self.nivel
        linea = max(lineas, key = len)
        self.ancho = (len(linea))*25
        self.largo = (len(lineas))*25
        return (self.ancho, self.largo)

#############################################################################################################

pygame.init()
pantalla = pygame.display.set_mode(T_PANTALLA)
pantalla_rect = pantalla.get_rect()
fondo = pygame.image.load("Mundo/Fondo.jpg").convert()
nivel = Nivel("Niveles/Niveles.txt")
nivel.crearNivel(0,0)
mundo = nivel.mundo
jugador = nivel.jugador
enboss = nivel.enboss
camara = Camara(pantalla, jugador.rect, nivel.getSize()[0], nivel.getSize()[1])
todos = nivel.todos.copy()
muros = nivel.muros.copy()
laser = nivel.laser.copy()
enemigos1 = nivel.enemigos1.copy()
enemigos2 = nivel.enemigos2.copy()
enemigos3 = nivel.enemigos3.copy()
enemigos4 = nivel.enemigos4.copy()
enemigos5 = nivel.enemigos5.copy()
explosiones = nivel.explosiones.copy()
puertas1 = nivel.puertas1.copy()
puertas2 = nivel.puertas2.copy()
calaveras = nivel.calaveras.copy()
estrellas = nivel.estrellas.copy()
pildoras = nivel.pildoras.copy()
rayos = nivel.rayos.copy()
cuadros = nivel.cuadros.copy()
ebalas = nivel.ebalas.copy()
balas = nivel.balas.copy()
reloj = pygame.time.Clock()

def Jugar():
    pygame.mouse.set_visible(False)
    pausa = False
    Bandera = False
    x, y = 0, 0
    Comenzar()   
    vencerLider = False                             
    while jugador.vida > 0 and jugador.ganar == False:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type== KEYDOWN and event.key == K_SPACE:
                if jugador.balas > 0:
                    jugador.balas -= 1
                    b = Bala(jugador.rect.x, jugador.rect.y, jugador.direccion)
                    balas.add(b)
                    todos.add(b)
            if event.type== KEYDOWN and event.key == K_x:
                if jugador.laser > 0:
                    jugador.laser -= 1
                    l = Laser(jugador.rect.x, jugador.rect.y, jugador.direccion)
                    laser.add(l)
                    todos.add(l)
            if event.type == KEYDOWN and event.key == K_m:
                jugador.rect.x = 10140
                jugador.rect.y = 1700
            if event.type == KEYDOWN and event.key == K_UP:
                jugador.ir_arriba()
            if event.type == KEYDOWN and event.key == K_LEFT:
                jugador.ir_izquierda()
            if event.type == KEYDOWN and event.key == K_RIGHT:
                jugador.ir_derecha()
            if event.type == KEYUP and event.key == K_UP:
                jugador.no_arriba()
            if event.type == KEYUP and event.key == K_LEFT:
                jugador.no_mover()
            if event.type == KEYUP and event.key == K_RIGHT:
                jugador.no_mover()
            if event.type == KEYDOWN and event.key == K_p:
                if pausa == True:
                    pausa = False
                    jugador.pausado = False
                    for e in enemigos1:
                        e.pausado = False
                    for e in enemigos2:
                        e.pausado = False
                    for e in enemigos3:
                        e.pausado = False
                    for e in enemigos4:
                        e.pausado = False
                    for e in enemigos5:
                        e.pausado = False
                    enboss.pausado = False
                    for b in balas:
                        b.pausado = False
                    for b in ebalas:
                        b.pausado = False
                    for ex in explosiones:
                        ex.pausado = False
                else:
                    pausa = True
                    jugador.pausado = True
                    for e in enemigos1:
                        e.pausado = True
                    for e in enemigos2:
                        e.pausado = True
                    for e in enemigos3:
                        e.pausado = True
                    for e in enemigos4:
                        e.pausado = True
                    for e in enemigos5:
                        e.pausado = True
                    enboss.pausado = True
                    for b in balas:
                        b.pausado = True
                    for b in ebalas:
                        b.pausado = True
                    for ex in explosiones:
                        ex.pausado = True

        for e5 in enemigos5:
            e5.movimientos(jugador)
        enboss.movimientos(jugador)

        for b in balas:
            col_bam = pygame.sprite.spritecollide(b, muros, False)
            col_bae1 = pygame.sprite.spritecollide(b, enemigos1, True)
            col_bae2 = pygame.sprite.spritecollide(b, enemigos2, True)
            col_bae3 = pygame.sprite.spritecollide(b, enemigos3, True)
            col_bae4 = pygame.sprite.spritecollide(b, enemigos4, True)
            col_bae5 = pygame.sprite.spritecollide(b, enemigos5, True)
            for bam in col_bam:
                balas.remove(b)
                todos.remove(b)
            for bam in col_bae1:
                ex = Explosion(bam.rect.x,bam.rect.y)
                Explo.play()
                balas.remove(b)
                todos.remove(b)
                explosiones.add(ex)
                todos.add(ex)
            for bam in col_bae2:
                ex = Explosion(bam.rect.x,bam.rect.y)
                Explo.play()
                balas.remove(b)
                todos.remove(b)
                explosiones.add(ex)
                todos.add(ex)
            for bam in col_bae3:
                ex = Explosion(bam.rect.x,bam.rect.y)
                Explo.play()
                balas.remove(b)
                todos.remove(b)
                explosiones.add(ex)
                todos.add(ex)
            for bam in col_bae4:
                ex = Explosion(bam.rect.x,bam.rect.y)
                Explo.play()
                balas.remove(b)
                todos.remove(b)
                explosiones.add(ex)
                todos.add(ex)
            for bam in col_bae5:
                Explo.play()
                ex = Explosion(bam.rect.x,bam.rect.y)
                balas.remove(b)
                todos.remove(b)
                explosiones.add(ex)
                todos.add(ex)
            if enboss.vida > 0:
                if pygame.sprite.collide_mask(b, enboss):
                    ex = miniExplosion(b.rect.x, b.rect.y)
                    explosiones.add(ex)
                    todos.add(ex)
                    Explo.play()
                    balas.remove(b)
                    todos.remove(b)
                    enboss.menosvidaB()
                    enboss.escudo = True
                    if enboss.vida <= 0:
                        ex = Explosion(b.rect.x, b.rect.y)
                        Explo.play()
                        Win.play()
                        todos.remove(enboss)
                        explosiones.add(ex)
                        todos.add(ex)

        if jugador.rect.x > 9235 and jugador.rect.y > 1735:
            jugador.inCuadro = True

        if jugador.rect.y > 2100:
            jugador.vida = 0

        for l in laser:
            col_la = pygame.sprite.spritecollide(l, muros, False)
            col_bae1 = pygame.sprite.spritecollide(l, enemigos1, True)
            col_bae2 = pygame.sprite.spritecollide(l, enemigos2, True)
            col_bae3 = pygame.sprite.spritecollide(l, enemigos3, True)
            col_bae4 = pygame.sprite.spritecollide(l, enemigos4, True)
            col_bae5 = pygame.sprite.spritecollide(l, enemigos5, True)
            for la in col_la:
                laser.remove(l)
                todos.remove(l)
            for bam in col_bae1:
                ex = Explosion(bam.rect.x,bam.rect.y)
                Explo.play()
                laser.remove(l)
                todos.remove(l)
                explosiones.add(ex)
                todos.add(ex)
            for bam in col_bae2:
                ex = Explosion(bam.rect.x,bam.rect.y)
                Explo.play()
                laser.remove(l)
                todos.remove(l)
                explosiones.add(ex)
                todos.add(ex)
            for bam in col_bae3:
                ex = Explosion(bam.rect.x,bam.rect.y)
                Explo.play()
                laser.remove(l)
                todos.remove(l)
                explosiones.add(ex)
                todos.add(ex)
            for bam in col_bae4:
                ex = Explosion(bam.rect.x,bam.rect.y)
                Explo.play()
                laser.remove(l)
                todos.remove(l)
                explosiones.add(ex)
                todos.add(ex)
            for bam in col_bae5:
                laser.remove(l)
                todos.remove(l)
                ex = Explosion(bam.rect.x,bam.rect.y)
                Explo.play()
                explosiones.add(ex)
                todos.add(ex)
            if enboss.vida > 0:
                if pygame.sprite.collide_mask(l, enboss):
                    ex = miniExplosion(l.rect.x, l.rect.y)
                    explosiones.add(ex)
                    todos.add(ex)
                    Explo.play()
                    laser.remove(l)
                    todos.remove(l)
                    enboss.menosvidaL()
                    enboss.escudo = True
                    if enboss.vida <= 0:
                        ex = Explosion(l.rect.x,l.rect.y)
                        Explo.play()
                        Win.play()
                        todos.remove(enboss)
                        explosiones.add(ex)
                        todos.add(ex)

        if enboss.vida <= 0:
            vencerLider = True

        for ex in explosiones:
            if ex.contador == 13:
                explosiones.remove(ex)
                todos.remove(ex)

        col_bal =pygame.sprite.groupcollide(balas, ebalas, True, True)
        for cb in col_bal:
            ex = miniExplosion(cb.rect.x, cb.rect.y)
            Explo.play()
            explosiones.add(ex)
            todos.add(ex)

        for eb in ebalas:
            col_ebam = pygame.sprite.spritecollide(eb, muros, False)
            for ebam in col_ebam:
                ebalas.remove(eb)
                todos.remove(eb)
            if pygame.sprite.collide_mask(jugador, eb):
                jugador.menosVida1()
                ex = miniExplosion(jugador.rect.x, jugador.rect.y)
                ebalas.remove(eb)
                todos.remove(eb)
                todos.add(ex)
                explosiones.add(ex)
                Explo.play()

        col_pildoras = pygame.sprite.spritecollide(jugador, pildoras, True)
        for pil in col_pildoras:
            Item.play() 
            if jugador.vida < 100:
                jugador.vida += 3
                if jugador.vida > 100:
                    jugador.vida = 100

        col_stars = pygame.sprite.spritecollide(jugador, estrellas, True)
        for star in col_stars:
            Item.play()
            jugador.balas += 1

        col_rayo = pygame.sprite.spritecollide(jugador, rayos, True)
        for r in col_rayo:
            Item.play()
            jugador.laser += 1

        col_obj1 = pygame.sprite.spritecollide(jugador, enemigos1, False)
        for ec in col_obj1:
            Danio.play()
            jugador.menosVida1()
            jugador.menosPuntaje()

        col_obj2 = pygame.sprite.spritecollide(jugador, enemigos2, False)
        for ec in col_obj2:
            Danio.play()
            jugador.menosVida2()
            jugador.menosPuntaje()

        col_obj3 = pygame.sprite.spritecollide(jugador, enemigos3, False)
        for ec in col_obj3:
            Danio.play()
            jugador.menosVida3()
            jugador.menosPuntaje1()

        col_obj3 = pygame.sprite.spritecollide(jugador, enemigos4, False)
        for ec in col_obj3:
            Danio.play()
            jugador.menosVida4()
            jugador.menosPuntaje1()

        col_obj3 = pygame.sprite.spritecollide(jugador, enemigos5, False)
        for ec in col_obj3:
            Danio.play()
            jugador.menosVida5()
            jugador.menosPuntaje1()

        col_objC = pygame.sprite.spritecollide(jugador, calaveras, True)
        for ec in col_objC:
            Item.play()
            N2.stop()
            N3.stop()
            N1.play(-1)
            jugador.menosPuntaje1()
            jugador.rect.x = 25
            jugador.rect.y = 1125
            pantalla1 = pygame.display.set_mode(T_PANTALLA)
            texto = fuente.render("N I V E L   1 ", True, BLANCO)
            texto2 = fuente.render("Casa Sala Principal", True, BLANCO)
            texto_rect = texto.get_rect()
            texto_x = pantalla1.get_width() / 2 - texto_rect.width / 2       
            texto_y = pantalla1.get_height() / 2 - texto_rect.height / 2
            pantalla1.blit(texto, [texto_x, texto_y])
            pantalla1.blit(texto2, [texto_x - 15, texto_y + 60])
            pygame.display.flip()
            pygame.time.delay(2000)
            break            

        col_objG = pygame.sprite.spritecollide(jugador, cuadros, True)
        for ec in col_objG:
            Item.play()
            jugador.poder = 25
            jugador.masPuntaje4()

        col_objP = pygame.sprite.spritecollide(jugador, puertas1, False)
        for ec in col_objP:
            N1.stop()
            N3.stop()
            N2.play(-1)
            jugador.masPuntaje2()
            jugador.masPuntaje3()
            jugador.rect.x = 25
            jugador.rect.y = 2100
            pantalla1 = pygame.display.set_mode(T_PANTALLA)
            texto = fuente.render("N I V E L   2", True, BLANCO)
            texto2 = fuente.render("Casa Cuarto Recuperacion", True, BLANCO)
            texto_rect = texto.get_rect()
            texto_x = pantalla1.get_width() / 2 - texto_rect.width / 2       
            texto_y = pantalla1.get_height() / 2 - texto_rect.height / 2
            pantalla1.blit(texto, [texto_x, texto_y])
            pantalla1.blit(texto2, [texto_x, texto_y + 60])
            pygame.display.flip()
            pygame.time.delay(2000)
            break

        col_objS = pygame.sprite.spritecollide(jugador, puertas2, False)
        for ec in col_objP:
            N1.stop()
            N2.stop()
            N3.play(-1)
            jugador.masPuntaje2()
            jugador.masPuntaje3()
            jugador.rect.x = 25
            jugador.rect.y = 3100
            pantalla1 = pygame.display.set_mode(T_PANTALLA)
            texto = fuente.render("N I V E L   3", True, BLANCO)
            texto2 = fuente.render("Llegando a la meta", True, BLANCO)
            texto_rect = texto.get_rect()
            texto_x = pantalla1.get_width() / 2 - texto_rect.width / 2       
            texto_y = pantalla1.get_height() / 2 - texto_rect.height / 2
            pantalla1.blit(texto, [texto_x, texto_y])
            pantalla1.blit(texto2, [texto_x, texto_y + 60])
            pygame.display.flip()
            pygame.time.delay(2000)
            break

        tim = pygame.time.get_ticks()/1000
        if jugador.inCuadro:
            print tim
            if tim % 10 == 0 and Bandera == False:
                Bandera = True
                aux = random.randrange(5)
                pos = random.randrange(9050, 10110)
                if aux == 1:
                    ay = Pildora(pos, 2100)
                    e = Enemigo5(10140, 1700)
                    enemigos5.add(e)
                    Item.play()
                    pildoras.add(ay)
                    todos.add(ay)
                    todos.add(e)
                if aux == 2:
                    ay = C_Rojo(pos, 2100)
                    e = Enemigo2(10140, 1700)
                    enemigos2.add(e)
                    cuadros.add(ay)
                    todos.add(ay)
                    todos.add(e)
                    Item.play()
                if aux == 3:
                    ay = Estrella(pos, 2100)
                    e = Enemigo5(10140, 1700)
                    enemigos5.add(e)
                    estrellas.add(ay)
                    todos.add(ay)
                    Item.play()
                    todos.add(e)
                if aux == 4:
                    ay = Rayo(pos, 2100)
                    e = Enemigo2(10140, 1700)
                    enemigos2.add(e)
                    rayos.add(ay)
                    todos.add(ay)
                    todos.add(e)
                    Item.play()
            if tim % 10 != 0:
                Bandera = False

        for e in enemigos2:
            if e.disparar:
                eb = eBala(e.rect.x, e.rect.y, DirBala(jugador, e))
                ebalas.add(eb)
                todos.add(eb)

        for e in enemigos4:
            if e.disparar:
                eb = eBala(e.rect.x, e.rect.y, DirBala(jugador, e))
                ebalas.add(eb)
                todos.add(eb)

        for e in enemigos5:
            if e.disparar:
                eb = eBala(e.rect.x, e.rect.y, DirBala(jugador, e))
                ebalas.add(eb)
                todos.add(eb)

        if enboss.disparar:
            eb = eBala(enboss.rect.x, enboss.rect.y, DirBala(jugador, enboss))
            ebalas.add(eb)
            todos.add(eb)

        if pygame.sprite.collide_mask(jugador, enboss):
            jugador.menosVida2()

        col_objP = pygame.sprite.spritecollide(jugador, puertas2, False)
        for ec in col_objP:
            if vencerLider:
                N2.stop()
                jugador.masPuntaje()
                jugador.masPuntaje()
                jugador.masPuntaje3()
                jugador.ganar = True
                pantalla1 = pygame.display.set_mode(T_PANTALLA)
                texto = fuenteG.render("A L I A S '70' H A  L O G R A D O  E S C A P A R", True, BLANCO)
                texto2 = fuente.render(" H A S  G A N A D O ", True, BLANCO)
                puntajef = fuente.render("PUNTAJE: " + str(jugador.puntaje), True, BLANCO)
                texto_rect = texto.get_rect()
                texto2_rect = texto2.get_rect()
                texto_x = pantalla1.get_width() / 2 - texto_rect.width / 2       
                texto_y = pantalla1.get_height() / 2 - texto_rect.height / 2
                texto2_x = pantalla1.get_width() / 2 - texto2_rect.width / 2       
                texto2_y = pantalla1.get_height() / 2 - texto2_rect.height / 2
                pantalla1.blit(texto, [texto_x, texto_y])
                pantalla1.blit(texto2, [texto2_x, texto2_y + 60])
                pantalla1.blit(puntajef, [30, 550])
                pygame.display.flip()
                pygame.mixer.music.set_volume(0.4)
                Win.play()
                pygame.time.delay(3000)
                break
            else:
                jugador.rect.right  = ec.rect.left - 25
        
        
        pantalla.blit(fondo, (0, 0))
        todos.update()
        camara.update() 
        camara.dibujarSprites(pantalla, todos)
        pygame.display.flip()    
        puntos = fuente.render("VIDA: " +str(jugador.vida) + "%", True, BLANCO)
        pantalla.blit(puntos, [15, 20])
        puntaje = fuente.render("PUNTAJE: " + str(jugador.puntaje), True, BLANCO)
        pantalla.blit(puntaje, [750, 20])
        reloj.tick(60)

        if(pausa):
            texto = fuenteP.render("P A U S A", True, BLANCO)
            texto_rect = texto.get_rect()
            texto_x = pantalla.get_width() / 2 - texto_rect.width / 2       
            texto_y = pantalla.get_height() / 2 - texto_rect.height / 2
            pantalla.blit(texto, [texto_x, texto_y])
            pygame.display.flip()          

        if (jugador.vida == 0):
            N1.stop()
            N2.stop()
            pantalla1 = pygame.display.set_mode(T_PANTALLA)
            texto = fuente.render("A L I A S 7 0  H A  C A I D O A L I N F I E R N O", True, BLANCO)
            puntajem = fuente.render("PUNTAJE: " + str(jugador.puntaje), True, BLANCO)
            texto_rect = texto.get_rect()
            texto_x = pantalla1.get_width() / 2 - texto_rect.width / 2       
            texto_y = pantalla1.get_height() / 2 - texto_rect.height / 2
            pantalla1.blit(texto, [texto_x, texto_y])
            pantalla1.blit(puntajem, [30, 550])
            pygame.display.flip()
            pygame.time.delay(2000)
            break    
        pygame.display.flip()
    pygame.mouse.set_visible(True)

def Comenzar():
    pygame.mixer.music.set_volume(0.5)
    N1.play(-1)
    jugador.puntaje = 0
    jugador.vida = 100
    jugador.ganar = False
    jugador.no_mover()
    jugador.no_arriba()
    jugador.rect.x = 25
    jugador.rect.y = 1125
    jugador.inCuadro = False
    jugador.poder = 20
    jugador.velocidad = 15
    pantalla1 = pygame.display.set_mode(T_PANTALLA)
    texto = fuente.render("N I V E L   1 - 1", True, BLANCO)
    texto2 = fuente.render("Casa Sala Principal", True, BLANCO)
    texto_rect = texto.get_rect()
    texto_x = pantalla1.get_width() / 2 - texto_rect.width / 2       
    texto_y = pantalla1.get_height() / 2 - texto_rect.height / 2
    pantalla1.blit(texto, [texto_x, texto_y])
    pantalla1.blit(texto2, [texto_x - 20, texto_y + 60])
    pygame.display.flip()
    pygame.time.delay(2000)


def InicioJuego():
    Cargando = 0
    time = 1
    while(Cargando < 100):
        pantalla.fill(NEGRO)
        texto = fuente.render("Cargando " + str(Cargando) + "%", True, BLANCO)
        texto_rect = texto.get_rect()
        Cargando += time
        time += random.randrange(2)
        texto_x = pantalla.get_width() / 2 - texto_rect.width / 2       
        texto_y = pantalla.get_height() / 2 - texto_rect.height / 2
        pantalla.blit(texto, (texto_x, texto_y))
        reloj.tick(10) 
        pygame.display.flip()

#############################################################################################################

def Intro():
    font=pygame.font.Font(None, 36)
    ver_inst = True
    pag=1
    diferencial = 0
    while ver_inst:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                listo = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pag += 1
                if pag == 4:
                    ver_inst = False
        
        if pag==1:

            fondo = pygame.image.load("Mundo/Fondo.jpg").convert()
            pantalla.blit(fondo, (0, 0))

            text=font.render("Alias 70 era un reconocido narcotraficante de  la ciudad...", True, BLANCO)
            pantalla.blit(text, [20, 20])

            im_portada = pygame.image.load("Mundo/Primera.png").convert_alpha()
            pantalla.blit(im_portada, (250,100))

        if pag==2:

            fondo = pygame.image.load("Mundo/Fondo.jpg").convert()
            pantalla.blit(fondo, (0, 0))

            text=font.render("Hasta que un dia se convirtio en la muerte...", True, BLANCO)
            pantalla.blit(text, [20, 20])

            text=font.render("Y fue desafiado por Lucifer a salir de la casa embrujada", True, BLANCO)
            pantalla.blit(text, [20, 60])

            text=font.render("Despues de esto, necesita tu ayuda para poder salir de...LA MUERTE", True, BLANCO)
            pantalla.blit(text, [20, 100])

            im_portada = pygame.image.load("Mundo/Introducir.png").convert_alpha()
            pantalla.blit(im_portada, (200,150))

        if pag==3:
            fondo = pygame.image.load("Mundo/Fondo.jpg").convert()
            pantalla.blit(fondo, (0, 0))
            texto=font.render("C O N T R O L E S", True, BLANCO)
            pantalla.blit(texto, [30, 30])
            im_jugador = pygame.image.load("Jugador/b_Verde.png").convert_alpha()
            im_laser = pygame.image.load("Jugador/L_derecho.png").convert_alpha()
            im_bala = pygame.image.load("Jugador/b_Jugador.png").convert_alpha()
            texto=font.render("Pulsa arriba para saltar", True, BLANCO)
            pantalla.blit(texto, [30, 120])

            texto=font.render("Derecha para correr hacia adelante", True, BLANCO)
            pantalla.blit(texto, [520, 120])

            texto=font.render("Izquierda para correr hacia atras", True, BLANCO)
            pantalla.blit(texto, [300, 240])

            texto=font.render("Espacio para disparar balas", True, BLANCO)
            pantalla.blit(texto, [30, 400])

            texto=font.render("X para disparar el laser", True, BLANCO)
            pantalla.blit(texto, [520, 400])

            pantalla.blit(im_jugador, (100, 180 - diferencial))
            pantalla.blit(im_jugador, (620 + diferencial, 150))
            pantalla.blit(im_jugador, (420 - diferencial, 270))
            pantalla.blit(im_jugador, (30, 430))
            pantalla.blit(im_bala, (75 + diferencial, 435))
            pantalla.blit(im_jugador, (520, 430))
            pantalla.blit(im_laser, (565 + diferencial, 435))
            if diferencial == 40:
                diferencial = 0
            else:
                diferencial += 4

        pygame.display.flip()
         
#############################################################################################################

fuente = pygame.font.Font(None, 40)
fuenteP = pygame.font.Font(None, 150)
fuenteG = pygame.font.Font(None, 70)
fuente2 = pygame.font.Font(None, 24)

terminar = False
fMenu = pygame.font.Font("Cool.otf", 60)
fMenuT = pygame.font.Font("Dragon.ttf",180)
rMenu = fMenuT.render("SIENDO", True, BLANCO)
rMenu2 = fMenuT.render("LA", True, BLANCO)
rMenu3 = fMenuT.render("MUERTE", True, BLANCO)

Menu = [Opcion("Jugar", (440, 400), 0, fMenu, pantalla),
        Opcion("Salir", (448, 500), 1, fMenu, pantalla)]    

N1 = pygame.mixer.Sound("Sonidos/Nivel1.ogg")
pygame.mixer.music.set_volume(1)
N2 =pygame.mixer.Sound("Sonidos/Nivel2.ogg")
pygame.mixer.music.set_volume(1)
N3 =pygame.mixer.Sound("Sonidos/Nivel3.ogg")



Item = pygame.mixer.Sound('Sonidos/Moneda.ogg')
Danio = pygame.mixer.Sound('Sonidos/Danio.ogg')
Win = pygame.mixer.Sound('Sonidos/Win.ogg')
Explo = pygame.mixer.Sound('Sonidos/eSonido.ogg')

clock = pygame.time.Clock()


while not terminar:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        terminar = True
        pantalla.fill((0, 0, 0))
        pantalla.blit(rMenu, [250, 30])
        pantalla.blit(rMenu2, [250, 140])
        pantalla.blit(rMenu3, [250, 250])
        
        for opcion in Menu:
                if opcion.rect.collidepoint(pygame.mouse.get_pos()):
                        opcion.ver=True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if(opcion.valor == 0):
                                    InicioJuego()
                                    Intro()
                                    Jugar()
                                elif(opcion.valor == 1):
                                        terminar = True
                else:
                        opcion.ver = False
                opcion.dibujar(pantalla)
        pygame.display.flip()
pygame.quit()


