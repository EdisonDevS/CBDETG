class Jugador(pygame.sprite.Sprite):
    def __init__(self, mat_i, pos_ini, lim):
        pygame.sprite.Sprite.__init__(self)
        self.accion=1
        self.concol=0
        self.m=mat_i
        self.lim=lim
        self.image=self.m[self.accion][self.concol]
        self.rect=self.image.get_rect()
        self.rect.x=pos_ini[0]
        self.rect.y=pos_ini[1]
        self.vely=0
        self.velx=0
        self.estado=0

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        self.image=self.m[self.accion][self.concol]

        if self.rect.y < 370:
            self.vely+=1
        else:
            self.vely=0

        if self.concol < lim[self.accion]:
            self.concol+=1
        else:
            if self.accion!=1:
                self.accion=1
            self.concol=0