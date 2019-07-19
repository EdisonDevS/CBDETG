import pygame
import random
from datetime import datetime
from Util import *
from niveles.clases.Bala import *

class NPC(pygame.sprite.Sprite):
    
    def __init__(self, mat_i, lim, tipo, fil,col):
        pygame.sprite.Sprite.__init__(self)
        #tipo de NPC
        self.tipo_NPC=0

        #control imagen
        self.matriz = mat_i
        self.limite = lim
        self.animacion = 0
        self.accion = 0
        self.image=self.matriz[self.accion][self.animacion]
        self.rect = self.image.get_rect()
        self.rect.x = fil*64    
        self.rect.y = col*64
        #stats
        self.tipo = tipo
        self.ventaja = 0
        self.sonido = pygame.mixer.Sound('niveles/sonidos/Talking.ogg')
        #self.sonido.play()

        #hora de creacion
        self.creacion=datetime.now()

    def update(self):
        if self.accion < self.limite-1:
            self.accion += 1
        else:
            self.accion  = 0
        self.image = self.matriz[self.accion][self.animacion]

        