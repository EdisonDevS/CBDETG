import pygame
import random
import sys
from datetime import datetime
from pygame.locals import *
from niveles.clases.Jugador import *
from niveles.clases.Bala import *
from niveles.clases.Enemigo import *
from niveles.clases.Explosion import *
from niveles.clases.Botiquin import *
from niveles.clases.Jefe import *

class lvl2:
	def __init__(self, pantalla):
		#configuracion del jugador
		img_juagador= pygame.image.load('niveles/images/liche.png')
		imagenesJugador=Util.cut(img_juagador, 9, 21, 29, 33)

		#configuraion de los enemigos
		img_enemigo= pygame.image.load('niveles/images/enemigos.png')
		imagenesEnemigo=Util.cut(img_enemigo, 7, 32, 24, 24)

		#configuracion de las explosiones
		img_explosion=pygame.image.load('niveles/images/explosion.png')
		imagenesExplosionRojo=Util.cut(img_explosion, 8, 6, 256, 256)

		#configuracion de las explosiones
		img_explosion_azul=pygame.image.load('niveles/images/explosion_azul.png')
		imagenesExplosionAzul=Util.cut(img_explosion_azul, 8, 4, 256, 256)

		#configuracion de las balas
		img_balas_enemigo=pygame.image.load('niveles/images/balas.png')
		imagenesBalasEnemigo=Util.cut(img_balas_enemigo, 9, 2, 128, 128)

		#configuracion de los botiquines
		img_botiquin=pygame.image.load('niveles/images/botiquin.png')
		imagenesBotiquin=Util.cut(img_botiquin, 2, 1, 32, 24)

		#configuracion del jefe
		img_jefe=pygame.image.load('niveles/images/boss.png')
		imagenesjefe=Util.cut(img_jefe, 9, 20, 96, 96)

		self.pantalla=pantalla
		self.nivel_aprobado=False

		#grupos
		jugadores=pygame.sprite.Group()
		jefes=pygame.sprite.Group()
		balas=pygame.sprite.Group()
		enemigos=pygame.sprite.Group()
		explosiones=pygame.sprite.Group()
		balas_enemigas=pygame.sprite.Group()
		botiquines=pygame.sprite.Group()
		bloques=pygame.sprite.Group()
		bloques = Util.mapear('niveles/Mapas/mapa2.map')
		
		#jugador
		j=Jugador(Util.CENTRO,imagenesJugador)
		jugadores.add(j)

		#Boss
		jefe = Jefe([400,500], imagenesjefe)
		jefes.add(jefe)

		#variables necesarias
		fin=False
		reloj=pygame.time.Clock()
		instanteInicial = datetime.now()

		#fuentes de texto
		fuente=pygame.font.Font(None, 30)
		titulos=pygame.font.Font(None, 70)

		#juego
		while not fin:

			if j.vida>100:
				j.vida-=0.1

			if j.vida<=0:
				self.muerte()
				break

			if len(jefes)==0 and len(enemigos)==0:
				self.nivel_finalizado()

			#el jefe ataca cuando está a determinada distancia del jugador
			for je in jefes:
				if pygame.sprite.collide_circle_ratio(0.5)(j,je):
					je.atacar=True
				else:
					je.atacar=False

			if not jefe.muriendo:
				jefe.comportamientoJefe(j.getPosition())
			else:
				if jefe.accion == 5:
					jefes.remove(jefe)
					

			instanteFinal = datetime.now()
			tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
			segundos = tiempo.seconds


			eventos=pygame.event.get()

			for event in eventos:
				if event.type == pygame.QUIT:
					fin=True
			
			#eventos del jugador
			j.eventos(balas, eventos)

			#actualizacion de explosiones
			for e in explosiones:
				if(e.animacion==e.lim_animacion):
					explosiones.remove(e)

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


			posibilidad_enemigo=random.randint(0,100)

			#print(posibilidad_enemigo)

			if posibilidad_enemigo in [100]:
				x=j.rect.x
				y=j.rect.y
				#se garantiza que el enemigo no salga a menos de 12px del jugador
				while(abs(x-j.rect.x)<200 or abs(y-j.rect.y)<200):
					x=random.randint(0,Util.ANCHO)
					y=random.randint(0,Util.ALTO)
				coordenadas=[x, y]
				e=Enemigo(coordenadas, imagenesEnemigo)
				enemy=[0,8]
				i=random.randint(0,1)
				e.tipo_enemigo=enemy[i]
				if(e.tipo_enemigo==16):
					e.incremento_caminar=3
					e.incremento_correr=3
				enemigos.add(e)


			#COLISION BALAS CON JEFE
			for b in balas:
				ls_col = pygame.sprite.spritecollide(b, jefes, False)
				for be in ls_col:
					if not be.muriendo:
						if be.vida>0:
							be.vida-=be.daño_bala
						else:
							be.animacion = 9
							be.accion = 0
							be.vida = 0
							be.muriendo = True
							be.vely = 0
							be.velx = 0

					balas.remove(b)


			#COLISION JEFE
			for je in jefes:
				ls_col = pygame.sprite.spritecollide(je, jugadores, False)
				for ju in ls_col:
					if ju.vida-je.daño_ataque>0:
						ju.vida-=je.daño_ataque
					else:
						ju.vida = 0

			#COLISIONES BALAS-ENEMIGOS
			for b in balas:
				ls_col = pygame.sprite.spritecollide(b, enemigos, False)
				for be in ls_col:
					if be.vida>0:
						be.vida-=be.daño_bala
					else:
						#la muerte del enemigo depende del tipo
						if(be.tipo_enemigo==0):
							posibilidad_Botiquin=random.randint(0,1)
							b=Botiquin([be.rect.x,be.rect.y], imagenesBotiquin, posibilidad_Botiquin)
							botiquines.add(b)
						
						elif(be.tipo_enemigo==8):
							None
						elif(be.tipo_enemigo==16):
							None
						elif(be.tipo_enemigo==24):
							e=Explosion([be.rect.x-128, be.rect.y-128], imagenesExplosionRojo, [7,5])
							explosiones.add(e)

						enemigos.remove(be)
					
					balas.remove(b)


			#COLISIONES EXPLOSION-JUGADOR
			for e in explosiones:
				ls_col = pygame.sprite.spritecollide(e, jugadores, False)
				for jugador in ls_col:
					if(jugador.vida > 0):
						jugador.vida-=1


			#COLISIONES DEL ENEMIGO AZUL
			for e in enemigos:
				ls_col = pygame.sprite.spritecollide(e, jugadores, False)
				for jugador in ls_col:
					if(jugador.vida > 0):
						if e.tipo_enemigo==0:
							None
						elif e.tipo_enemigo==24:
							jugador.vida-=1
							x=Explosion([jugador.rect.x-64, jugador.rect.y-64], imagenesExplosionRojo, [7,5])
							explosiones.add(x)
							enemigos.remove(e)
						elif e.tipo_enemigo==16:
							jugador.vida-=1
							x=Explosion([jugador.rect.x-64, jugador.rect.y-64], imagenesExplosionAzul, [7,3])
							explosiones.add(x)
							enemigos.remove(e)


			#COLISIONES BALAS ENEMIGAS - JUGADOR
			for b in balas_enemigas:
				ls_col = pygame.sprite.spritecollide(b, jugadores, False)
				for jugador in ls_col:
					if(jugador.vida > 0):
						jugador.vida-=10
					balas_enemigas.remove(b)


			#COLISIONES PAREDES
			for jugador in jugadores:
				ls_col = pygame.sprite.spritecollide(jugador,  bloques, False)
				for e in ls_col:
					if jugador.inmune:
						None
					else:
						j.vida-=0.5


			#COLISIONES JUGADOR - BOTIQUIN
			for b in botiquines:
				ls_col = pygame.sprite.spritecollide(b, jugadores, False)
				for jugador in ls_col:
					if b.tipo_ayuda==0:
						jugador.vida+=40
					else:
						jugador.inmune=True
						jugador.inicio_inmunidad=datetime.now()
					botiquines.remove(b)


			'''
			inicio = [j.rect.x,j.rect.y]
			end = pygame.mouse.get_pos()
			desplazamiento = Util.angular(end, inicio)
			desplazamiento = [(j.rect.x - 100*desplazamiento[0]+j.rect.width/2),(j.rect.y - 100*desplazamiento[1]+j.rect.height/2)]
			'''
			player_position=[]

			player_position=j.getPosition()



			balas.update()
			jefes.update()
			balas_enemigas.update()
			jugadores.update()
			enemigos.update(player_position, balas_enemigas, imagenesBalasEnemigo)
			explosiones.update()
			pantalla.fill(Util.FONDO)

			bloques.draw(pantalla)

			#se muestran los puntajes
			texto="Vida: "+str(int(j.vida))
			textoPuntaje=fuente.render(texto, 1, Util.BLANCO)
			pantalla.blit(textoPuntaje,[100,20])

			texto="Vida del jefe: "+str(jefe.vida)
			textoPuntaje=fuente.render(texto, 1, Util.BLANCO)
			pantalla.blit(textoPuntaje,[400,20])

			texto="Tiempo: "+str(segundos)
			textoPuntaje=fuente.render(texto, 1, Util.BLANCO)
			pantalla.blit(textoPuntaje,[300,20])

			if j.inmune:
				texto="Inmunidad/Magma: Activada"
				textoPuntaje=fuente.render(texto, 1, Util.BLANCO)
				pantalla.blit(textoPuntaje,[600,20])
			else:
				texto="Inmunidad/Magma: Desactivada"
				textoPuntaje=fuente.render(texto, 1, Util.BLANCO)
				pantalla.blit(textoPuntaje,[600,20])


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
			botiquines.draw(pantalla)
			pygame.display.flip()
			reloj.tick(20)


	def muerte(self):

		fondo = pygame.transform.scale2x( pygame.image.load('niveles/images/Fondo.png'))

		#fuentes de texto
		fuente=pygame.font.Font(None, 20)
		titulos=pygame.font.Font(None, 70)
		reloj=pygame.time.Clock()
		repetir=False

		while True:
			

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button==1:
						pos=pygame.mouse.get_pos()
						if (pos[0]>450 and pos[0]<900) and (pos[1]>400 and pos[1]<470):
							repetir=True
						elif (pos[0]>600 and pos[0]<900) and (pos[1]>500 and pos[1]<570):
							pygame.quit()
							sys.exit()


			if repetir:
				break

			self.pantalla.blit(fondo,[0,0])
			#self.pantalla.fill(Util.BLANCO)

			texto="Game Over"
			textoPuntaje=titulos.render(texto, 1, Util.AMARILLO)
			self.pantalla.blit(textoPuntaje,[520,200])

			texto="Volver a intentar"
			textoPuntaje=titulos.render(texto, 1, Util.BLANCO)
			self.pantalla.blit(textoPuntaje,[450,400])

			texto="Salir"
			textoPuntaje=titulos.render(texto, 1, Util.BLANCO)
			self.pantalla.blit(textoPuntaje,[600,500])

			pygame.display.flip()
			reloj.tick(20)


	def nivel_finalizado(self):
		fondo = pygame.transform.scale2x( pygame.image.load('niveles/images/Fondo.png'))
		#fuentes de texto
		fuente=pygame.font.Font(None, 20)
		titulos=pygame.font.Font(None, 70)
		reloj=pygame.time.Clock()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button==1:
						pos=pygame.mouse.get_pos()
					if (pos[0]>450 and pos[0]<900) and (pos[1]>400 and pos[1]<470):
						self.nivel_aprobado=True
					elif (pos[0]>600 and pos[0]<900) and (pos[1]>500 and pos[1]<570):
						pygame.quit()
						sys.exit()


			if self.nivel_aprobado:
				break
			
			self.pantalla.blit(fondo,[0,0])				
			#self.pantalla.fill(Util.BLANCO)

			texto="Fleicitaciones, ahora el mundo es un lugar más seguro"
			textoPuntaje=titulos.render(texto, 1, Util.AMARILLO)
			self.pantalla.blit(textoPuntaje,[30,200])

			texto="Volver a jugar"
			textoPuntaje=titulos.render(texto, 1, Util.BLANCO)
			self.pantalla.blit(textoPuntaje,[500,400])

			texto="Salir"
			textoPuntaje=titulos.render(texto, 1, Util.BLANCO)
			self.pantalla.blit(textoPuntaje,[600,500])

			pygame.display.flip()
			reloj.tick(20)

			pygame.display.flip()
			reloj.tick(20)