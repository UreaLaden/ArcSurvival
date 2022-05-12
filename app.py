from src.utils import *
from src.sprites import *

def main():
    """Start the game"""
    game = InitializeGameSpace()
    background = LoadBackground()

    configured_sprites = ConfigureSprites(MOB_SIZE)
    sprites = configured_sprites[0]
    # Game Loop
    while running == True:
        #Updates the clock 60 Frames Per Second
        game[1].tick(FPS)         

        sprites.update()
        ProcessEvents()

        ProcessCollisions(configured_sprites)

        RenderGraphics(game[0],background,sprites)
        sprites.draw(game[0])
        pygame.display.flip()
    pygame.quit()
#If this module is executing the script 
#the global variable __name__ gets set to __main__
if __name__ == "__main__":
    main()
