import pygame
import math
import random
import time
import configparser
from niveles.clases.Bloque import *
from niveles.clases.Enemigo import *
from niveles.clases.NPC import *
from niveles.clases.Jefe import *
from Genesis import *

class Util:
    #colores
    BLANCO=[255,255,255]
    FONDO=[61,37,59]
    VERDE=[0,255,0]
    ROJO=[255,0,0]
    AZUL=[0,255,255]
    NEGRO=[0,0,0]
    AMARILLO = [255, 255, 0]

    #tamaños enemigos
    GRANDE = [30,30]
    MEIDO = [20,20]
    PEQUEÑO = [10,10]

    #tamaños balas
    ESTANDAR = [10,20]
    SNIPER = [6,30]
    BOMBA = [30,30]

    #pantalla
    ANCHO = 1344
    ALTO = 640
    TAMAÑOPANTALLA = [ANCHO, ALTO]
    CENTROX = ANCHO // 2
    CENTROY = ALTO // 2
    CENTRO = [CENTROX,CENTROY]

    #barra de Vida
    ANCHOVIDA = 213
    ALTOVIDA = 30
    TAMAÑOVIDA = [ANCHOVIDA, ALTOVIDA]
    POSICIONBARRAVIDA=[135,16]

    #barra de Inmunidad
    ANCHOINMUNE = 108
    ALTOINMUNE = 30
    TAMAÑOINMUNE = [ANCHOINMUNE, ALTOINMUNE]
    POSICIONBARRAINMUNE=[445,16]
    INMUNIDAD=5

    #minimapa
    ANCHOHABITACION=16
    ALTOHABITACION=16
    XMINIMAPA = 1120
    YMINIMAPA = 80

    def cut(img, columnas, filas, ancho, alto):
        imagenes  = []
        for i in range(columnas):
            imagenes.append([])

        for i in range(columnas):
            for j in range(filas):
                cuadro = img.subsurface(i*ancho, j*alto, ancho, alto)
                imagenes[i].append(cuadro)

        return imagenes

    def angular(Inicio, Fin):
        yo = Fin[1] - Inicio[1]
        xo = Fin[0] - Inicio[0]
        ang = math.atan2(yo,xo)
        print(ang)
        x = math.cos(ang)
        y = math.sin(ang)
        return ([x,y])


    def mapear(habitacion, map, ene, npc, boss):
        mapa=map[habitacion[0]][habitacion[1]]
        #print(mapa)
        mapi = pygame.image.load('niveles/images/mapa.png')
        puer = pygame.image.load('niveles/images/puertasDobles.png')
        key = pygame.image.load('niveles/images/llave.png')
        puerta = Util.cut(puer, 4, 2, 64, 64)
        matrizMapa = Util.cut(mapi, 8, 6, 64, 64)
        imagenesEnemigo=ene
        imagenesNPCreaper=npc
        imagenesBoss=boss
        bloques = pygame.sprite.Group()
        enemigos = pygame.sprite.Group()
        piso = pygame.sprite.Group()
        magma = pygame.sprite.Group()
        agua = pygame.sprite.Group()
        pasto = pygame.sprite.Group()
        puertas = pygame.sprite.Group()
        bosses = pygame.sprite.Group()
        NPCreapers = pygame.sprite.Group()
        llaves = pygame.sprite.Group()
        filas = 0
        for col in range (10):
            for c in mapa[col]:
                #Llave
                if(c[1] == 8000):
                    llave = Bloque(key, [filas*64,col*64])
                    llaves.add(llave)
                #Bosses
                if(c[1] == -1000):
                    b = Jefe([filas*64, col*64], imagenesBoss)
                    NPCreapers.add(b)
                if(c[1] == -2000):
                    b = NPC(imagenesBoss, 4, 1, filas, col)
                    NPCreapers.add(b)
                #NPCs
                if(c[1] == -100):
                    m = NPC(imagenesNPCreaper, 4, 1, filas, col)
                    NPCreapers.add(m)
                if(c[1] == -200):
                    m = NPC(imagenesNPCreaper, 4, 1, filas, col)
                    NPCreapers.add(m)
                #enemigos
                if(c[1] == -10):
                    e=Enemigo([filas*64,col*64], imagenesEnemigo)
                    e.tipo_enemigo = int((c[1]+10)*8)
                    enemigos.add(e)
                if(c[1] == -9):
                    e=Enemigo([filas*64,col*64], imagenesEnemigo)
                    e.tipo_enemigo = int((c[1]+10)*8)
                    enemigos.add(e)
                if(c[1] == -8):
                    e=Enemigo([filas*64,col*64], imagenesEnemigo)
                    e.tipo_enemigo = int((c[1]+10)*8)
                    enemigos.add(e)
                if(c[1] == -7):
                    e=Enemigo([filas*64,col*64], imagenesEnemigo)
                    e.tipo_enemigo = int((c[1]+10)*8)
                    enemigos.add(e)
                        

                #azul
                if(c[0] == 1):
                    bloque = Bloque(matrizMapa[2][2], [filas*64,col*64])
                    piso.add(bloque)
                if(c[0] == 2):
                    bloque = Bloque(matrizMapa[3][2], [filas*64,col*64])
                    piso.add(bloque)
                if(c[0] == 3):
                    bloque = Bloque(matrizMapa[4][4], [filas*64,col*64])
                    agua.add(bloque)
                if(c[0] == 4):
                    bloque = Bloque(matrizMapa[4][5], [filas*64,col*64])
                    agua.add(bloque)
                if(c[0] == 5):
                    bloque = Bloque(matrizMapa[2][1], [filas*64,col*64])
                    bloques.add(bloque)
                if(c[0] == 6):
                    bloque = Bloque(matrizMapa[2][0], [filas*64,col*64])
                    bloques.add(bloque)
                #oscuro
                if(c[0] == 7):
                    bloque = Bloque(matrizMapa[4][2], [filas*64,col*64])
                    piso.add(bloque)
                if(c[0] == 8):
                    bloque = Bloque(matrizMapa[5][2], [filas*64,col*64])
                    piso.add(bloque)
                if(c[0] == 9):
                    bloque = Bloque(matrizMapa[0][4], [filas*64,col*64])
                    magma.add(bloque)
                if(c[0] == 10):
                    bloque = Bloque(matrizMapa[1][5], [filas*64,col*64])
                    magma.add(bloque)
                if(c[0] == 11):
                    bloque = Bloque(matrizMapa[4][1], [filas*64,col*64])
                    bloques.add(bloque)
                if(c[0] == 12):
                    bloque = Bloque(matrizMapa[4][0], [filas*64,col*64])
                    bloques.add(bloque)
                #arenisca
                if(c[0] == 13):
                    bloque = Bloque(matrizMapa[0][2], [filas*64,col*64])
                    piso.add(bloque)
                if(c[0] == 14):
                    bloque = Bloque(matrizMapa[1][2], [filas*64,col*64])
                    piso.add(bloque)
                if(c[0] == 15):
                    bloque = Bloque(matrizMapa[2][4], [filas*64,col*64])
                    pasto.add(bloque)
                if(c[0] == 16):
                    bloque = Bloque(matrizMapa[3][5], [filas*64,col*64])
                    pasto.add(bloque)
                if(c[0] == 17):
                    bloque = Bloque(matrizMapa[1][1], [filas*64,col*64])
                    bloques.add(bloque)
                if(c[0] == 18):
                    bloque = Bloque(matrizMapa[1][0], [filas*64,col*64])
                    bloques.add(bloque)
                #puertas
                if(c[0] == -1):
                    bloque = Bloque(puerta[2][0], [filas*64,col*64])
                    puertas.add(bloque)
                if(c[0] == -2):
                    bloque = Bloque(puerta[1][0], [filas*64,col*64])
                    puertas.add(bloque)
                if(c[0] == -3):
                    bloque = Bloque(puerta[3][0], [filas*64,col*64])
                    puertas.add(bloque)
                if(c[0] == -4):
                    bloque = Bloque(puerta[3][1], [filas*64,col*64])
                    puertas.add(bloque)
                if(c[0] == -5):
                    bloque = Bloque(puerta[1][1], [filas*64,col*64])
                    puertas.add(bloque)
                if(c[0] == -6):
                    bloque = Bloque(puerta[2][1], [filas*64,col*64])
                    puertas.add(bloque)
                if(c[0] == -24):
                    bloque = Bloque(puerta[0][0], [filas*64,col*64])
                    puertas.add(bloque)
                if(c[0] == -25):
                    bloque = Bloque(puerta[0][1], [filas*64,col*64])
                    puertas.add(bloque)
                #nieve
                if(c[0] == 19):
                    bloque = Bloque(matrizMapa[6][3], [filas*64,col*64])
                    piso.add(bloque)
                if(c[0] == 20):
                    bloque = Bloque(matrizMapa[6][2], [filas*64,col*64])
                    piso.add(bloque)
                if(c[0] == 21):
                    bloque = Bloque(matrizMapa[6][4], [filas*64,col*64])
                    agua.add(bloque)
                if(c[0] == 22):
                    bloque = Bloque(matrizMapa[6][1], [filas*64,col*64])
                    bloques.add(bloque)
                if(c[0] == 23):
                    bloque = Bloque(matrizMapa[6][0], [filas*64,col*64])
                    bloques.add(bloque)
                if(c[0] == 24):
                    bloque = Bloque(matrizMapa[6][5], [filas*64,col*64])
                    bloques.add(bloque)
                if(c[0] == 25):
                    bloque = Bloque(matrizMapa[7][5], [filas*64,col*64])
                    bloques.add(bloque)
                filas += 1
            filas = 0

        return bloques, piso, magma, agua, pasto, puertas, enemigos, NPCreapers, bosses, llaves
