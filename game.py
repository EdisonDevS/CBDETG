import pygame
import random
from pygame.locals import *
import sys
from Util import *
from clases.Jugador import *
from clases.Bala import *
from clases.Enemigo import *

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Util.ANCHO, Util.ALTO])


    #configuracion del jugador
    img_juagador= pygame.image.load('images/liche.png')

    imagenesJugador=Util.cut(img_juagador, 9, 21, 29, 33)


    #configuraion de los enemigos
    img_enemigo= pygame.image.load('images/enemigos.png')

    imagenesEnemigo=Util.cut(img_enemigo, 7, 32, 24, 24)

    #grupos
    jugadores=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()

    j=Jugador(Util.CENTRO,imagenesJugador)
    jugadores.add(j)
    fin=False
    reloj=pygame.time.Clock()

    vuelo=0
    desplazamiento = [0,0]
    fuente=pygame.font.Font(None, 20)
    puntaje=0

    while not fin:
        eventos=pygame.event.get()

        for event in eventos:
            if event.type == pygame.QUIT:
                fin=True
            #eventos del jugador
        j.eventos(balas, eventos)


        posibilidad_enemigo=random.randint(0,100)

        #print(posibilidad_enemigo)

        if posibilidad_enemigo in [100,50,0]:
            coordenadas=[random.randint(0,Util.ANCHO), random.randint(0,Util.ALTO)]
            e=Enemigo(coordenadas, imagenesEnemigo)
            e.tipo_enemigo=random.randint(0,3)*8
            enemigos.add(e)

        #Disparo
        if j.disparando:
            j.disparos += 1
            if j.disparos >= j.cadencia:
                j.disparos = 0
                b=Bala([j.rect.x, j.rect.y], pygame.mouse.get_pos(), imagenesJugador)
                balas.add(b)


        #elimina la bala de memoria cuando sale de la pantalla
        for b in balas:
            if (b.rect.x > Util.ANCHO) or (b.rect.x < 0) or (b.rect.y > Util.ALTO) or (b.rect.y < 0):
                balas.remove(b)

        #el enemigo corre cuando está a determinada distancia del jugador
        for e in enemigos:
            if pygame.sprite.collide_circle_ratio(2.0)(j,e):
                e.correr=True
            else:
                e.correr=False

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


        #se muestran los puntajes
        """
        texto="Puntaje: "+str(puntaje)
        textoPuntaje=fuente.render(texto, 1, Util.NEGRO)
        pantalla.blit(textoPuntaje,[100,100])
        """
        '''
        pygame.draw.line(pantalla, Util.ROJO, [int(j.rect.x+j.rect.width/2), int(j.rect.y+j.rect.height/2)], desplazamiento, 1)
        pygame.draw.circle(pantalla, Util.NEGRO, [int(j.rect.x+j.rect.width/2), int(j.rect.y+j.rect.height/2)], 100, 1)
        '''

        jugadores.draw(pantalla)
        balas.draw(pantalla)
        enemigos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)