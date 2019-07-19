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
from niveles.clases.Hud import *
from niveles.clases.NPC import *
from niveles.clases.Bob import *
from Util import *

class lvl1:
	def __init__(self, pantalla, mapa):
		#configuracion del jugador
		img_juagador= pygame.image.load('niveles/images/liche.png')
		imagenesJugador=Util.cut(img_juagador, 9, 21, 29, 33)

		#configuracion del boss
		img_boss= pygame.image.load('niveles/images/el_otro_boss.png')
		imagenesBoss=Util.cut(img_boss, 19, 8, 64, 64)

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
		img_botiquin=pygame.image.load('niveles/images/botiquin.png')
		imagenesBotiquin=Util.cut(img_botiquin, 2, 1, 32, 24)

		#configuracion de NPC 1
		img_NPCreaper= pygame.image.load('niveles/images/NPCreaper.png')
		imagenesNPCreaper = Util.cut(img_NPCreaper, 3, 1, 64, 72)

		img_enemigo= pygame.transform.scale2x(pygame.image.load('niveles/images/enemigos.png'))
		imagenesEnemigo=Util.cut(img_enemigo, 7, 32, 48, 48)

		img_Bob = pygame.transform.scale(pygame.image.load('niveles/images/el_otro_boss.png'),[1824,768])
		imagenesBob = Util.cut(img_Bob, 19, 8, 96, 96)

		img_Mino = pygame.image.load('niveles/images/boss.png')
		imagenesMino = Util.cut(img_Mino, 9, 20, 96, 96)

		dialogos = pygame.image.load('niveles/images/dialogos.png')
		imagenesDialogos = Util.cut(dialogos, 4, 1, 492, 268)

		HUD=Hud(pantalla)

		self.pantalla=pantalla
		self.nivel_aprobado = False
		self.fondo = pygame.transform.scale( pygame.image.load('niveles/images/Fondo.png'), Util.TAMAÑOPANTALLA)
		self.habitacionActual=[2,2]
		self.mapa = mapa

		#grupos
		jugadores=pygame.sprite.Group()
		balas=pygame.sprite.Group()
		enemigos=pygame.sprite.Group()
		explosiones=pygame.sprite.Group()
		balas_enemigas=pygame.sprite.Group()
		botiquines=pygame.sprite.Group()
		NPCreapers = pygame.sprite.Group()
		bosses = pygame.sprite.Group()
		llaves = pygame.sprite.Group()
		bobs = pygame.sprite.Group()
		minos = pygame.sprite.Group()
		abismos = pygame.sprite.Group()

		mapita = Util.mapear(self.habitacionActual, self.mapa, imagenesEnemigo, imagenesNPCreaper, imagenesBoss)

		bloques = mapita[0]
		piso = mapita[1]
		magma = mapita[2]
		agua = mapita[3]
		pasto = mapita[4]
		puertas = mapita[5]
		enemigos = mapita[6]
		NPCreapers = mapita[7]
		bosses = mapita[8]
		llaves = mapita[9]
		bobs = mapita[10]
		habitacionBoss=mapita[10]
		abismos = mapita[11]

		#jugador
		j=Jugador(Util.CENTRO,imagenesJugador, self.habitacionActual)
		#bob = Jefe_Bob(Util.CENTRO, imagenesBob)
		#mino = Jefe(Util.CENTRO, imagenesMino)
		#minos.add(mino)
		#bobs.add(bob)
		jugadores.add(j)
		#variables necesarias
		fin=False
		reloj=pygame.time.Clock()
		instanteInicial = datetime.now()

		buscarLlave = True

		#fuentes de texto
		fuente=pygame.font.Font(None, 30)
		titulos=pygame.font.Font(None, 70)

		dialogo = 0

		#juego
		while not fin:

			
			mapita = Util.mapear(self.habitacionActual, self.mapa, imagenesEnemigo, imagenesNPCreaper, imagenesBoss)

			bloques = mapita[0]
			piso = mapita[1]
			magma = mapita[2]
			agua = mapita[3]
			pasto = mapita[4]
			puertas = mapita[5]
			abismos = mapita[11]


			if j.vida>100:
				j.vida-=0.1

			if j.vida<=0:
				self.muerte()
				break


			instanteFinal = datetime.now()
			tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
			segundos = tiempo.seconds

			#if segundos < 20:
				#m = Muerte(Util.CENTRO, imagenesMuerte)

######################### MINOTAURO ##########################################################################
##############################################################################################################

			#COMPORTAMIENTO POR PROXIMIDAD MINOTAURO
			for je in minos:
				if pygame.sprite.collide_circle_ratio(0.5)(j,je):
					je.atacar=True
				else:
					je.atacar=False

			#COLISION ATAQUES MINOTAURO CON JUGADOR
			for je in minos:
				ls_col = pygame.sprite.spritecollide(je, jugadores, False)
				for ju in ls_col:
					if ju.vida-je.daño_ataque>0:
						ju.vida-=je.daño_ataque
					else:
						ju.vida = 0

			#COLISION BALAS CON MINOTAURO
			for b in balas:
				ls_col = pygame.sprite.spritecollide(b, minos, False)
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

			#CONTROL VIDA MINOTAURO
			for minon in minos:
				if not minon.muriendo:
					minon.comportamientoJefe(j.getPosition())
				else:
					if minon.accion == 5:
						minos.remove(minon)
						nivel_finalizado()

######################### BOB ################################################################################
##############################################################################################################

			#COMPORTAMIENTO POR PROXIMIDAD BOB
			for je in bobs:
				if pygame.sprite.collide_circle_ratio(0.5)(j,je):
					je.atacar=True
				else:
					je.atacar=False

			#COLISION ATAQUES MINOTAURO CON BOB
			for je in bobs:
				ls_col = pygame.sprite.spritecollide(je, jugadores, False)
				for ju in ls_col:
					if ju.vida-je.daño_ataque>0:
						ju.vida-=je.daño_ataque
					else:
						ju.vida = 0

			#COLISION BALAS CON BOB
			for b in balas:
				ls_col = pygame.sprite.spritecollide(b, bobs, False)
				for be in ls_col:
					if not be.muriendo:
						if be.vida>0:
							be.vida-=be.daño_bala
						else:
							be.animacion = 3
							be.accion = 0
							be.vida = 0
							be.muriendo = True
							be.vely = 0
							be.velx = 0

					balas.remove(b)

			#CONTROL VIDA BOB
			for bobn in bobs:
				if not bobn.muriendo:
					bobn.comportamientoJefe_Bob(j.getPosition())
				else:
					if bobn.accion == 18:
						bobs.remove(bobn)

##############################################################################################################
##############################################################################################################

			if len(enemigos)!=0:
				if j.rect.x > (Util.ANCHO - j.rect.width - 64):
					j.velx = 0
					j.rect.x = Util.ANCHO  - j.rect.width - 64
				if j.rect.x < 64:
					j.velx = 0
					j.rect.x = 64
				if j.rect.y > (Util.ALTO  - j.rect.height - 64):
					j.vely = 0
					j.rect.y = Util.ALTO - j.rect.height - 64
				if j.rect.y < 64:
					j.vely = 0
					j.rect.y = 64
				
			"""
			#oleadas de enemigos
			if segundos<20:
				posibilidad_enemigo=random.randint(0,100)
				#print(posibilidad_enemigo)
				if posibilidad_enemigo in [100,50,25,0]:
					x=j.rect.x
					y=j.rect.y
					#se garantiza que el enemigo no salga a menos de 200px del jugador
					while(abs(x-j.rect.x)<200 or abs(y-j.rect.y)<200):
						x=random.randint(64,Util.ANCHO-88)
						y=random.randint(64,Util.ALTO-88)
					coordenadas=[x, y]
					#se garantiza que el enemigo no aparezca sobre un muro
					crear=False
					for b in bloques:
						if ((coordenadas[0] > b.rect.left and coordenadas[0] < b.rect.right) and (coordenadas[1] > b.rect.top and coordenadas[1] < b.rect.bottom)):
							None
						else:
							crear=True
					if crear:
						e=Enemigo(coordenadas, imagenesEnemigo)
						e.tipo_enemigo=2*8
						if(e.tipo_enemigo==16):
							e.incremento_caminar=3
							e.incremento_correr=3
						enemigos.add(e)
			elif segundos>25 and segundos<45:
				posibilidad_enemigo=random.randint(0,100)
				#print(posibilidad_enemigo)
				if posibilidad_enemigo in [100,50,25,0]:
					x=j.rect.x
					y=j.rect.y
					#se garantiza que el enemigo no salga a menos de 12px del jugador
					while(abs(x-j.rect.x)<200 or abs(y-j.rect.y)<200):
						x=random.randint(64,Util.ANCHO-88)
						y=random.randint(64,Util.ALTO-88)
					coordenadas=[x, y]
					#se garantiza que el enemigo no aparezca sobre un muro
					crear=False
					for b in bloques:
						if ((coordenadas[0] > b.rect.left and coordenadas[0] < b.rect.right) and (coordenadas[1] > b.rect.top and coordenadas[1] < b.rect.bottom)):
							None
						else:
							crear=True
					if crear:
						e=Enemigo(coordenadas, imagenesEnemigo)
						e.tipo_enemigo=random.randint(2,3)*8
						if(e.tipo_enemigo==16):
							e.incremento_caminar=3
							e.incremento_correr=3
						enemigos.add(e)
			elif segundos>50 and segundos<70:
				posibilidad_enemigo=random.randint(0,100)
				#print(posibilidad_enemigo)
				if posibilidad_enemigo in [100,50,25,0]:
					x=j.rect.x
					y=j.rect.y
					#se garantiza que el enemigo no salga a menos de 12px del jugador
					while(abs(x-j.rect.x)<200 or abs(y-j.rect.y)<200):
						x=random.randint(64,Util.ANCHO-88)
						y=random.randint(64,Util.ALTO-88)
					coordenadas=[x, y]
					#se garantiza que el enemigo no aparezca sobre un muro
					crear=False
					for b in bloques:
						if ((coordenadas[0] > b.rect.left and coordenadas[0] < b.rect.right) and (coordenadas[1] > b.rect.top and coordenadas[1] < b.rect.bottom) and (coordenadas[0] < b.rect.left-24)):
							None
						else:
							crear=True
					if crear:
						e=Enemigo(coordenadas, imagenesEnemigo)
						e.tipo_enemigo=random.randint(0,3)*8
						if(e.tipo_enemigo==16):
							e.incremento_caminar=3
							e.incremento_correr=3
						enemigos.add(e)
			elif segundos>75 and segundos<95:
				posibilidad_enemigo=random.randint(0,100)
				#print(posibilidad_enemigo)
				if posibilidad_enemigo in [100,50,25,0]:
					x=j.rect.x
					y=j.rect.y
					#se garantiza que el enemigo no salga a menos de 12px del jugador
					while(abs(x-j.rect.x)<200 or abs(y-j.rect.y)<200):
						x=random.randint(64,Util.ANCHO-88)
						y=random.randint(64,Util.ALTO-88)
					coordenadas=[x, y]
					#se garantiza que el enemigo no aparezca sobre un muro
					crear=False
					for b in bloques:
						if ((coordenadas[0] > b.rect.left and coordenadas[0] < b.rect.right) and (coordenadas[1] > b.rect.top and coordenadas[1] < b.rect.bottom)):
							None
						else:
							crear=True
					if crear:
						e=Enemigo(coordenadas, imagenesEnemigo)
						e.tipo_enemigo=random.randint(1,3)*8
						if(e.tipo_enemigo==16):
							e.incremento_caminar=3
							e.incremento_correr=3
						enemigos.add(e)
			"""

			eventos=pygame.event.get()

			for e in eventos:
				if e.type==pygame.KEYDOWN:
					if e.key == pygame.K_e:
						if dialogo<3:
							dialogo+=1

			for event in eventos:
				if event.type == pygame.QUIT:
					fin=True
			#eventos del jugador
			j.eventos(balas, eventos)
			#m.eventos(eventos)
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


			#COLISIONES BALAS ENEMIGAS - MUROS
			for b in balas_enemigas:
				ls_col = pygame.sprite.spritecollide(b, bloques, False)
				for jugador in ls_col:
					balas_enemigas.remove(b)


			#COLISIONES BALAS - MUROS
			for b in balas:
				ls_col = pygame.sprite.spritecollide(b, bloques, False)
				for jugador in ls_col:
					balas.remove(b)


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


			#COlISIONES MAGMA
			for jugador in jugadores:
				ls_col = pygame.sprite.spritecollide(jugador,  magma, False)
				for e in ls_col:
					jugador.burn.play()
					if jugador.inmune:
						None
					else:
						j.vida-=0.5

			#colisiones del jugador con los muros
			for jugador in jugadores:
				ls_col = pygame.sprite.spritecollide(jugador,  bloques, False)
				for e in ls_col:
					#print(""+str(jugador.rect.top) + " " + str(e.rect.bottom))
					if ((jugador.velx == 0 and jugador.vely > 0) and (jugador.rect.bottom <= e.rect.top+10) and (len(ls_col)==2) and ((ls_col[0].rect.right==ls_col[1].rect.right) and ((ls_col[0].rect.bottom==ls_col[1].rect.top) or (ls_col[1].rect.bottom==ls_col[0].rect.top)))):
						if jugador.rect.top==e.rect.bottom:
						 	None
						else:
							jugador.rect.bottom=e.rect.top
					elif ((jugador.velx == 0 and jugador.vely < 0) and (jugador.rect.top >= e.rect.bottom-10) and (len(ls_col)==2) and ((ls_col[0].rect.right==ls_col[1].rect.right) and ((ls_col[0].rect.bottom==ls_col[1].rect.top) or (ls_col[1].rect.bottom==ls_col[0].rect.top)))):
						if jugador.rect.bottom==e.rect.top:
						 	None
						else:
							jugador.rect.top=e.rect.bottom
					elif ((jugador.velx < 0 and jugador.vely == 0) and (jugador.rect.left >= e.rect.right-10) and (len(ls_col)==2) and ((ls_col[0].rect.top==ls_col[1].rect.top) and ((ls_col[0].rect.left==ls_col[1].rect.right) or (ls_col[1].rect.left==ls_col[0].rect.right)))):
						if jugador.rect.right==e.rect.left:
						 	None
						else:
							jugador.rect.left=e.rect.right
					elif ((jugador.velx > 0 and jugador.vely == 0) and (jugador.rect.right <= e.rect.left+10) and (len(ls_col)==2) and ((ls_col[0].rect.top==ls_col[1].rect.top) and ((ls_col[0].rect.left==ls_col[1].rect.right) or (ls_col[1].rect.left==ls_col[0].rect.right)))):
						if jugador.rect.left==e.rect.right:
						 	None
						else:
							jugador.rect.right=e.rect.left
					elif ((jugador.velx == 0 and jugador.vely > 0) and (jugador.rect.bottom <= e.rect.top+10)):
						jugador.rect.bottom = e.rect.top
					elif ((jugador.velx < 0 and jugador.vely > 0) and (jugador.rect.bottom <= e.rect.top+10)):
						jugador.rect.bottom = e.rect.top
					elif ((jugador.velx < 0 and jugador.vely > 0) and (jugador.rect.left >= e.rect.right-10)):
						jugador.rect.left = e.rect.right
					elif ((jugador.velx < 0 and jugador.vely == 0) and (jugador.rect.left >= e.rect.right-10)):
						jugador.rect.left = e.rect.right
					elif ((jugador.velx < 0 and jugador.vely < 0) and (jugador.rect.left >= e.rect.right-10)):
						jugador.rect.left = e.rect.right
					elif ((jugador.velx < 0 and jugador.vely < 0) and (jugador.rect.top >= e.rect.bottom-10)):
						jugador.rect.top = e.rect.bottom
					elif ((jugador.velx == 0 and jugador.vely < 0) and (jugador.rect.top >= e.rect.bottom-10)):
						jugador.rect.top = e.rect.bottom
					elif ((jugador.velx > 0 and jugador.vely < 0) and (jugador.rect.top >= e.rect.bottom-10)):
						jugador.rect.top = e.rect.bottom
					elif ((jugador.velx > 0 and jugador.vely < 0) and (jugador.rect.right <= e.rect.left+10)):
						jugador.rect.right = e.rect.left
					elif ((jugador.velx > 0 and jugador.vely == 0) and (jugador.rect.right <= e.rect.left+10)):
						jugador.rect.right = e.rect.left
					elif ((jugador.velx > 0 and jugador.vely > 0) and (jugador.rect.right <= e.rect.left+10)):
						jugador.rect.right = e.rect.left
					elif ((jugador.velx > 0 and jugador.vely > 0) and (jugador.rect.bottom <= e.rect.top+10)):
						jugador.rect.bottom = e.rect.top

			for jugador in jugadores:
				ls_col = pygame.sprite.spritecollide(jugador,  bloques, False)
				for e in ls_col:
					#print(""+str(jugador.rect.top) + " " + str(e.rect.bottom))
					if ((jugador.velx == 0 and jugador.vely > 0) and (jugador.rect.bottom <= e.rect.top+60) and (len(ls_col)==2) and ((ls_col[0].rect.right==ls_col[1].rect.right) and ((ls_col[0].rect.bottom==ls_col[1].rect.top) or (ls_col[1].rect.bottom==ls_col[0].rect.top)))):
						jugador.rect.y+=30
					elif ((jugador.velx == 0 and jugador.vely < 0) and (jugador.rect.top >= e.rect.bottom-60) and (len(ls_col)==2) and ((ls_col[0].rect.right==ls_col[1].rect.right) and ((ls_col[0].rect.bottom==ls_col[1].rect.top) or (ls_col[1].rect.bottom==ls_col[0].rect.top)))):
						jugador.rect.y-=30
					elif ((jugador.velx < 0 and jugador.vely == 0) and (jugador.rect.left >= e.rect.right-60) and (len(ls_col)==2) and ((ls_col[0].rect.top==ls_col[1].rect.top) and ((ls_col[0].rect.left==ls_col[1].rect.right) or (ls_col[1].rect.left==ls_col[0].rect.right)))):
						jugador.rect.x-=30
					elif ((jugador.velx > 0 and jugador.vely == 0) and (jugador.rect.right <= e.rect.left+60) and (len(ls_col)==2) and ((ls_col[0].rect.top==ls_col[1].rect.top) and ((ls_col[0].rect.left==ls_col[1].rect.right) or (ls_col[1].rect.left==ls_col[0].rect.right)))):
						jugador.rect.x+=30
					elif ((jugador.velx == 0 and jugador.vely > 0) and (jugador.rect.bottom <= e.rect.top+60)):
						jugador.rect.bottom = e.rect.top
					elif ((jugador.velx < 0 and jugador.vely > 0) and (jugador.rect.bottom <= e.rect.top+60)):
						jugador.rect.bottom = e.rect.top
					elif ((jugador.velx < 0 and jugador.vely > 0) and (jugador.rect.left >= e.rect.right-60)):
						jugador.rect.left = e.rect.right
					elif ((jugador.velx < 0 and jugador.vely == 0) and (jugador.rect.left >= e.rect.right-60)):
						jugador.rect.left = e.rect.right
					elif ((jugador.velx < 0 and jugador.vely < 0) and (jugador.rect.left >= e.rect.right-60)):
						jugador.rect.left = e.rect.right
					elif ((jugador.velx < 0 and jugador.vely < 0) and (jugador.rect.top >= e.rect.bottom-60)):
						jugador.rect.top = e.rect.bottom
					elif ((jugador.velx == 0 and jugador.vely < 0) and (jugador.rect.top >= e.rect.bottom-60)):
						jugador.rect.top = e.rect.bottom
					elif ((jugador.velx > 0 and jugador.vely < 0) and (jugador.rect.top >= e.rect.bottom-60)):
						jugador.rect.top = e.rect.bottom
					elif ((jugador.velx > 0 and jugador.vely < 0) and (jugador.rect.right <= e.rect.left+60)):
						jugador.rect.right = e.rect.left
					elif ((jugador.velx > 0 and jugador.vely == 0) and (jugador.rect.right <= e.rect.left+60)):
						jugador.rect.right = e.rect.left
					elif ((jugador.velx > 0 and jugador.vely > 0) and (jugador.rect.right <= e.rect.left+60)):
						jugador.rect.right = e.rect.left
					elif ((jugador.velx > 0 and jugador.vely > 0) and (jugador.rect.bottom <= e.rect.top+60)):
						jugador.rect.bottom = e.rect.top


			#colisiones de los dinosaurios con los murus
			for dinosaurio in enemigos:
				ls_col = pygame.sprite.spritecollide(dinosaurio,  bloques, False)
				for e in ls_col:
					if ((dinosaurio.velx == 0 and dinosaurio.vely > 0) and (dinosaurio.rect.bottom <= e.rect.top+10) and (len(ls_col)==2) and ((ls_col[0].rect.right==ls_col[1].rect.right) and ((ls_col[0].rect.bottom==ls_col[1].rect.top) or (ls_col[1].rect.bottom==ls_col[0].rect.top)))):
						dinosaurio.rect.y+=7
					elif ((dinosaurio.velx == 0 and dinosaurio.vely < 0) and (dinosaurio.rect.top >= e.rect.bottom-10) and (len(ls_col)==2) and ((ls_col[0].rect.right==ls_col[1].rect.right) and ((ls_col[0].rect.bottom==ls_col[1].rect.top) or (ls_col[1].rect.bottom==ls_coaaaaaal[0].rect.top)))):
						dinosaurio.rect.y-=7
					elif ((dinosaurio.velx < 0 and dinosaurio.vely == 0) and (dinosaurio.rect.left >= e.rect.right-10) and (len(ls_col)==2) and ((ls_col[0].rect.top==ls_col[1].rect.top) and ((ls_col[0].rect.left==ls_col[1].rect.right) or (ls_col[1].rect.left==ls_col[0].rect.right)))):
						dinosaurio.rect.x-=7
					elif ((dinosaurio.velx > 0 and dinosaurio.vely == 0) and (dinosaurio.rect.right <= e.rect.left+10) and (len(ls_col)==2) and ((ls_col[0].rect.top==ls_col[1].rect.top) and ((ls_col[0].rect.left==ls_col[1].rect.right) or (ls_col[1].rect.left==ls_col[0].rect.right)))):
						dinosaurio.rect.x+=7
					elif ((dinosaurio.velx > 0 and dinosaurio.vely > 0) and (dinosaurio.rect.bottom <= e.rect.top+10)):
						dinosaurio.rect.bottom = e.rect.top
					elif ((dinosaurio.velx == 0 and dinosaurio.vely > 0) and (dinosaurio.rect.bottom <= e.rect.top+10)):
						dinosaurio.rect.bottom = e.rect.top
					elif ((dinosaurio.velx < 0 and dinosaurio.vely > 0) and (dinosaurio.rect.bottom <= e.rect.top+10)):
						dinosaurio.rect.bottom = e.rect.top
					elif ((dinosaurio.velx < 0 and dinosaurio.vely > 0) and (dinosaurio.rect.left >= e.rect.right-10)):
						dinosaurio.rect.left = e.rect.right
					elif ((dinosaurio.velx < 0 and dinosaurio.vely == 0) and (dinosaurio.rect.left >= e.rect.right-10)):
						dinosaurio.rect.left = e.rect.right
					elif ((dinosaurio.velx < 0 and dinosaurio.vely < 0) and (dinosaurio.rect.left >= e.rect.right-10)):
						dinosaurio.rect.left = e.rect.right
					elif ((dinosaurio.velx < 0 and dinosaurio.vely < 0) and (dinosaurio.rect.top >= e.rect.bottom-10)):
						dinosaurio.rect.top = e.rect.bottom
					elif ((dinosaurio.velx == 0 and dinosaurio.vely < 0) and (dinosaurio.rect.top >= e.rect.bottom-10)):
						dinosaurio.rect.top = e.rect.bottom
					elif ((dinosaurio.velx > 0 and dinosaurio.vely < 0) and (dinosaurio.rect.top >= e.rect.bottom-10)):
						dinosaurio.rect.top = e.rect.bottom
					elif ((dinosaurio.velx > 0 and dinosaurio.vely < 0) and (dinosaurio.rect.right <= e.rect.left+10)):
						dinosaurio.rect.right = e.rect.left
					elif ((dinosaurio.velx > 0 and dinosaurio.vely == 0) and (dinosaurio.rect.right <= e.rect.left+10)):
						dinosaurio.rect.right = e.rect.left
					elif ((dinosaurio.velx > 0 and dinosaurio.vely > 0) and (dinosaurio.rect.right <= e.rect.left+10)):
						dinosaurio.rect.right = e.rect.left


			#buscando la llave
			for j in jugadores:
				ls_col = pygame.sprite.spritecollide(j, llaves, True)
				for jugador in ls_col:
					buscarLlave=False

			'''
			inicio = [j.rect.x,j.rect.y]
			end = pygame.mouse.get_pos()
			desplazamiento = Util.angular(end, inicio)
			desplazamiento = [(j.rect.x - 100*desplazamiento[0]+j.rect.width/2),(j.rect.y - 100*desplazamiento[1]+j.rect.height/2)]
			'''
			player_position=[]


			player_position=j.getPosition()



			balas.update()
			bobs.update()
			minos.update()
			bosses.update()
			NPCreapers.update()
			balas_enemigas.update()

			enemigos.update(j.getPosition(), balas_enemigas, imagenesBalasEnemigo)
			explosiones.update()
			pantalla.fill(Util.FONDO)
			pantalla.blit(self.fondo,[0,0])
			#print(bloques)
			piso.draw(pantalla)
			magma.draw(pantalla)
			agua.draw(pantalla)
			pasto.draw(pantalla)
			bloques.draw(pantalla)
			puertas.draw(pantalla)

			enemigos, NPCreapers, bosses, llaves, botiquines, bobs, habitacionBoss = j.update(bloques, enemigos, bosses, self.mapa, imagenesEnemigo, imagenesNPCreaper, NPCreapers, imagenesBoss, llaves, botiquines, bobs)
			
			if habitacionBoss and buscarLlave:
				if j.rect.y < 64:
					j.rect.y -= 64
					enemigos, NPCreapers, bosses, llaves, botiquines, bobs, habitacionBoss = j.update(bloques, enemigos, bosses, self.mapa, imagenesEnemigo, imagenesNPCreaper, NPCreapers, imagenesBoss, llaves, botiquines, bobs)
					texto="Necesitas la llave para acceder a esta habitación"
					textoPuntaje=titulos.render(texto, 1, Util.AMARILLO)
					self.pantalla.blit(textoPuntaje,[200,200])
				elif j.rect.x <64:
					j.rect.y- 64
					enemigos, NPCreapers, bosses, llaves, botiquines, bobs, habitacionBoss = j.update(bloques, enemigos, bosses, self.mapa, imagenesEnemigo, imagenesNPCreaper, NPCreapers, imagenesBoss, llaves, botiquines, bobs)
					texto="Necesitas la llave para acceder a esta habitación"
					textoPuntaje=titulos.render(texto, 1, Util.AMARILLO)
					self.pantalla.blit(textoPuntaje,[200,200])
				elif j.rect.y > Util.ALTO -64:
					j.rect.y += 64
					enemigos, NPCreapers, bosses, llaves, botiquines, bobs, habitacionBoss = j.update(bloques, enemigos, bosses, self.mapa, imagenesEnemigo, imagenesNPCreaper, NPCreapers, imagenesBoss, llaves, botiquines, bobs)
					texto="Necesitas la llave para acceder a esta habitación"
					textoPuntaje=titulos.render(texto, 1, Util.AMARILLO)
					self.pantalla.blit(textoPuntaje,[200,200])
				elif j.rect.x > Util.ANCHO-64:
					j.rect.x += 64
					enemigos, NPCreapers, bosses, llaves, botiquines, bobs, habitacionBoss = j.update(bloques, enemigos, bosses, self.mapa, imagenesEnemigo, imagenesNPCreaper, NPCreapers, imagenesBoss, llaves, botiquines, bobs)
					texto="Necesitas la llave para acceder a esta habitación"
					textoPuntaje=titulos.render(texto, 1, Util.AMARILLO)
					self.pantalla.blit(textoPuntaje,[200,200])

			
			for j in jugadores:
				ls_col = pygame.sprite.spritecollide(j, NPCreapers, False)
				for e in ls_col:
					if dialogo in [0,1,3]:
						pantalla.blit(imagenesDialogos[dialogo][0], [e.rect.x - 492, e.rect.y - 268])
					else:
						pantalla.blit(imagenesDialogos[dialogo][0], [j.rect.x, e.rect.y - 268])


			#se muestran los puntajes



			"""texto="Tiempo: "+str(segundos)
			textoPuntaje=fuente.render(texto, 1, Util.BLANCO)
			pantalla.blit(textoPuntaje,[300,20])"""



			"""
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
			"""
			'''
			pygame.draw.line(pantalla, Util.ROJO, [int(j.rect.x+j.rect.width/2), int(j.rect.y+j.rect.height/2)], desplazamiento, 1)
			pygame.draw.circle(pantalla, Util.NEGRO, [int(j.rect.x+j.rect.width/2), int(j.rect.y+j.rect.height/2)], 100, 1)
			'''

			#cargando elementos del HUD
			bobs.draw(pantalla)
			minos.draw(pantalla)
			bosses.draw(pantalla)
			llaves.draw(pantalla)
			HUD.update(j.vida, j.tiempo_inmunidad, j.habitaciones)
			jugadores.draw(pantalla)
			NPCreapers.draw(pantalla)
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
						if (pos[0]>480 and pos[0]<900) and (pos[1]>400 and pos[1]<470):
							self.nivel_aprobado=True
						elif (pos[0]>600 and pos[0]<900) and (pos[1]>500 and pos[1]<570):
							pygame.quit()
							sys.exit()


			if self.nivel_aprobado:
				break

			self.pantalla.blit(fondo,[0,0])
			#self.pantalla.fill(Util.BLANCO)

			texto="Nivel completado"
			textoPuntaje=titulos.render(texto, 1, Util.AMARILLO)
			self.pantalla.blit(textoPuntaje,[480,200])

			texto="Siguiente nivel"
			textoPuntaje=titulos.render(texto, 1, Util.BLANCO)
			self.pantalla.blit(textoPuntaje,[500,400])

			texto="Salir"
			textoPuntaje=titulos.render(texto, 1, Util.BLANCO)
			self.pantalla.blit(textoPuntaje,[600,500])

			pygame.display.flip()
			reloj.tick(20)