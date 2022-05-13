import sys
from tkinter import scrolledtext
import pygame
from src.explosions import Explosion
from src.mob import *

def CheckCollision(first_group:pygame.sprite.Group,second_group:pygame.sprite.Group,dokill:bool = True,dokill2:bool = True) -> bool:
    return pygame.sprite.groupcollide(first_group,second_group,dokill,dokill2)

def ProcessCollisions(all_sprites:tuple[pygame.sprite.Group,...]) -> bool :
    """Accepts the Tuple containing all of the configured sprites. Process all 
    collisions and return False when the player is hit"""

    global running
    global sprite_group
    mob = all_sprites[1]
    player = all_sprites[2]
    bullet = all_sprites[3]

    player_hit = pygame.sprite.spritecollide(player,mob,True,pygame.sprite.collide_circle)
    mob_hits = pygame.sprite.groupcollide(mob,bullet,True,True)

    HandlePlayerCollisions(player,player_hit)
    HandleMobCollisions(mob,mob_hits)


def HandlePlayerCollisions(player:pygame.sprite.Group,player_hit:list[pygame.sprite.Sprite]):
    """Handles collisions with the Player"""
    global running
    global sprite_group

    for hit in player_hit:
        player.shield -= hit.radius * 2
        expl = Explosion(hit.rect.center,'sm')
        sprite_group.add(expl)
        SpawnMob()
        if player.shield <= 0:
            death_explosion = Explosion(player.rect.center,'player')
            sprite_group.add(death_explosion)
            player.hide()
            player.shield = 100

def HandleMobCollisions(mob:pygame.sprite.Group,mob_hits:list[pygame.sprite.Sprite]):
    """Handles Meteor impacts"""
    global score
    for hit in mob_hits:
        score += 50 - hit.radius
        expl = Explosion(hit.rect.center,'lg')
        sprite_group.add(expl)
        SpawnMob()
