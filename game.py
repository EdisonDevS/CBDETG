import pygame
import random
from Util import *
from clases.Jugador import *
from clases.Bala import *
from clases.Enemigo import *

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Util.ANCHO, Util.ALTO])
    img= pygame.image.load('images/liche.png')

    info=img.get_rect()
    ancho_img=info[2]
    alto_img=info[3]

    m=Util.cut(img, 9, 21, 29, 33)

    #grupos
    jugadores=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()

    j=Jugador(Util.CENTRO,m)
    jugadores.add(j)
    fin=False
    reloj=pygame.time.Clock()

    vuelo=0
    desplazamiento = [0,0]

    while not fin:

        posibilidad_enemigo=random.randint(0,100)

        #print(posibilidad_enemigo)

        if posibilidad_enemigo in [100,50,0]:
            coordenadas=[random.randint(0,Util.ANCHO), random.randint(0,Util.ALTO)]
            e=Enemigo(coordenadas, m)
            enemigos.add(e)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                j.accion=0
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    j.velx=-5
                    j.animacion = 8
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    j.velx=5
                    j.animacion = 10
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    j.vely=-5
                    j.animacion = 18
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    j.vely=5
                    j.animacion = 9
            if event.type==pygame.KEYUP:
                j.accion = 0
                j.animacion = 13
                j.velx=0
                j.vely=0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==3:
                    if j.animacion != 0:
                            j.animacion = 1
                if event.button==1:
                    b=Bala([j.rect.x, j.rect.y], pygame.mouse.get_pos(), m)
                    balas.add(b)

        #elimina la bala de memoria cuando sale de la pantalla
        for b in balas:
            if (b.rect.x > Util.ANCHO) or (b.rect.x < 0) or (b.rect.y > Util.ALTO) or (b.rect.y < 0):
                balas.remove(b)


        #COLISIONES
        for b in balas:
            ls_col = pygame.sprite.spritecollide(b, enemigos, True)
            for be in ls_col:
                balas.remove(b)

        '''
        inicio = [j.rect.x,j.rect.y]
        end = pygame.mouse.get_pos()
        desplazamiento = Util.angular(end, inicio)
        desplazamiento = [(j.rect.x - 100*desplazamiento[0]+j.rect.width/2),(j.rect.y - 100*desplazamiento[1]+j.rect.height/2)]
        '''
        player_position=[]
        
        for j in jugadores:
            player_position=j.getPosition()

        balas.update()
        jugadores.update()
        enemigos.update(player_position)
        pantalla.fill(Util.BLANCO)
        
        '''
        pygame.draw.line(pantalla, Util.ROJO, [int(j.rect.x+j.rect.width/2), int(j.rect.y+j.rect.height/2)], desplazamiento, 1)
        pygame.draw.circle(pantalla, Util.NEGRO, [int(j.rect.x+j.rect.width/2), int(j.rect.y+j.rect.height/2)], 100, 1)
        '''

        jugadores.draw(pantalla)
        balas.draw(pantalla)
        enemigos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)