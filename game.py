import pygame
from Util import *
from clases.Jugador import *

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Util.ANCHO, Util.ALTO])
    img= pygame.image.load('images/liche.png')

    info=img.get_rect()
    ancho_img=info[2]
    alto_img=info[3]

    m=Util.cut(img, 9, 21, 29, 33)

    jugadores=pygame.sprite.Group()
    j=Jugador([100,50],m)
    jugadores.add(j)
    fin=False
    reloj=pygame.time.Clock()

    vuelo=0 

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    j.velx=-5
                    j.animacion = 10
                    j.concol=0
                if event.key == pygame.K_RIGHT:
                    j.velx=5
                    j.animacion = 10
                    j.concol=0
                if event.key == pygame.K_UP:
                    j.vely=-5
                    j.animacion = 18
                    j.concol=0
                if event.key == pygame.K_DOWN:
                    j.vely=5
                    j.animacion = 8
                    j.concol=0
            if event.type==pygame.KEYUP:
                j.animacion = 13
                j.velx=0
                j.vely=0
            

        jugadores.update()
        pantalla.fill(Util.NEGRO)
        jugadores.draw(pantalla)
        pygame.display.flip()
        reloj.tick(10)