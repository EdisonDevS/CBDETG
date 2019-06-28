import pygame
from datetime import datetime
from Util import *
from niveles.clases.Bala import *
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
        self.vida = 1000
        self.cadencia = 5
        self.disparos = 0
        self.escudo = 0
        self.inmune = False
        self.disparando = True
        self.inicio_inmunidad=datetime.now()

    def update(self):
        transcurrido_inmunidad=datetime.now()-self.inicio_inmunidad

        if transcurrido_inmunidad.seconds > 5:
            self.inmune=False

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
    	return [self.rect.x+self.rect.width/2, self.rect.y+self.rect.height/2]


    def eventos(self, balas, evento):
        for event in evento:
            if event.type==pygame.KEYDOWN:
                self.accion=0
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.velx=-5
                    self.animacion = 8
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.velx=5
                    self.animacion = 10
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.vely=-5
                    self.animacion = 18
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.vely=5
                    self.animacion = 9
            if event.type==pygame.KEYUP:
                self.accion = 0
                self.animacion = 13
                self.velx=0
                self.vely=0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==3:
                    if self.animacion != 0:
                            self.animacion = 1
                if event.button==1:
                    b=Bala([self.rect.x, self.rect.y], pygame.mouse.get_pos(), self.matriz)
                    balas.add(b)