import pygame
import random
from datetime import datetime
from Util import *
from niveles.clases.Texto import *

class Historia:
    #Clase Para El Las Historias
    def __init__(self, pantalla, tipo):
        fondoB1 = pygame.image.load('niveles/images/bosque1.png')
        fondoB2 = pygame.image.load('niveles/images/bosque2.png')
        fondoB3 = pygame.image.load('niveles/images/bosque3.png')
        fondoB4 = pygame.image.load('niveles/images/bosque4.png')
        fondosB = [fondoB1, fondoB2, fondoB3, fondoB4]
        #tipo : "0" Prologo, "1" Inter-Nivel, "2" Final
        fuente = pygame.font.SysFont("Times New Roman", 20)        
        img_texto = pygame.image.load('niveles/images/Botones/botones3.png')
        imagenestexto = Util.cut(img_texto, 1, 11, 966, 140)
        textos = pygame.sprite.Group()
        #t = Texto(Util.CENTRO, imagenestexto, 7)
        #textos.add(t)
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
            
            pantalla.blit(fondosB[3],[0,0])
            #textos.draw(pantalla)
            pygame.display.flip()