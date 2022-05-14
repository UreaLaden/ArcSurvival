from src.gamemanager import *
from src.explosions import *
from src.mob import *
from src.enemy import *
from src.pickup import *

def CheckCollision(first_group:pygame.sprite.Group,second_group:pygame.sprite.Group,dokill:bool = True,dokill2:bool = True) -> bool:
    return pygame.sprite.groupcollide(first_group,second_group,dokill,dokill2)

def ProcessCollisions(game:GameManager) -> bool :
    """Process all collisions and return False when the player is hit"""

    mob = game.mob_group
    player = game.player
    bullet = game.bullet_group
    enemy = game.enemy_group
    pickup = game.power_group

    player_hit = pygame.sprite.spritecollide(player,mob,True,pygame.sprite.collide_circle)
    mob_hits = pygame.sprite.groupcollide(mob,bullet,True,True)
    enemy_hits = pygame.sprite.groupcollide(enemy,bullet,True,True)
    enemy_player_hits = pygame.sprite.spritecollide(player,enemy,True,pygame.sprite.collide_circle)
    pickup_hits = pygame.sprite.spritecollide(player,pickup,True,pygame.sprite.collide_circle)

    HandlePlayerCollisions(game,player_hit,enemy_player_hits)
    HandleMobCollisions(game,mob_hits)
    HandleEnemyCollisions(game,enemy_hits)
    HandlePickupCollisions(game,pickup_hits)


def HandlePlayerCollisions(game:GameManager,player_hit:list[pygame.sprite.Sprite],alien_hits:list[pygame.sprite.Sprite]):
    """When a player is hit"""

    for hit in player_hit:
        game.player.shield -= hit.radius * 2
        expl = Explosion(hit.rect.center,'sm')
        game.all_sprites.add(expl)
        SpawnMob(game)
        if game.player.shield <= 0:
            death_explosion = Explosion(game.player.rect.center,'player')
            game.all_sprites.add(death_explosion)
            game.player.die()

    for hit in alien_hits:
        game.player.shield -= hit.radius * 2
        expl = Explosion(hit.rect.center,'lg')
        game.all_sprites.add(expl)
        SpawnFireTeam(game)
        if game.player.shield <= 0:
            death_explosion = Explosion(game.player.rect.center,'player')
            game.all_sprites.add(death_explosion)
            game.player.die()

    if game.player.lives == 0 :
        game.game_over = True
        
def HandleEnemyCollisions(game:GameManager,enemy_hits:list[pygame.sprite.Sprite]):
    "When the enemy hits the player"
    for hit in enemy_hits:
        game.score += 100 - hit.radius
        expl = Explosion(hit.rect.center,'lg')
        game.all_sprites.add(expl)
        SpawnFireTeam(game)

def HandleMobCollisions(game:GameManager,mob_hits:list[pygame.sprite.Sprite]) -> int:
    """When a bullet hits a meteor"""
    for hit in mob_hits:
        game.score += 50 - hit.radius
        expl = Explosion(hit.rect.center,'lg')
        game.all_sprites.add(expl)
        if random.random() > 0.9:
            powerup = Pickup(hit.rect.center)
            game.all_sprites.add(powerup)
            game.power_group.add(powerup)
        SpawnMob(game)

def HandlePickupCollisions(game:GameManager,pickup_hits:list[pygame.sprite.Sprite]):
    for hit in pickup_hits:
        if hit.type == 'shield':
            game.player.shield += random.randrange(10,30)
            if game.player.shield >= 100:
                game.player.shield = 100
        if hit.type == 'gun':
            game.player.powerup()