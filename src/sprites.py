import pygame
from src.utils import *
from src.mob import *


def ConfigureSprites(mob_size:int) -> tuple[pygame.sprite.Group,...] :
    """Creates our Sprite Group, adds
    the relevant Sprite Objects to the Group
    rent returns all of the sprite groups
    (sprites,mobs)
    """
    #Sprite Groups
    global sprite_group
    global mob_group
    global bullet_group

    #Sprite Objects
    player = Player()
    for m in range(mob_size):
        SpawnMob()

    sprite_group.add(player)
    return (sprite_group,mob_group,player,bullet_group)

