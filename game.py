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
    j=Jugador(Util.CENTRO,m)
    jugadores.add(j)
    fin=False
    reloj=pygame.time.Clock()

    vuelo=0
    desplazamiento = [0,0]

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                j.accion=0
                if event.key == pygame.K_a:
                    j.velx=-5
                    j.animacion = 8
                if event.key == pygame.K_d:
                    j.velx=5
                    j.animacion = 10
                if event.key == pygame.K_w:
                    j.vely=-5
                    j.animacion = 18
                if event.key == pygame.K_s:
                    j.vely=5
                    j.animacion = 9
            if event.type==pygame.KEYUP:
                j.accion = 0
                j.animacion = 13
                j.velx=0
                j.vely=0

            if event.type == pygame.MOUSEBUTTONDOWN:
                j.puntero = True
            if event.type == pygame.MOUSEBUTTONUP:
                j.puntero = False
                if j.animacion != 0:
                        j.animacion = 1
        inicio = [j.rect.x,j.rect.y]
        end = pygame.mouse.get_pos()
        desplazamiento = Util.angular(end, inicio)
        desplazamiento = [(j.rect.x - 100*desplazamiento[0]+j.rect.width/2),(j.rect.y - 100*desplazamiento[1]+j.rect.height/2)]



        jugadores.update()
        pantalla.fill(Util.BLANCO)
        if j.puntero:
            pygame.draw.line(pantalla, Util.CYAN, [int(j.rect.x+j.rect.width/2), int(j.rect.y+j.rect.height/2)], desplazamiento, 1)
        #pygame.draw.circle(pantalla, Util.NEGRO, [int(j.rect.x+j.rect.width/2), int(j.rect.y+j.rect.height/2)], 100, 1)
        jugadores.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)