import pygame
from os import path
import sys
from src.constants import *
from src.player import *
from src.collisions import *

def LoadBackground():
    """Returns a tuple contain the background Image and its Rect"""
    img_dir = path.join(IMG_DIR,'Background-4.jpg')
    image = pygame.image.load(img_dir).convert()
    rect = image.get_rect()
    
    return (image,rect)

def ProcessEvents():
    """Handles events and user input
    Returns false when user quits"""
    global running

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_ESCAPE]:
        sys.exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

def InitializeGameSpace():
    """Game Window setup and config. 
       Good point to discuss Tuples
       (screen,clock,font_name)   
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #Initialize the display
    pygame.display.set_caption("Arc Survival") #Set the window Title
    clock = pygame.time.Clock() #Used to help track time
    font_name = GameFont('arial')
    return (screen,clock,font_name)

def GameFont(font: str):
    return pygame.font.match_font(font)

def RenderGraphics(screen : pygame.Surface,background:tuple[pygame.Surface,pygame.Rect],
sprites:pygame.sprite.Group):
        """Update the full display Surface to the screen after drawing everything"""

        ScrollBackground(screen,background[0],background[1])

        sprites.draw(screen)

        pygame.display.flip()

def ScrollBackground(screen:pygame.Surface,background:pygame.Surface,rect:pygame.Rect):
    """Scroll the Background image vertically"""
    #This explicit declaration is required to remind us that we are actually modifying
    #the value of the variable in the outer scope
    global x1
    global x2
    global y1
    global y2
    
    screen.blit(background,rect)

    y2 += 10
    y1 += 10
    
    screen.blit(background,(x1,y1))
    screen.blit(background,(x2,y2))
    
    if y1 > SCREEN_HEIGHT:
        y1 = -SCREEN_HEIGHT
    if y2 > SCREEN_HEIGHT:
        y2 = -SCREEN_HEIGHT
  