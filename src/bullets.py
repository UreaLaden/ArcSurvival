import pygame
from src.constants import *
from src.groups import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMG_DIR,'laserRed16.png'))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

def SpawnBullet(x:int,y:int):
    global sprite_group
    global bullet_group

    bullet = Bullet(x,y)

    sprite_group.add(bullet)
    bullet_group.add(bullet)

