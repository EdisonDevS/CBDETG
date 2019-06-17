import pygame
class Jugador(pygame.sprite.Sprite):
    
	def __init__(self, pos, mat_i):
		pygame.sprite.Sprite.__init__(self)
		#control imagen
		self.accion = 0
		self.animacion = 0
		self.matriz = mat_i
		self.limite = [8,7,7,9,9,9,9,6,6,6,6,4,4,4,4,6,5,4,6,3,3]
		self.image = self.matriz[self.accion][self.animacion]
		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]

		#stats
		self.velx = 0
		self.vely = 0
		self.vida = 100
		self.cadencia = 30
		self.escudo = 0
		self.inmune = False

	def update(self):
		self.rect.x+=self.velx
		self.rect.y+=self.vely
		self.image=self.matriz[self.accion][self.animacion]

		if self.rect.y < 300:	
			self.vely+=1
		else:
			self.vely=0

		if self.accion < self.limite[self.animacion]-1:
			self.accion+=1
		else:
			if self.animacion!=13:
				self.animacion=13
			self.accion=0

	