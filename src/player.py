import pygame
from src.constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(PLAYER_IMG),(80,48))
        self.image.set_colorkey(BLACK) #Any pixels with the same color will be transparent
        self.rect = self.image.get_rect()
        self.radius = PLAYER_RADIUS
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -9.5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 9.5
        self.rect.x += self.speedx

        # Keep sprite on screen
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    