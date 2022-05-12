import pygame
from os import path
from src.constants import *
from src.player import *


def LoadBackground():
    """Returns a tuple contain the background Image and its Rect"""
    img_dir = path.join(IMG_DIR,'Background-4.jpg')
    image = pygame.image.load(img_dir).convert()
    rect = image.get_rect()
    return (image,rect)

def ProcessEvents():
    """Handles events and user input
    Returns false when user quits"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

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

def RenderGraphics(screen : pygame.Surface,background:tuple[pygame.Surface,pygame.Rect],sprites:pygame.sprite.Group):
        """Update the full display Surface to the screen after drawing everything"""
        screen.blit(background[0],background[1])
        sprites.draw(screen)

        pygame.display.flip()