import pygame
import random
from datetime import datetime
from Util import *


import pygame
import random
from datetime import datetime
from Util import *
from niveles.clases.Texto import *

class Historia:
    #Clase Para El Las Historias
    def __init__(self, pantalla, tipo):
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos=pygame.mouse.get_pos()     
                        #Volver                   
                        if (pos[0] > 996 and pos[0] < 1337) and (pos[1] > 563 and pos[1] < 629):
                            fin = True       
            
            pantalla.blit(fondo,[0,0])
            textos.draw(pantalla)
            pygame.display.flip()