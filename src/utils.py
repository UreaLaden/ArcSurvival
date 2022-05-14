from sys import exit
from src.gamemanager import *
from src.mob import *
from src.player import *

def ConfigureSprites(game:GameManager):
    """Creates our Sprite Group, adds
    the relevant Sprite Objects to the Group
    rent returns all of the sprite groups
    (sprite_group,mob_group,player,bullet_group)
    """
    #Sprite Objects
    game.all_sprites = pygame.sprite.Group()
    game.mob_group = pygame.sprite.Group()
    game.bullet_group = pygame.sprite.Group()
    game.player = Player(game)
    
    for _ in range(game.mob_size):
        SpawnMob(game)

    game.all_sprites.add(game.bullet_group)
    game.all_sprites.add(game.player)

def ProcessEvents(game:GameManager):
    """Handles events and user input
    Returns false when user quits"""

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_ESCAPE]:
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False

def RenderGraphics(game:GameManager):
        """Update the full display Surface to the screen after drawing everything"""

        ScrollBackground(game)

        game.all_sprites.draw(game.screen)

        game.DrawUIText(18,SCREEN_WIDTH / 2, 10)
        game.DrawHealthBar(5,5,game.player.shield)
        game.DrawLives(SCREEN_WIDTH - 100,5,game.player.lives)

        pygame.display.flip()

def ScrollBackground(game:GameManager):
    """Scroll the Background image vertically"""
    #This explicit declaration is required to remind us that we are actually modifying
    #the value of the variable in the outer scope
    x1 = game.x1
    x2 = game.x2
    y1 = game.y1
    y2 = game.y2
    background_surface = game.background[0]
    rect = game.background[1]
    
    game.screen.blit(background_surface,rect)

    game.y2 += 10
    game.y1 += 10
    
    game.screen.blit(background_surface,(x1,y1))
    game.screen.blit(background_surface,(x2,y2))
    
    if y1 > SCREEN_HEIGHT:
        game.y1 = -SCREEN_HEIGHT
    if y2 > SCREEN_HEIGHT:
        game.y2 = -SCREEN_HEIGHT

