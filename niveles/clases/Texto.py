import pygame
import random
from datetime import datetime
from Util import *

class Texto(pygame.sprite.Sprite):
    '''
    Clase Texto
    '''
    #mat_i = matriz recorte imagen
    def __init__(self, pos, mat_i, tipo):
        pygame.sprite.Sprite.__init__(self)
        self.m = mat_i
        #Valores Para Centrar Cada Texto
        self.ajuste = [[-452, -290], [-452, -120], [-452, 80], [0, 0], [0, 0], [0, 0], [0, 0], [8, 238], [0, 0], [0, 0], [8, 238]]
        self.col = 0
        #tipo 0 : Titulo Juego
        #tipo 1 : Jugar
        #tipo 2 : Tutorial
        #tipo 3 : Pausa
        #tipo 4 : Piso II
        #tipo 5 : Victoria
        #tipo 6 : Perdiste           
        self.tipo = tipo
        self.image = self.m[self.col][self.tipo]
        self.rect = self.image.get_rect()     
        self.rect.x = pos[0] + self.ajuste[self.tipo][0]
        self.rect.y = pos[1] + self.ajuste[self.tipo][1]
        self.pos = [self.rect.x, self.rect.y]
