import pygame
import random
from Util import *
from clases.Bala import *

class Jefe(pygame.sprite.Sprite):
    
    def __init__(self, pos, mat_i):
        pygame.sprite.Sprite.__init__(self)

        #control imagen
        self.accion = 0
        self.animacion = 5
        self.matriz = mat_i
        self.limite = [5,8,5,9,5,6,9,3,3,6,5,8,5,9,5,6,9,3,3,6]
        self.image=pygame.transform.scale2x(self.matriz[self.accion][self.animacion])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.centroSprite = [self.rect.x+self.rect.width/2,self.rect.y+self.rect.height/2]

        #stats
        self.daño_ataque = 0
        self.cool_down = 0
        self.velx = 0
        self.vely = 0
        self.vida = 100
        self.escudo = 0
        self.inmune = False
        self.atacar=False
        self.atacando=False

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        self.centroSprite = [self.rect.x+self.rect.width/2,self.rect.y+self.rect.height/2]
        self.image=pygame.transform.scale2x(self.matriz[self.accion][self.animacion])

        #Control daño por tipo de ataque

        #derecha
        if self.animacion == 3 and self.accion == 1:
            self.daño_ataque = 10
        if self.animacion == 4 and self.accion == 1:
            self.daño_ataque = 5
        if self.animacion == 6 and self.accion == 3:
            self.daño_ataque = 7

        if self.animacion == 3 and self.accion == 3:
            self.daño_ataque = 0
        if self.animacion == 4 and self.accion == 3:
            self.daño_ataque = 0
        if self.animacion == 6 and self.accion == 7:
            self.daño_ataque = 0

        #izquierda
        if self.animacion == 13 and self.accion == 1:
            self.daño_ataque = 10
        if self.animacion == 14 and self.accion == 1:
            self.daño_ataque = 5
        if self.animacion == 16 and self.accion == 3:
            self.daño_ataque = 7

        if self.animacion == 13 and self.accion == 3:
            self.daño_ataque = 0
        if self.animacion == 14 and self.accion == 3:
            self.daño_ataque = 0
        if self.animacion == 16 and self.accion == 7:
            self.daño_ataque = 0

        #Control sprites
        if self.accion < self.limite[self.animacion]-1:
            self.accion+=1
        else:
            self.accion = 0
            self.atacando = False
            if self.animacion == 5:
                self.animacion = 0

    def run(self,pos_jugador):
        desplazamiento = Util.angular(self.centroSprite, pos_jugador)
        self.velx = 5*desplazamiento[0]
        self.vely = 5*desplazamiento[1]
        if desplazamiento[0] >= 0:
            self.animacion = 1
        else:
            self.animacion = 11

    def ataquePesado(self, pos_jugador):
        self.velx = 0
        self.vely = 0
        self.atacando=True
        desplazamiento = Util.angular(self.centroSprite, pos_jugador)
        if self.accion == 0:
            if desplazamiento[0] >= 0:
                self.animacion = 3
            else:
                self.animacion = 13

    def ataqueLiviano(self, pos_jugador):
        self.velx = 0
        self.vely = 0
        self.atacando=True
        desplazamiento = Util.angular(self.centroSprite, pos_jugador)
        if self.accion == 0:
            if desplazamiento[0] >= 0:
                self.animacion = 3
            else:
                self.animacion = 13

    def ataqueRotatorio(self, pos_jugador):
        self.velx = 0
        self.vely = 0
        self.atacando=True
        desplazamiento = Util.angular(self.centroSprite, pos_jugador)
        if self.accion == 0:
            if desplazamiento[0] >= 0:
                self.animacion = 6
            else:
                self.animacion = 16