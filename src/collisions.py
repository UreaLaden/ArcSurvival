from src.gamemanager import *
from src.explosions import *
from src.mob import *

def CheckCollision(first_group:pygame.sprite.Group,second_group:pygame.sprite.Group,dokill:bool = True,dokill2:bool = True) -> bool:
    return pygame.sprite.groupcollide(first_group,second_group,dokill,dokill2)

def ProcessCollisions(game:GameManager) -> bool :
    """Accepts the Tuple containing all of the configured sprites. Process all 
    collisions and return False when the player is hit"""

    mob = game.mob_group
    player = game.player
    bullet = game.bullet_group

    player_hit = pygame.sprite.spritecollide(player,mob,True,pygame.sprite.collide_circle)
    mob_hits = pygame.sprite.groupcollide(mob,bullet,True,True)

    HandlePlayerCollisions(game,player_hit)
    HandleMobCollisions(game,mob_hits)


def HandlePlayerCollisions(game:GameManager,player_hit:list[pygame.sprite.Sprite],):
    """Handles collisions with the Player"""

    for hit in player_hit:
        game.player.shield -= hit.radius * 2
        expl = Explosion(hit.rect.center,'sm')
        game.all_sprites.add(expl)
        SpawnMob(game)
        if game.player.shield <= 0:
            death_explosion = Explosion(game.player.rect.center,'player')
            game.all_sprites.add(death_explosion)
            game.player.hide()
            game.player.shield = 100

    if game.player.lives == 0 and not death_explosion.alive():
        game.game_over = True
        
    

def HandleMobCollisions(game:GameManager,mob_hits:list[pygame.sprite.Sprite]) -> int:
    """Handles Meteor impacts"""
    for hit in mob_hits:
        game.score += 50 - hit.radius
        expl = Explosion(hit.rect.center,'lg')
        game.all_sprites.add(expl)
        SpawnMob(game)
