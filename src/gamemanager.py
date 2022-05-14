import pygame
from os import path
from src.constants import *

class GameManager():
    """Initialize the Game Space"""
    def __init__(self):
        self.InitializeGameSpace()
        self.background   = self.LoadBackground()
        self.game_over    = True    
        self.running      = True
        self.waiting      = True
        self.score        = 0
        self.mob_size     = 8
        self.fireteam     = 3
        self.font         = pygame.font.match_font('arial')
        self.clock        = pygame.time.Clock() #Used to help track time
        #Sprite Groups
        self.all_sprites  = pygame.sprite.Group()
        self.mob_group    = pygame.sprite.Group()
        self.enemy_group  = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.power_group  = pygame.sprite.Group()
        self.x1           = 0
        self.x2           = 0
        self.y1           = 0
        self.y2           = -SCREEN_HEIGHT
            
    def reset(self):
        self.game_over  = False    
        self.score      = 0

    def InitializeGameSpace(self):
        """Initialize Pygame"""
        pygame.init()
        pygame.display.set_caption("Arc Survival") #Set the window Title
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #Initialize the display


    def LoadBackground(self):
        """Returns a tuple contain the background Image and its Rect"""
        img_dir = path.join(IMG_DIR,'Background-4.jpg')
        
        background:dict[pygame.Surface,pygame.Rect] = {}
        background['surface'] = pygame.image.load(img_dir).convert()
        background['rect'] = pygame.image.load(img_dir).convert().get_rect()

        return background

    def DrawUIText(self,ui_text:str,size:int,x:int,y:int):
        """Renders UI onto the Screen
            screen,font_name,text,size,x,y
        """
        
        font = pygame.font.Font(self.font,size)
        text_surface = font.render(ui_text,True,WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface,text_rect)


    def DrawHealthBar(self,x,y,health):
        if health < 0:
            health = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 10
        fill = (health / 100) * BAR_LENGTH
        outline_rect = pygame.Rect(x,y,BAR_LENGTH,BAR_HEIGHT)
        fill_rect = pygame.Rect(x,y,fill,BAR_HEIGHT)
        pygame.draw.rect(self.screen,GREEN,fill_rect)
        pygame.draw.rect(self.screen,WHITE,outline_rect,2)

    def DrawLives(self,x:int,y:int,lives:int):
        player_mini_img = pygame.image.load(PLAYER_IMG).convert()
        img = pygame.transform.scale(player_mini_img,(25,19))
        img.set_colorkey(BLACK)
        for i in range(lives):
            img_rect = img.get_rect()
            img_rect.x = x + 30 * i
            img_rect.y = y
            self.screen.blit(img,img_rect)

    