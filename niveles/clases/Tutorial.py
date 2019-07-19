import pygame
import random
from datetime import datetime
from Util import *
from niveles.clases.Texto import *

class Tutorial:
    #Clase Para El Tutorial
    def __init__(self, pantalla):
        fondo = pygame.image.load('niveles/images/tutorial.png')
        fuente=pygame.font.Font(None, 20)
        titulos=pygame.font.Font(None, 70)
        img_texto = pygame.image.load('niveles/images/Botones/botones2.png')
        imagenestexto = Util.cut(img_texto, 1, 8, 966, 140)
        textos = pygame.sprite.Group()
        t = Texto(Util.CENTRO, imagenestexto, 7)
        textos.add(t)
        fin = False

        while not fin:            
            eventos = pygame.event.get()
            for event in eventos:
                if event.type == pygame.QUIT:
                    fin = True
            
            pantalla.blit(fondo,[0,0])
            textos.draw(pantalla)
            #texto="Volver"
            #textoPuntaje = titulos.render(texto, 1, Util.ROJO)
            #pantalla.blit(textoPuntaje,[1200,550]) 
            pygame.display.flip()

    