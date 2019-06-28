import pygame
import math

class Botiquin(pygame.sprite.Sprite):
	def __init__(self, pos_ini, mat_i, tipo):
		pygame.sprite.Sprite.__init__(self)
		self.tipo_ayuda=tipo
		self.accion = 0
		self.animacion = 0
		self.matriz = mat_i
		self.image=pygame.transform.scale(self.matriz[self.tipo_ayuda][0],[32,24])
		self.rect = self.image.get_rect()
		self.rect.x = pos_ini[0]
		self.rect.y = pos_ini[1]