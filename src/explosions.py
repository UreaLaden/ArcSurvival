import pygame
from src.constants import *


explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []

class Explosion(pygame.sprite.Sprite):
    def __init__(self,center,size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 25

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

def SetExplosions():
    """Gather all of the explosion images into a dictionary for reference later"""
    global explosion_anim

    for i in range(24):
        filename = 'expl_01_{}.png'.format(i)
        img = pygame.image.load(path.join(IMG_DIR,'Explosions',filename)).convert()
        img.set_colorkey(BLACK)

        img_lg = pygame.transform.scale(img,(75,75))
        img_sm = pygame.transform.scale(img,(32,32))

        explosion_anim['lg'].append(img_lg)
        explosion_anim['sm'].append(img_sm)

        #player explosion images same 24
        filename = 'expl_10_00{}.png'.format(i)
        img = pygame.image.load(path.join(IMG_DIR,'Explosions',filename)).convert()
        img.set_colorkey(BLACK)
        explosion_anim['player'].append(img)
    '''
        for k in explosion_anim.keys():
            print(explosion_anim[k])
    '''
