from src.utils import *
from src.sprites import *

def main():
    """Start the game"""

    game = InitializeGameSpace()
    background = LoadBackground()
    score = "Hello Leaundrae, Let's Play a Game"
    running = True
    game_over = True
    # Game Loop
    while running == True:
        if game_over:
            game_over = False    
            configured_sprites = ConfigureSprites(MOB_SIZE)
            sprites = configured_sprites[0]

        #Updates the clock 60 Frames Per Second
        game[1].tick(FPS)         
        sprites.update()
        RenderGraphics(game[0],background,sprites,score,game[2],configured_sprites[2])
        ProcessCollisions(configured_sprites)
        ProcessEvents()
        sprites.draw(game[0])
        pygame.display.flip()
    pygame.quit()
#If this module is executing the script 
#the global variable __name__ gets set to __main__
if __name__ == "__main__":
    main()
