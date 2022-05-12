import sys
import pygame
from src.mob import *

def CheckCollision(first_group:pygame.sprite.Group,second_group:pygame.sprite.Group,dokill:bool = True,dokill2:bool = True) -> bool:
    return pygame.sprite.groupcollide(first_group,second_group,dokill,dokill2)

def ProcessCollisions(all_sprites:tuple[pygame.sprite.Group,...]) -> bool :
    """Accepts the Tuple containing all of the configured sprites. Process all 
    collisions and return False when the player is hit"""

    global running
    mob = all_sprites[1]
    player = all_sprites[2]
    bullet = all_sprites[3]

    player_hit = pygame.sprite.spritecollide(player,mob,True,pygame.sprite.collide_circle)
    mob_hit = pygame.sprite.groupcollide(mob,bullet,True,True)

    if mob_hit :
        print("Hit Meteor")
        SpawnMob()

    if player_hit:
        print("Player Hit")
        SpawnMob()


