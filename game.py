import pygame
import random
from datetime import datetime
import sys
from Util import *
from niveles.lvl1 import *
from niveles.lvl2 import *
from Genesis import *
from niveles.clases.Texto import *
from niveles.clases.Tutorial import *
from niveles.clases.Historia import *

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Util.ANCHO, Util.ALTO])

    fuente=pygame.font.Font(None, 20)
    titulos=pygame.font.Font(None, 70)
    reloj=pygame.time.Clock()

    fondo = pygame.transform.scale2x(pygame.image.load('niveles/images/Fondo.png'))
    #Textos
    img_texto = pygame.image.load('niveles/images/Botones/botones.png')
    imagenestexto = Util.cut(img_texto, 1, 7, 966, 130)
    textos = pygame.sprite.Group()
    t = Texto(Util.CENTRO, imagenestexto, 0)
    t1 = Texto(Util.CENTRO, imagenestexto, 1)
    t2 = Texto(Util.CENTRO, imagenestexto, 2)
    textos.add(t)
    textos.add(t1)
    textos.add(t2)
    #Historia Prologo
    finHist1 = False #True
    fin=False	    
    m = pygame.mixer.music.load('niveles/sonidos/musica.ogg')
    pygame.mixer.music.play(-1)        

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    pos=pygame.mouse.get_pos()
                    '''
                    if (pos[0]>500 and pos[0]<1000) and (pos[1]>300 and pos[1]<370):
                        map=Genesis()
                        j=lvl1(pantalla, map.generateMap(1))
                        if j.nivel_aprobado:
                            j=lvl2(pantalla)
                    '''
                    #Jugar
                    if (pos[0] > 556 and pos[0] < 850) and (pos[1] > 236 and pos[1] < 307):
                        if finHist1 == False:
                            finHist1 = True
                            prologo = Historia(pantalla, 0)
    
                        map=Genesis()
                        #j=lvl1(pantalla, map.generateMap(1))
                        #if j.nivel_aprobado:
                        j=lvl2(pantalla, map.generateMap(2))
                        finHist1 = False
                    if (pos[0] > 493 and pos[0] < 913) and (pos[1] > 440 and pos[1] < 512):
                        tut = Tutorial(pantalla)                        


        
        pantalla.blit(fondo,[0,0])
        #pantalla.fill(Util.BLANCO)
        textos.draw(pantalla)
        #texto="Iniciar Juego"
        #textoPuntaje=titulos.render(texto, 1, Util.BLANCO)
        #pantalla.blit(textoPuntaje,[500,300])        
        pygame.display.flip()
        reloj.tick(20)
