import pygame
from os import path
from src.constants import *
from src.gamemanager import *
from src.soundeffects import *

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

def SpawnBullet(game:GameManager,x:int,y:int):
    bullet = Bullet(x,y)
    game.all_sprites.add(bullet)
    game.bullet_group.add(bullet)
    shoot_sound.play()

