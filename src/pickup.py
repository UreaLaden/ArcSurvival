from os import listdir,path
import pygame
import random
from src.constants import IMG_DIR, SCREEN_HEIGHT

def GetPickups():
    pickups = {}
    pickup_dir = path.join(IMG_DIR,'Pickups')    

    gun_img = pygame.image.load(path.join(pickup_dir,'bolt_gold.png')).convert()
    shield_img = pygame.image.load(path.join(pickup_dir,'shield_gold.png')).convert()

    pickups['gun'] = gun_img
    pickups['shield'] = shield_img

    return pickups

def PickupTypes():
    pickups = ['shield','gun']
    return pickups

class Pickup(pygame.sprite.Sprite):
    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(PickupTypes())
        self.image = GetPickups()[self.type]
        self.image.set_colorkey()
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 5

    def update(self):
        self.rect.y += self.speedy
        #kill if it moves off the top of the screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
