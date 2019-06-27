import pygame
import random
from pygame.locals import *
import sys
from Util import *
from clases.Jugador import *
from clases.Bala import *
from clases.Enemigo import *
from clases.Explosion import *
from clases.Jefe import *

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Util.ANCHO, Util.ALTO])


    #configuracion del jugador
    img_juagador= pygame.image.load('images/liche.png')
    imagenesJugador=Util.cut(img_juagador, 9, 21, 29, 33)


    #configuraion de los enemigos
    img_enemigo= pygame.image.load('images/enemigos.png')
    imagenesEnemigo=Util.cut(img_enemigo, 7, 32, 24, 24)

    #configuracion de las explosiones
    img_explosion=pygame.image.load('images/explosion.png')
    imagenesExplosion=Util.cut(img_explosion, 8, 6, 256, 256)

    #configuracion de las balas
    img_balas_enemigo=pygame.image.load('images/balas.png')
    imagenesBalasEnemigo=Util.cut(img_balas_enemigo, 9, 2, 128, 128)

    #configuracion del jefe
    img_jefe=pygame.image.load('images/boss.png')
    imagenesjefe=Util.cut(img_jefe, 9, 20, 96, 96)

    #grupos
    jugadores=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()
    explosiones=pygame.sprite.Group()
    balas_enemigas=pygame.sprite.Group()
    jefes=pygame.sprite.Group()

    j=Jugador(Util.CENTRO,imagenesJugador)
    jugadores.add(j)
    fin=False
    reloj=pygame.time.Clock()

    jefe = Jefe(Util.CENTRO, imagenesjefe)
    jefes.add(jefe)

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

        #actualizacion de explosiones
        for e in explosiones:
            if(e.animacion==5):
                explosiones.remove(e)
      
        posibilidad_enemigo=random.randint(0,100)

        #print(posibilidad_enemigo)

        if posibilidad_enemigo in [100,50,0]:
            x=j.rect.x
            y=j.rect.y
            while(abs(x-j.rect.x)<200 or abs(y-j.rect.y)<200):
                x=random.randint(0,Util.ANCHO)
                y=random.randint(0,Util.ALTO)
            coordenadas=[x, y]
            e=Enemigo(coordenadas, imagenesEnemigo)
            e.tipo_enemigo=random.randint(0,3)*8
            enemigos.add(e)
        #Disparo
        """
        if j.disparando:
            j.disparos += 1
            if j.disparos >= j.cadencia:
                j.disparos = 0
                b=Bala([j.rect.x, j.rect.y], pygame.mouse.get_pos(), imagenesJugador)
                balas.add(b)
        """

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

        #el jefe ataca cuando está a determinada distancia del jugador
        for je in jefes:
            if pygame.sprite.collide_circle_ratio(0.5)(j,je):
                je.atacar=True
            else:
                je.atacar=False

        jefe.comportamientoJefe(j.getPosition())
        print(jefe.daño_ataque)

        #COLISIONES BALAS-ENEMIGOS
        for b in balas:
            ls_col = pygame.sprite.spritecollide(b, jefes, False)
            for be in ls_col:
                if be.vida>0:
                    be.vida-=be.daño_bala
                else:
                    enemigos.remove(be)
                
                balas.remove(b)


        #COLISION BALAS CON JEFE
        for b in balas:
            ls_col = pygame.sprite.spritecollide(b, enemigos, False)
            for be in ls_col:
                if be.vida>0:
                    be.vida-=be.daño_bala
                else:
                    #la muerte del enemigo depende del tipo
                    if(be.tipo_enemigo==0):
                        None
                    elif(be.tipo_enemigo==8):
                        None
                    elif(be.tipo_enemigo==16):
                        None
                    elif(be.tipo_enemigo==24):
                        print("entro")
                        e=Explosion([be.rect.x-128, be.rect.y-128], imagenesExplosion)
                        explosiones.add(e)

                    enemigos.remove(be)
                
                balas.remove(b)


        #COLISION JEFE
        for je in jefes:
            ls_col = pygame.sprite.spritecollide(je, jugadores, False)
            for ju in ls_col:
                if ju.vida-je.daño_ataque>0:
                    ju.vida-=je.daño_ataque
                else:
                    ju.vida = 0
       


        #COLISIONES EXPLOSION-JUGADOR
        for e in explosiones:
            ls_col = pygame.sprite.spritecollide(e, jugadores, False)
            for jugador in ls_col:
                if(jugador.vida > 0):
                    jugador.vida-=1



        #COLISIONES BALAS ENEMIGAS - JUGADOR
        for b in balas_enemigas:
            ls_col = pygame.sprite.spritecollide(b, jugadores, False)
            for jugador in ls_col:
                if(jugador.vida > 0):
                    jugador.vida-=10
                    balas_enemigas.remove(b)

        '''
        inicio = [j.rect.x,j.rect.y]
        end = pygame.mouse.get_pos()
        desplazamiento = Util.angular(end, inicio)
        desplazamiento = [(j.rect.x - 100*desplazamiento[0]+j.rect.width/2),(j.rect.y - 100*desplazamiento[1]+j.rect.height/2)]
        '''
        player_position=[]

        
        for je in jugadores:
            player_position=je.getPosition()
        


        balas.update()
        jefes.update()
        balas_enemigas.update()
        jugadores.update()
        enemigos.update(player_position, balas_enemigas, imagenesBalasEnemigo)
        explosiones.update()
        pantalla.fill(Util.NEGRO)


        #se muestran los puntajes
        
        texto="Vida: "+str(jefe.vida)
        textoPuntaje=fuente.render(texto, 1, Util.BLANCO)
        pantalla.blit(textoPuntaje,[100,100])
        
        '''
        pygame.draw.line(pantalla, Util.ROJO, [int(j.rect.x+j.rect.width/2), int(j.rect.y+j.rect.height/2)], desplazamiento, 1)
        pygame.draw.circle(pantalla, Util.NEGRO, [int(j.rect.x+j.rect.width/2), int(j.rect.y+j.rect.height/2)], 100, 1)
        '''

        jugadores.draw(pantalla)
        jefes.draw(pantalla)
        balas.draw(pantalla)
        balas_enemigas.draw(pantalla)
        enemigos.draw(pantalla)
        explosiones.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)