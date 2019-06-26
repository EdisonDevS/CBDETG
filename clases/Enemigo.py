import pygame
import random
from Util import *
from clases.Bala import *

class Enemigo(pygame.sprite.Sprite):
    
    def __init__(self, pos, mat_i):
        pygame.sprite.Sprite.__init__(self)
        #tipo de enemigo
        self.tipo_enemigo=0

        #control imagen
        self.accion = 0
        self.animacion = 1
        self.matriz = mat_i
        self.limite = [4,6,7,7,4,6,7,7,4,6,7,7,4,6,7,7,4,6,7,7,4,6,7,7,4,6,7,7,4,6,7,7]
        self.image=pygame.transform.scale2x(self.matriz[self.accion][self.animacion+self.tipo_enemigo])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        #stats
        self.daño_bala=25
        self.velx = 1
        self.vely = 1
        self.vida = 100
        self.cadencia = 30
        self.escudo = 0
        self.inmune = False
        self.correr=False
        self.incremento_correr=0
        self.incremento_caminar=0


    def update(self, player_position, balas_enemgas, img_balas):
        self.disparar(balas_enemgas, player_position, img_balas)

        self.image=pygame.transform.scale2x(self.matriz[self.accion][self.animacion+self.tipo_enemigo])

        if self.correr:
            self.velx=3+self.incremento_correr
            self.vely=3+self.incremento_correr
        else:
            self.velx=1+self.incremento_caminar
            self.vely=1+self.incremento_caminar

        if self.accion < self.limite[self.animacion]-1:
            self.accion+=1
        else:
            self.accion=0

        #seguir al jugador
        if abs(player_position[0]-self.rect.x)<=1:
            if self.correr:
                self.animacion=3
            else:
                self.animacion=0
        elif self.rect.x < player_position[0]:
            self.rect.x += self.velx
            if self.correr:
                self.animacion=3
            else:
                self.animacion=1
        elif self.rect.x > player_position[0]: 
            self.rect.x -= self.velx
            if self.correr:
                self.animacion=7
            else:
                self.animacion=5
        
        if abs(player_position[1]-self.rect.y)<=1:
            self.rect.y+=0
        elif self.rect.y < player_position[1]:
            self.rect.y += self.vely
        else: 
            self.rect.y -= self.vely


    def disparar(self, balas_enemigas, player_position, img_balas):
        if self.tipo_enemigo==8:
            posibilidad=random.randint(0,200)
            if posibilidad in [0,100]:
                print("bala")
                img_balas[2][0]=pygame.transform.scale(img_balas[2][0], [32,32])
                b=Bala([self.rect.x, self.rect.y], player_position, img_balas)
                balas_enemigas.add(b)
