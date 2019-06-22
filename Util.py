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
    ANCHO = 1366
    ALTO = 680
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