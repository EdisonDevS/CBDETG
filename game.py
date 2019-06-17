import pygame
from Util import *
from clases.Jugador import *

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    img= pygame.image.load('/images/Liche.png')

    info=img.get_rect()
    ancho_img=info[2]
    alto_img=info[3]

    lim=[3,3,2,4,1,3,4,4,6,0]

    m=cortar(img, 70, 80)

    jugadores=pygame.sprite.Group()
    j=Jugador(m,[100,50], lim)
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
        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        pygame.display.flip()
        reloj.tick(30)