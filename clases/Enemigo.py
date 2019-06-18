class Enemigo(pygame.sprite.Sprite):
    def __init__(self, pos, mat_i, lim):
        pygame.sprite.Sprite.__init__(self)
        #control imagen
        self.accion = 0
        self.animacion = 0
        self.matiz = mat_i
        self.limite = lim
        self.image = self.m[self.animacion][self.accion]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        #stats
        self.velx = 0
        self.vely = 0
        self.vida = 100
        self.cadencia = 30
        self.element = 0
        self.escudo = 0