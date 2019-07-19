import pygame
import random
from datetime import datetime
from Util import *
from niveles.clases.Texto import *

class Historia:
    #Clase Para El Las Historias
    def __init__(self, pantalla, tipo):
        fondoB1 = pygame.image.load('niveles/images/bosque1.png')
        fondoB2 = pygame.image.load('niveles/images/bosque2.png')
        fondoB3 = pygame.image.load('niveles/images/bosque3.png')
        fondoB4 = pygame.image.load('niveles/images/bosque4.png')        
        fondosB = [fondoB1, fondoB2, fondoB3, fondoB4]

        #tipo : "0" Prologo, "1" Inter-Nivel, "2" Final
        fuente1 = pygame.font.SysFont("Times New Roman", 25)  
        textoPrologo = [str(" Cuentas las leyendas que en lo profundo de un gran bosque vivia un hechiro sin igual , tan poderoso"), 
        str(" que el solo podria destruir naciones enteras.")]
        '''
        +" En su choza el hechicero pasaba su tiempo investigando sobre nuevos hechizos que le permitieran"
        + " alcanzar un poder mayor, una noche un pequeño jabali paso por su residencia emitiendo una "
        + "energia inusual, la cual llamo su atencion entonces tomo una antorcha y se dispuso a perseguirlo;"
        + " logro alcanzarlo en una cueva la cual emitia la misma energía que el Jabali pero en mayor cantidad" 
        + ". Lo que observo en esa cueva el hechicero era algo totalmente nuevo para el, lo que habia en la "
        + "cueva era un gran lago de agua negra, esta sustancia lo cautivo ya que emitia una fuerte energia, "
        + "mientras observaba con asombro un fuerte viento del exterior le hecho a volar el sombrero ante esto"
        + " el reacciono soltando la antorcha para que su sombrero no se ensuciace."
        + " Unos segundos después de que el hechicero soltase la antorcha una gran explosión extruendo los "
        + "cielos y arraso a su paso con casi todo el bosque.")
        '''
        #prologo = fuente1.render(textoPrologo, 1, Util.BLANCO)   
        prologo = []
        for f in textoPrologo:
            prologo.append(fuente1.render(f, 1, Util.NEGRO))

        img_texto = pygame.image.load('niveles/images/Botones/botones3.png')
        imagenestexto = Util.cut(img_texto, 1, 11, 966, 140)
        textos = pygame.sprite.Group()
        #t = Texto(Util.CENTRO, imagenestexto, 7)
        #textos.add(t)

        reloj=pygame.time.Clock()
        instanteInicial = datetime.now()
        fin = False
        i = 0
        j = 0
        while not fin:            
            eventos = pygame.event.get()
            for event in eventos:
                if event.type == pygame.QUIT:
                    fin = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos=pygame.mouse.get_pos()     
                        #Volver                   
                        if (pos[0] > 996 and pos[0] < 1337) and (pos[1] > 563 and pos[1] < 629):
                            fin = True  
            
            instanteFinal = datetime.now()                     
            tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
            segundos = tiempo.seconds
            #if segundos % 1 == 0:
            i += 1
            if i > 3:
                i = 0
            pantalla.blit(fondosB[i],[0,0])
            #textos.draw(pantalla)
            for p in prologo:
                pantalla.blit(p,[150,100 + j]) 
                j += 23
            j = 0
            pygame.display.flip()
            reloj.tick(2)