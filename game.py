import pygame
from Util import *
from clases.Jugador import *

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Util.ANCHO, Util.ALTO])
    img= pygame.image.load('/images/Liche.png')

    info=img.get_rect()
    ancho_img=info[2]
    alto_img=info[3]

    m=Util.cut(img, 9, 21, 26, 31)

    jugadores=pygame.sprite.Group()
    j=Jugador(m,[100,50])
    jugadores.add(j)
    fin=False
    reloj=pygame.time.Clock()

    vuelo=0 

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    j.accion=8
                    j.concol=0
                if event.key == pygame.K_e:
                    j.accion=0
                    j.concol=0
                if event.key == pygame.K_q:
                    j.accion=2
                    j.concol=0
                if event.key == pygame.K_w:
                    j.accion=3
                    j.concol=0
                if event.key == pygame.K_LCTRL:
                    j.accion=9
                    j.concol=0
                if event.key == pygame.K_e:
                    j.accion=6
                    j.concol=0
                if event.key == pygame.K_r:
                    j.accion=7
                    j.concol=0
                if event.key == pygame.K_LEFT:
                    j.velx=-5
                    j.concol=0
                if event.key == pygame.K_RIGHT:
                    j.velx=5
                    j.concol=0
            if event.type==pygame.KEYUP:
                j.velx=0
            

        jugadores.update()
        pantalla.fill(Util.NEGRO)
        jugadores.draw(pantalla)
        pygame.display.flip()
        reloj.tick(30)