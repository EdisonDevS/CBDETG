import pygame
import math

class Explosion(pygame.sprite.Sprite):
    def __init__(self, pos_ini, mat_i, lim):
        pygame.sprite.Sprite.__init__(self)
        #limites de los sprites
        self.lim_accion=lim[0]
        self.lim_animacion=lim[1]

        self.accion = 0
        self.animacion = 0
        self.matriz = mat_i
        self.image=self.matriz[0][0]
        self.rect = self.image.get_rect()
        self.rect.x = pos_ini[0]
        self.rect.y = pos_ini[1]


    def update(self):
        if(self.accion<7):
            self.accion+=1
        else:
            self.accion=0
            self.animacion+=1

        self.image=self.matriz[self.accion][self.animacion]
        
        #print(self.rect.x, self.rect.y)
