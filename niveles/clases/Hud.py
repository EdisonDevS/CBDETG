import pygame
import math
from Util import *

class Hud(pygame.sprite.Sprite):
    def __init__(self, pantalla):
        pygame.sprite.Sprite.__init__(self)

        #imagen
        self.imagen = pygame.image.load('niveles/images/HUD.png')

        #pantalla
        self.pantalla=pantalla

        #fuentes de texto
        self.fuente=pygame.font.Font(None, 30)



    def update(self, vida, inmune, habitaciones):
        #se muestra el texto de Vida
        texto="Vida: "
        textoPuntaje=self.fuente.render(texto, 1, Util.BLANCO)
        self.pantalla.blit(textoPuntaje,[100,20])

        #barra de Vida
        #300: tamaño en pixeles de la barra de vida (se modifica para el sprite bonito de Serna)
        tam_vida=(vida*Util.ANCHOVIDA)//100
        color_verde=(vida*250)//100

        pygame.draw.rect(self.pantalla, [255-color_verde, color_verde, 0], pygame.Rect((Util.POSICIONBARRAVIDA[0], Util.POSICIONBARRAVIDA[1], tam_vida, Util.ALTOVIDA)), 0)


        #Inmunidad
        if inmune >= 0:
            tam_inmune=(inmune*Util.ANCHOINMUNE)//Util.INMUNIDAD
            pygame.draw.rect(self.pantalla, [255,102,0], pygame.Rect((Util.POSICIONBARRAINMUNE[0], Util.POSICIONBARRAINMUNE[1], tam_inmune, Util.ALTOINMUNE)), 0)

        #se dibuja el HUD
        self.pantalla.blit(self.imagen, [0,0])


        #minimapa
        nivel=0
        lateral=0

        for i in range(5):
            for k in range(5):
                if habitaciones[i][k] == 0:
                    pygame.draw.rect(self.pantalla, Util.VERDE, (Util.XMINIMAPA+lateral, Util.YMINIMAPA+nivel, Util.ANCHOHABITACION, Util.ALTOHABITACION), 1)

                elif habitaciones[i][k] == 1:
                    pygame.draw.rect(self.pantalla, Util.ROJO, pygame.Rect((Util.XMINIMAPA+lateral, Util.YMINIMAPA+nivel, Util.ANCHOHABITACION, Util.ALTOHABITACION)), 0)

                elif habitaciones[i][k] == 2:
                    pygame.draw.rect(self.pantalla, Util.VERDE, pygame.Rect((Util.XMINIMAPA+lateral, Util.YMINIMAPA+nivel, Util.ANCHOHABITACION, Util.ALTOHABITACION)), 0)

                lateral += 2*Util.ANCHOHABITACION

            nivel+=2*Util.ALTOHABITACION
            lateral=0
