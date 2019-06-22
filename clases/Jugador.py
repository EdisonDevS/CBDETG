import pygame
from Util import *
class Jugador(pygame.sprite.Sprite):
    
    def __init__(self, pos, mat_i):
        pygame.sprite.Sprite.__init__(self)
        #control imagen
        self.accion = 0
        self.animacion = 0
        self.matriz = mat_i
        self.limite = [8,8,7,9,9,9,9,6,6,6,6,4,4,4,4,6,5,4,6,3,3]
        self.image=pygame.transform.scale2x(self.matriz[self.accion][self.animacion])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        #stats
        self.velx = 0
        self.vely = 0
        self.vida = 100
        self.cadencia = 5
        self.disparos = 0
        self.escudo = 0
        self.inmune = False
        self.disparando = False

    def update(self):
        self.dash()
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        self.image=pygame.transform.scale2x(self.matriz[self.accion][self.animacion])

        if self.accion < self.limite[self.animacion]-1:
            self.accion+=1
        else:
            self.accion=0
            if self.animacion == 0:
                self.animacion = 13
            if self.animacion == 17:
                self.animacion = 13
            if self.animacion == 1:
                self.animacion = 0
    
    def dash(self):
        if self.animacion == 1 and self.accion == 7:
            inicio = [self.rect.x+self.rect.width/2,self.rect.y+self.rect.height/2]
            end = pygame.mouse.get_pos()
            desplazamiento = Util.angular(inicio, end)
            self.rect.x += 100*desplazamiento[0]
            self.rect.y += 100*desplazamiento[1]


    def getPosition(self):
    	return [self.rect.x, self.rect.y]