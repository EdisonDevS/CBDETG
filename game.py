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

    fondo = pygame.transform.scale2x( pygame.image.load('niveles/images/Fondo.png'))

    fin=False

    musica = pygame.mixer.Sound('niveles/sonidos/musica.ogg')
    musica.play()

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    pos=pygame.mouse.get_pos()
                    if (pos[0]>500 and pos[0]<1000) and (pos[1]>300 and pos[1]<370):
                        j=lvl1(pantalla)
                        if j.nivel_aprobado:
                            j=lvl2(pantalla)

        pantalla.blit(fondo,[0,0])


        #pantalla.fill(Util.BLANCO)

        texto="Iniciar Juego"
        textoPuntaje=titulos.render(texto, 1, Util.BLANCO)
        pantalla.blit(textoPuntaje,[500,300])

        pygame.display.flip()
        reloj.tick(20)
