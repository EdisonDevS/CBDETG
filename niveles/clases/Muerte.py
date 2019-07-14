import pygame
import random
from datetime import datetime
from Util import *

class Muerte(pygame.sprite.Sprite):
    '''
    Clase Muerte
    '''
    #mat_i = matriz recorte imagen
    def __init__(self, pos, mat_i):
        pygame.sprite.Sprite.__init__(self)
        self.m = mat_i
        #self.vida = 200
        #self.flag = 0
        self.lim = [2, 2, 15, 15, 10, 10]
        self.col = 0
        #Imagen en Idle
        self.accion = 0
        #Direccion: "0" Imgen mirando a la izquierda, "1" Imgen mirando a la derecha
        self.direccion = 0
        self.image = self.m[self.accion][self.direccion][self.col]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        #self.velx = 0
        #self.vely = 0
        #self.sonidoA = pygame.mixer.Sound('.ogg')    
    '''          
    def sonidos(self):
        if self.accion == 0:
            self.sonidoA.play()
    '''
    def update(self, player_position):
        #self.rect.x += self.velx
        #self.rect.y += self.vely
        
        if player_position < self.rect.x:
            self.direccion = 0
        elif player_position > self.rect.x:
            self.direccion = 1

        self.image = self.m[self.accion][self.col]

        if self.col < self.lim[self.accion]:
            self.col += 1
        else:
            self.col = 0
            #Para que despues de cada accion vuelva a estar en walk
            if self.accion != 0 and self.direccion == 0:
                self.accion = 0
            elif self.accion != 1 and self.direccion == 1:
                self.accion = 1


