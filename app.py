from src.gamemanager import *
from src.utils import *
from src.explosions import *
from src.collisions import *

def main():
    game = GameManager()
    SetExplosions()

    # Game Loop
    while game.running:
        if game.game_over:
            game.reset()
            ShowTitleScreen(game)
            ConfigureSprites(game)

        #Updates the clock 60 Frames Per Second
        game.clock.tick(Config.FPS.value)         
        game.all_sprites.update()

        RenderGraphics(game)
        ProcessCollisions(game)
        ProcessEvents(game)

        game.all_sprites.draw(game.screen)
        pygame.display.flip()

    pygame.quit()
#If this module is executing the script 
#the global variable __name__ gets set to __main__
if __name__ == "__main__":
    main()
