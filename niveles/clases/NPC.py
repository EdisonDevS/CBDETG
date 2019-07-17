import pygame
import random
from datetime import datetime
from Util import *
from niveles.clases.Bala import *

class NPC(pygame.sprite.Sprite):
    
    def __init__(self, pos, mat_i, lim, ):
        pygame.sprite.Sprite.__init__(self)
        #tipo de NPC
        self.tipo_NPC=0

        #control imagen
        self.matriz = mat_i
        self.limite = lim
        self.image=self.matriz[self.accion][self.animacion+self.tipo_NPC]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        #stats
        self.ventaja = 0
        self.sonido = pygame.mixer.Sound('niveles/sonidos/dinos.ogg')
        self.sonido.play()

        #hora de creacion
        self.creacion=datetime.now()

    def update(self):
        transcurrido=datetime.now()-self.creacion
        segundos=transcurrido.seconds

        if(segundos%5==0):
            self.x=random.randint(0,Util.ANCHO)
            self.y=random.randint(0,Util.ALTO)
        
        if(self.tipo_enemigo==0):
            player_position=[self.x,self.y]


            
        self.disparar(balas_enemgas, player_position, img_balas)

        self.image=pygame.transform.scale2x(self.matriz[self.accion][self.animacion+self.tipo_enemigo])

        