import pygame
from Util import *

class Bloque(pygame.sprite.Sprite):
	"""docstring for Bloque"""
	def __init__(self, imagen, punto, tangible):
		pygame.sprite.Sprite.__init__(self)
		self.image = imagen
		self.rect = self.image.get_rect()
		self.rect.x = punto[0]
		self.rect.y = punto[1]

		self.tangible = tangible