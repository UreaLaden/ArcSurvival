from src.utils import *

def main():
    """Start the game"""
    game = InitializeGameSpace()

    background = LoadBackground()
    sprites = ConfigureSprites()

    # Game Loop
    running = True
    while running:
        running = ProcessEvents()
        
        #Updates the clock 60 Frames Per Second
        game[1].tick(FPS)         

        sprites.update()

        RenderGraphics(game[0],background,sprites)
    
    pygame.quit()
#If this module is executing the script 
#the global variable __name__ gets set to __main__
if __name__ == "__main__":
    main()
