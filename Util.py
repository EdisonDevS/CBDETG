import pygame
import math
import random
import time

class Util:
    #colores
    BLANCO=[255,255,255]
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
    ANCHO = 1024
    ALTO = 384
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

    def VelTr(Enemigo, Jugador):
        yo = Jugador.rect.y - Enemigo.rect.y
        xo = Jugador.rect.x - Enemigo.rect.x
        ang = math.atan2(yo,xo)
        x = int(math.cos(ang))
        y = int(math.sin(ang))
        return ([x,y])