from src.utils import *
from src.mob import *

def ConfigureSprites(mob_size:int):
    """Creates our Sprite Group, adds
    the relevant Sprite Objects to the Group
    then returns that Group"""
     #Sprite Groups
    sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    #Sprite Objects
    player = Player()
    for m in range(mob_size):
        SpawnMob(sprites,mobs)

    sprites.add(player)
    return sprites

