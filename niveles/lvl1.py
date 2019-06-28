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

class lvl1:
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

		#configuracion de los Botiquines
		img_Botiquin=pygame.image.load('niveles/images/botiquin.png')
		imagenesBotiquin=Util.cut(img_Botiquin, 2, 1, 32, 24)

		self.pantalla=pantalla
		self.nivel_aprobado = False
		#self.fondo = pygame.transform.scale2x( pygame.image.load('niveles/images/Fondo.png'))

		#grupos
		jugadores=pygame.sprite.Group()
		balas=pygame.sprite.Group()
		enemigos=pygame.sprite.Group()
		explosiones=pygame.sprite.Group()
		balas_enemigas=pygame.sprite.Group()
		botiquines=pygame.sprite.Group()
		bloques=pygame.sprite.Group()

		bloques = Util.mapear('niveles/Mapas/mapa1.map')

		#jugador
		j=Jugador(Util.CENTRO,imagenesJugador)
		jugadores.add(j)

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
				j.vida-=1

			if j.vida<=0:
				self.muerte()
				break

			instanteFinal = datetime.now()
			tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
			segundos = tiempo.seconds

			if segundos>95 and len(enemigos)==0:
				self.nivel_finalizado()
				break
			
			#oleadas de enemigos
			if segundos<20:
				posibilidad_enemigo=random.randint(0,100)

				#print(posibilidad_enemigo)

				if posibilidad_enemigo in [100,50,0]:
					x=j.rect.x
					y=j.rect.y
					#se garantiza que el enemigo no salga a menos de 12px del jugador
					while(abs(x-j.rect.x)<200 or abs(y-j.rect.y)<200):
						x=random.randint(0,Util.ANCHO)
						y=random.randint(0,Util.ALTO)
					coordenadas=[x, y]
					e=Enemigo(coordenadas, imagenesEnemigo)
					e.tipo_enemigo=2*8
					if(e.tipo_enemigo==16):
						e.incremento_caminar=3
						e.incremento_correr=3
					enemigos.add(e)

			elif segundos>25 and segundos<45:
				posibilidad_enemigo=random.randint(0,100)

				#print(posibilidad_enemigo)

				if posibilidad_enemigo in [100,50,0]:
					x=j.rect.x
					y=j.rect.y
					#se garantiza que el enemigo no salga a menos de 12px del jugador
					while(abs(x-j.rect.x)<200 or abs(y-j.rect.y)<200):
						x=random.randint(0,Util.ANCHO)
						y=random.randint(0,Util.ALTO)
					coordenadas=[x, y]
					e=Enemigo(coordenadas, imagenesEnemigo)
					e.tipo_enemigo=random.randint(2,3)*8
					if(e.tipo_enemigo==16):
						e.incremento_caminar=3
						e.incremento_correr=3
					enemigos.add(e)

			elif segundos>50 and segundos<70:
				posibilidad_enemigo=random.randint(0,100)

				#print(posibilidad_enemigo)

				if posibilidad_enemigo in [100,50,0]:
					x=j.rect.x
					y=j.rect.y
					#se garantiza que el enemigo no salga a menos de 12px del jugador
					while(abs(x-j.rect.x)<200 or abs(y-j.rect.y)<200):
						x=random.randint(0,Util.ANCHO)
						y=random.randint(0,Util.ALTO)
					coordenadas=[x, y]
					e=Enemigo(coordenadas, imagenesEnemigo)
					e.tipo_enemigo=random.randint(0,3)*8
					if(e.tipo_enemigo==16):
						e.incremento_caminar=3
						e.incremento_correr=3
					enemigos.add(e)

			elif segundos>75 and segundos<95:
				posibilidad_enemigo=random.randint(0,100)

				#print(posibilidad_enemigo)

				if posibilidad_enemigo in [100,50,0]:
					x=j.rect.x
					y=j.rect.y
					#se garantiza que el enemigo no salga a menos de 12px del jugador
					while(abs(x-j.rect.x)<200 or abs(y-j.rect.y)<200):
						x=random.randint(0,Util.ANCHO)
						y=random.randint(0,Util.ALTO)
					coordenadas=[x, y]
					e=Enemigo(coordenadas, imagenesEnemigo)
					e.tipo_enemigo=random.randint(1,3)*8
					if(e.tipo_enemigo==16):
						e.incremento_caminar=3
						e.incremento_correr=3
					enemigos.add(e)

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


			#COLISIONES JUGADOR - Botiquin
			for b in botiquines:
				ls_col = pygame.sprite.spritecollide(b, jugadores, False)
				for jugador in ls_col:
					if b.tipo_ayuda==0:
						jugador.vida+=40
					else:
						jugador.inmune=True
						jugador.inicio_inmunidad=datetime.now()
					botiquines.remove(b)


			#COlISIONES PAREDES
			for jugador in jugadores:
				ls_col = pygame.sprite.spritecollide(jugador,  bloques, False)
				for e in ls_col:
					if jugador.inmune:
						None
					else:
						j.vida-=1
			'''
			inicio = [j.rect.x,j.rect.y]
			end = pygame.mouse.get_pos()
			desplazamiento = Util.angular(end, inicio)
			desplazamiento = [(j.rect.x - 100*desplazamiento[0]+j.rect.width/2),(j.rect.y - 100*desplazamiento[1]+j.rect.height/2)]
			'''
			player_position=[]

			
			player_position=j.getPosition()
			


			balas.update()
			balas_enemigas.update()
			jugadores.update()
			enemigos.update(player_position, balas_enemigas, imagenesBalasEnemigo)
			explosiones.update()
			pantalla.fill(Util.FONDO)

			bloques.draw(pantalla)

			#pantalla.blit(self.fondo,[0,0])
			#se muestran los puntajes
			texto="Vida: "+str(j.vida)
			textoPuntaje=fuente.render(texto, 1, Util.BLANCO)
			pantalla.blit(textoPuntaje,[100,20])


			texto="Tiempo: "+str(segundos)
			textoPuntaje=fuente.render(texto, 1, Util.BLANCO)
			pantalla.blit(textoPuntaje,[300,20])

			if j.inmune:
				texto="Inmunidad/Magma: Activada"
				textoPuntaje=fuente.render(texto, 1, Util.BLANCO)
				pantalla.blit(textoPuntaje,[500,20])
			else:
				texto="Inmunidad/Magma: Desactida"
				textoPuntaje=fuente.render(texto, 1, Util.BLANCO)
				pantalla.blit(textoPuntaje,[500,20])

			if(segundos>20 and segundos<25):
				texto="Segunda oleada: "+str(25-segundos)
				textoPuntaje=titulos.render(texto, 1, Util.BLANCO)
				pantalla.blit(textoPuntaje,[100,300])

			if(segundos>45 and segundos<50):
				texto="Tercera oleada: "+str(50-segundos)
				textoPuntaje=titulos.render(texto, 1, Util.BLANCO)
				pantalla.blit(textoPuntaje,[100,300])


			if(segundos>70 and segundos<75):
				texto="Cuarta oleada: "+str(75-segundos)
				textoPuntaje=titulos.render(texto, 1, Util.BLANCO)
				pantalla.blit(textoPuntaje,[100,300])

			
			'''
			pygame.draw.line(pantalla, Util.ROJO, [int(j.rect.x+j.rect.width/2), int(j.rect.y+j.rect.height/2)], desplazamiento, 1)
			pygame.draw.circle(pantalla, Util.NEGRO, [int(j.rect.x+j.rect.width/2), int(j.rect.y+j.rect.height/2)], 100, 1)
			'''
			
			
			jugadores.draw(pantalla)            
			balas.draw(pantalla)
			balas_enemigas.draw(pantalla)
			enemigos.draw(pantalla)
			explosiones.draw(pantalla)
			botiquines.draw(pantalla)
			pygame.display.flip()
			reloj.tick(20)


	def muerte(self):
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
						if (pos[0]>600 and pos[0]<900) and (pos[1]>500 and pos[1]<570):
							repetir=True
						elif (pos[0]>600 and pos[0]<900) and (pos[1]>600 and pos[1]<670):
							pygame.quit()
							sys.exit()


			if repetir:
				break

			self.pantalla.fill(Util.BLANCO)

			texto="Game Over"
			textoPuntaje=titulos.render(texto, 1, Util.NEGRO)
			self.pantalla.blit(textoPuntaje,[600,300])

			texto="Volver a intentar"
			textoPuntaje=titulos.render(texto, 1, Util.NEGRO)
			self.pantalla.blit(textoPuntaje,[600,500])

			texto="Salir"
			textoPuntaje=titulos.render(texto, 1, Util.NEGRO)
			self.pantalla.blit(textoPuntaje,[600,600])

			pygame.display.flip()
			reloj.tick(20)


	def nivel_finalizado(self):
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
						if (pos[0]>600 and pos[0]<900) and (pos[1]>500 and pos[1]<570):
							self.nivel_aprobado=True
						elif (pos[0]>700 and pos[0]<900) and (pos[1]>600 and pos[1]<670):
							pygame.quit()
							sys.exit()


			if self.nivel_aprobado:
				break

			self.pantalla.fill(Util.BLANCO)

			texto="Nivel completado"
			textoPuntaje=titulos.render(texto, 1, Util.NEGRO)
			self.pantalla.blit(textoPuntaje,[600,300])

			texto="Siguiente nivel"
			textoPuntaje=titulos.render(texto, 1, Util.NEGRO)
			self.pantalla.blit(textoPuntaje,[600,500])

			texto="Salir"
			textoPuntaje=titulos.render(texto, 1, Util.NEGRO)
			self.pantalla.blit(textoPuntaje,[700,600])

			pygame.display.flip()
			reloj.tick(20)