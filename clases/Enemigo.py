import pygame
from Util import *

class Enemigo(pygame.sprite.Sprite):
    
    def __init__(self, pos, mat_i):
        pygame.sprite.Sprite.__init__(self)
        #control imagen
        self.accion = 0
        self.animacion = 7
        self.matriz = mat_i
        self.limite = [8,8,7,9,9,9,9,6,6,6,6,4,4,4,4,6,5,4,6,3,3]
        self.image = self.matriz[self.accion][self.animacion]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        #stats
        self.velx = 0
        self.vely = 0
        self.vida = 100
        self.cadencia = 30
        self.escudo = 0
        self.inmune = False


    def update(self, player_position):
        self.image=self.matriz[self.accion][self.animacion]

        if self.accion < self.limite[self.animacion]-1:
            self.accion+=1
        else:
            self.accion=0

        #seguir al jugador
        if self.rect.x < player_position[0]:
            self.rect.x +=1
        else: self.rect.x -=1

        if self.rect.y < player_position[1]:
            self.rect.y +=1
        else: self.rect.y -=1