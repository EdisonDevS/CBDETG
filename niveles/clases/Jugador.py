import pygame
from datetime import datetime
from Util import *
from niveles.clases.Bala import *
class Jugador(pygame.sprite.Sprite):

    def __init__(self, pos, mat_i, habitacion):
        pygame.sprite.Sprite.__init__(self)
        #control imagen
        self.accion = 0
        self.animacion = 0
        self.matriz = mat_i
        self.limite = [8,8,7,9,9,9,9,6,6,6,6,4,4,4,4,6,5,4,6,3,3]
        self.image=pygame.transform.scale(self.matriz[self.accion][self.animacion], [48, 55])

        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        #habitaciones
        self.habitacionActual = habitacion
        self.habitaciones=[
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0]
                        ]

        self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]=1

        #stats
        self.velx = 0
        self.vely = 0
        self.sonido = pygame.mixer.Sound('niveles/sonidos/fireball.ogg')
        self.burn = pygame.mixer.Sound('niveles/sonidos/burn.ogg')
        self.vida = 100
        self.cadencia = 5
        self.disparos = 0
        self.escudo = 0
        self.inmune = True
        self.tiempo_inmunidad = 5
        self.disparando = True
        self.inicio_inmunidad=datetime.now()


    def update(self, bloques, enemigos, bosses, mapa, imagenesEnemigo,imagenesNPCreaper, NPCreapers, imagenesBoss, llaves, botiquines, bobs, botiquinesBruja, imagenesBotiquin):
        transcurrido_inmunidad=datetime.now()-self.inicio_inmunidad
        self.tiempo_inmunidad = 5-transcurrido_inmunidad.seconds
        
        if transcurrido_inmunidad.seconds >= Util.INMUNIDAD:
            self.inmune=False

        self.dash(bloques)
        if self.animacion == 0 and self.accion == 1:
            self.velx = 0
            self.vely = 0
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        self.image=pygame.transform.scale(self.matriz[self.accion][self.animacion], [48, 55])

        dibujarEnemigos=True
        habitacionBoss = False

        #se hace el cambio de habitación
        if self.rect.x < 0:
            if self.habitacionActual[1]==0:
                self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]=2
                self.habitacionActual[1]=4
                if self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]==2:
                    dibujarEnemigos=False
                self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]=1

            else:
                self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]=2
                self.habitacionActual[1] = self.habitacionActual[1]-1
                if self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]==2:
                    dibujarEnemigos=False
                self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]=1
            self.rect.x = Util.ANCHO-self.rect.w
            self.rect.y = 6*64
            mapa=Util.mapear(self.habitacionActual, mapa, imagenesEnemigo,imagenesNPCreaper, imagenesBoss, imagenesBotiquin)
            if dibujarEnemigos:
                enemigos=mapa[6]
            else:
                enemigos=pygame.sprite.Group()

            for b in botiquines:
                botiquines.remove(b)
            NPCreapers=mapa[7]
            bosses = mapa[8]
            llaves = mapa[9]
            bobs = mapa[10]
            habitacionBoss = mapa[11]
            botiquinesBruja = mapa[13]

        if self.rect.x > Util.ANCHO-self.rect.w:
            if self.habitacionActual[1]==4:
                self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]=2
                self.habitacionActual[1]=0
                if self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]==2:
                    dibujarEnemigos=False
                self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]=1
            else:
                self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]=2
                self.habitacionActual[1] = self.habitacionActual[1]+1
                if self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]==2:
                    dibujarEnemigos=False
                self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]=1
            self.rect.x = 0
            self.rect.y = 3*64
            mapa=Util.mapear(self.habitacionActual, mapa, imagenesEnemigo,imagenesNPCreaper, imagenesBoss, imagenesBotiquin)
            if dibujarEnemigos:
                enemigos=mapa[6]
            else:
                enemigos=pygame.sprite.Group()

            for b in botiquines:
                botiquines.remove(b)
            NPCreapers=mapa[7]
            bosses = mapa[8]
            llaves = mapa[9]
            bobs = mapa[10]
            habitacionBoss = mapa[11]
            botiquinesBruja = mapa[13]

        if self.rect.y < 0:
            if self.habitacionActual[0]==0:
                self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]=2
                self.habitacionActual[0]=4
                if self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]==2:
                    dibujarEnemigos=False
                self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]=1
            else:
                self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]=2
                self.habitacionActual[0] = self.habitacionActual[0]-1
                if self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]==2:
                    dibujarEnemigos=False
                self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]=1
            self.rect.y = Util.ALTO-self.rect.h
            self.rect.x = 4*64
            mapa=Util.mapear(self.habitacionActual, mapa, imagenesEnemigo,imagenesNPCreaper, imagenesBoss, imagenesBotiquin)
            if dibujarEnemigos:
                enemigos=mapa[6]
            else:
                enemigos=pygame.sprite.Group()

            for b in botiquines:
                botiquines.remove(b)
            NPCreapers=mapa[7]
            bosses = mapa[8]
            llaves = mapa[9]
            bobs = mapa[10]
            habitacionBoss = mapa[11]
            botiquinesBruja = mapa[13]

        if self.rect.y > Util.ALTO-self.rect.h:
            if self.habitacionActual[0]==4:
                self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]=2
                self.habitacionActual[0]=0
                if self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]==2:
                    dibujarEnemigos=False
                self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]=1
            else:
                self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]=2
                self.habitacionActual[0] = self.habitacionActual[0]+1
                if self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]==2:
                    dibujarEnemigos=False
                self.habitaciones[self.habitacionActual[0]][self.habitacionActual[1]]=1
            self.rect.y = 0
            self.rect.x = 17*64
            mapa=Util.mapear(self.habitacionActual, mapa, imagenesEnemigo,imagenesNPCreaper, imagenesBoss, imagenesBotiquin)
            if dibujarEnemigos:
                enemigos=mapa[6]
            else:
                enemigos=pygame.sprite.Group()

            #se borran los botiquines que haya en el mapa
            for b in botiquines:
                botiquines.remove(b)

            NPCreapers=mapa[7]
            bosses = mapa[8]
            llaves = mapa[9]
            bobs = mapa[10]
            habitacionBoss = mapa[11]
            botiquinesBruja = mapa[13]

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


        return enemigos, NPCreapers, bosses, llaves, botiquines, bobs, habitacionBoss




    def dash(self, bloques):
        hacerDash=True

        inicio = [self.rect.x+self.rect.width/2,self.rect.y+self.rect.height/2]
        end = pygame.mouse.get_pos()
        desplazamiento = Util.angular(inicio, end)
        '''
        for b in bloques:
            if ((self.rect.x+desplazamiento[0]*100 >= b.rect.x and self.rect.x+desplazamiento[0]*100 <= b.rect.x+64) and (self.rect.y+desplazamiento[1]*100 >= b.rect.y and self.rect.y+desplazamiento[1]*100 <= b.rect.y+64)):
                hacerDash=False
        '''
        if self.animacion == 1 and self.accion == 4:
            self.velx += 30*desplazamiento[0]
            self.vely += 30*desplazamiento[1]



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
                    self.sonido.play()
                    balas.add(b)
