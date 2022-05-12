from src.constants import *
from src.player import Player

def main():

    print("Program Name: " ,__name__)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #Initialize the display
    pygame.display.set_caption("Arc Survival")
    clock = pygame.time.Clock() #Used to help track time
    font_name = pygame.font.match_font('arial')

    #Sprite Groups
    all_sprites = pygame.sprite.Group()

    #Sprite Objects
    player = Player()

    all_sprites.add(player)
    # Game Loop
    running = True
    while running:
        clock.tick(FPS) #Updates the clock Lock the framerate at 60 Frames Per Second

        #Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Update
        all_sprites.update()

        screen.fill(RED)
        all_sprites.draw(screen)

         #Update the full display Surface to the screen after drawing everything
        pygame.display.flip()
    
    pygame.quit()
#If this module is executing the script 
#the global variable __name__ gets set to __main__
if __name__ == "__main__":
    main()
