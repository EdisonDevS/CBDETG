import pygame
import random
from Util import *
from niveles.clases.Bala import *

class Jefe_Bob(pygame.sprite.Sprite):
    
    def __init__(self, pos, mat_i):
        pygame.sprite.Sprite.__init__(self)

        #control imagen
        self.accion = 0
        self.animacion = 5
        self.matriz = mat_i
        self.limite = [4,8,10,19,4,8,10,19]
        self.image=pygame.transform.scale2x(self.matriz[self.accion][self.animacion])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.centroSprite = [self.rect.x+self.rect.width/2,self.rect.y+self.rect.height/2]

        #stats
        self.sonido = pygame.mixer.Sound('niveles/sonidos/toro.ogg')
        self.sonido.play()
        self.daño_ataque = 0
        self.velx = 0
        self.vely = 0
        self.vida = 10
        self.daño_bala = 25
        self.muriendo = False
        self.atacar=False
        self.atacando=False

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        self.centroSprite = [self.rect.x+self.rect.width/2,self.rect.y+self.rect.height/2]
        self.image=pygame.transform.scale2x(self.matriz[self.accion][self.animacion])

        #Control daño por tipo de ataque

        #derecha
        if self.animacion == 2 and self.accion == 5:
            self.daño_ataque = 10
        if self.animacion == 2 and self.accion == 7:
            self.daño_ataque = 0

        #izquierda
        if self.animacion == 6 and self.accion == 5:
            self.daño_ataque = 10
        if self.animacion == 6 and self.accion == 7:
            self.daño_ataque = 0

        #Control sprites
        if self.accion < self.limite[self.animacion]-1:
            self.accion+=1
        else:
            self.accion = 0
            self.atacando = False
            if self.animacion == 2:
                self.animacion = 0
            if self.animacion == 6:
                self.animacion = 0
            
    

    def run(self,pos_jugador):
        desplazamiento = self.angular(self.centroSprite, pos_jugador)
        self.velx = 7*desplazamiento[0]
        self.vely = 7*desplazamiento[1]
        if self.accion == 0:
            if desplazamiento[0] >= 0:
                self.animacion = 1
            else:
                self.animacion = 5

    def ataque(self, pos_jugador):
        self.velx = 0
        self.vely = 0
        self.atacando=True
        desplazamiento = self.angular(self.centroSprite, pos_jugador)
        if self.accion == 0:
            if desplazamiento[0] >= 0:
                self.animacion = 2
            else:
                self.animacion = 6

    def angular(self, Inicio, Fin):
        yo = Fin[1] - Inicio[1]
        xo = Fin[0] - Inicio[0]
        ang = math.atan2(yo,xo)
        print(ang)
        x = math.cos(ang)
        y = math.sin(ang)
        return ([x,y])

    def comportamientoJefe_Bob(self, pos_jugador):
        #if not self.atacar: 
            #self.run(pos_jugador)
        #else:
        posibilidad_ataque=random.randint(0,20)
        if self.velx > 0:
            self.animacion = 0
        elif self.velx < 0:
            self.animacion = 4
        self.velx = 0
        self.vely = 0
        if not self.atacando:
            if posibilidad_ataque in [1,2,3,4,5,6,7,8,9,10]:
                self.sonido.play()
                self.ataque(pos_jugador)