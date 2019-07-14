import pygame
import math
from Util import *

class Hud(pygame.sprite.Sprite):
    def __init__(self, pantalla):
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

        pygame.draw.rect(self.pantalla, Util.VERDE, (150, 15, Util.ANCHOVIDA, Util.ALTOVIDA), 1)
        pygame.draw.rect(self.pantalla, [255-color_verde, color_verde, 0], pygame.Rect((150, 15, tam_vida, Util.ALTOVIDA)), 0)


        #Inmunidad
        if inmune:
            texto="Inmunidad/Magma: Activada"
            textoPuntaje=self.fuente.render(texto, 1, Util.BLANCO)
            self.pantalla.blit(textoPuntaje,[500,20])
        else:
            texto="Inmunidad/Magma: Desactivada"
            textoPuntaje=self.fuente.render(texto, 1, Util.BLANCO)
            self.pantalla.blit(textoPuntaje,[500,20])



        #minimapa
        nivel=0
        lateral=0

        for i in range(5):
            for k in range(5):
                if habitaciones[i][k] == 0:
                    pygame.draw.rect(self.pantalla, Util.VERDE, (1185+lateral, 475+nivel, 10, 10), 1)

                elif habitaciones[i][k] == 1:
                    pygame.draw.rect(self.pantalla, Util.ROJO, pygame.Rect((1185+lateral, 475+nivel, 10, 10)), 0)

                elif habitaciones[i][k] == 2:
                    pygame.draw.rect(self.pantalla, Util.VERDE, pygame.Rect((1185+lateral, 475+nivel, 10, 10)), 0)

                lateral += 20

            nivel+=20
            lateral=0
