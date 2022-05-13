import pygame
from src.utils import *
from src.mob import *
from src.explosions import *


def ConfigureSprites(mob_size:int) -> tuple[pygame.sprite.Group,...] :
    """Creates our Sprite Group, adds
    the relevant Sprite Objects to the Group
    rent returns all of the sprite groups
    (sprite_group,mob_group,player,bullet_group)
    """
    #Sprite Groups
    global sprite_group
    global mob_group
    global bullet_group
    global score
    #Sprite Objects
    player = Player()
    for _ in range(mob_size):
        SpawnMob()

    SetExplosions()    
    sprite_group.add(player)
    score = 0
    return (sprite_group,mob_group,player,bullet_group)

