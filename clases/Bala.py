import pygame
import math

class Bala(pygame.sprite.Sprite):
    def __init__(self, pos_ini, pos_fin, mat_i):
        pygame.sprite.Sprite.__init__(self)
        self.accion = 0
        self.animacion = 0
        self.matriz = mat_i
        self.image=pygame.transform.scale2x(self.matriz[1][0])
        self.rect = self.image.get_rect()
        self.rect.x = pos_ini[0]
        self.rect.y = pos_ini[1]
        self.pos_ini=pos_ini
        self.pos_fin=pos_fin

        #stats
        self.velx = 0
        self.vely = 0
        self.tipo = 0

        #crear trayectoria
        self.trayectoria()


    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        #print(self.rect.x, self.rect.y)


    def trayectoria(self):
        #print(self.pos_fin, self.pos_ini)
        ang= math.atan2((self.pos_fin[1]-self.pos_ini[1]),(self.pos_fin[0]-self.pos_ini[0]))
        #print(ang)
        x=int(30*math.cos(ang))
        y=int(30*math.sin(ang))
        print (x,y)
        self.velx=x
        self.vely=y