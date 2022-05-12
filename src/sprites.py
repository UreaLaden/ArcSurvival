import pygame
from src.player import Player

def ConfigureSprites():
    """Creates our Sprite Group, adds
    the relevant Sprite Objects to the Group
    then returns that Group"""
     #Sprite Groups
    sprites = pygame.sprite.Group()
    
    #Sprite Objects
    player = Player()
    
    sprites.add(player)
    return sprites
