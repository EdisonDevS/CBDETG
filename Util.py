import pygame
import math
import random
import time
import configparser
from niveles.clases.Bloque import *
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
        print(yo)
        print(xo)
        ang = math.atan2(yo,xo)
        print(ang)
        x = math.cos(ang)
        y = math.sin(ang)
        return ([x,y])


    def mapear(habitacion, map):
        mapa=map[habitacion[0]][habitacion[1]]
        #print(mapa)
        mapi = pygame.image.load('niveles/images/mapa.png')
        matrizMapa=Util.cut(mapi, 6, 6, 64, 64)
        bloques = pygame.sprite.Group()
        filas = 0
        for col in range (10):
            for c in mapa[col]:
                if(c == 1):
                    bloque = Bloque(matrizMapa[2][2], [filas*64,col*64])
                    bloques.add(bloque)
                if(c == 2):
                    bloque = Bloque(matrizMapa[3][2], [filas*64,col*64])
                    bloques.add(bloque)
                if(c == 3):
                    bloque = Bloque(matrizMapa[4][4], [filas*64,col*64])
                    bloques.add(bloque)
                if(c == 4):
                    bloque = Bloque(matrizMapa[4][5], [filas*64,col*64])
                    bloques.add(bloque)
                if(c == 5):
                    bloque = Bloque(matrizMapa[2][1], [filas*64,col*64])
                    bloques.add(bloque)
                if(c == 6):
                    bloque = Bloque(matrizMapa[2][0], [filas*64,col*64])
                    bloques.add(bloque)
                if(c == 7):
                    bloque = Bloque(matrizMapa[4][2], [filas*64,col*64])
                    bloques.add(bloque)
                if(c == 8):
                    bloque = Bloque(matrizMapa[5][2], [filas*64,col*64])
                    bloques.add(bloque)
                if(c == 9):
                    bloque = Bloque(matrizMapa[0][4], [filas*64,col*64])
                    bloques.add(bloque)
                if(c == 10):
                    bloque = Bloque(matrizMapa[1][5], [filas*64,col*64])
                    bloques.add(bloque)
                if(c == 11):
                    bloque = Bloque(matrizMapa[4][1], [filas*64,col*64])
                    bloques.add(bloque)
                if(c == 12):
                    bloque = Bloque(matrizMapa[4][0], [filas*64,col*64])
                    bloques.add(bloque)
                filas += 1
            filas = 0

        return bloques