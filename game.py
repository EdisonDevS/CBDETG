import pygame
import random
from datetime import datetime
import sys
from Util import *
from niveles.lvl1 import *
from niveles.lvl2 import *

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Util.ANCHO, Util.ALTO])

    fuente=pygame.font.Font(None, 20)
    titulos=pygame.font.Font(None, 70)
    reloj=pygame.time.Clock()

    fin=False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    pos=pygame.mouse.get_pos()
                    if (pos[0]>600 and pos[0]<700) and (pos[1]>600 and pos[1]<670):
                        j=lvl1(pantalla)
                        if j.nivel_aprobado:
                            j=lvl2(pantalla)


        pantalla.fill(Util.BLANCO)

        texto="Empezar"
        textoPuntaje=titulos.render(texto, 1, Util.NEGRO)
        pantalla.blit(textoPuntaje,[600,600])

        pygame.display.flip()
        reloj.tick(20)
