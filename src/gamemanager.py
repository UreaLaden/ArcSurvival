import pygame
from os import path
from src.soundeffects import *
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
        self.font         = pygame.font.match_font(Config.FONT.value)
        self.clock        = pygame.time.Clock() #Used to help track time
        #Sprite Groups
        self.all_sprites  = pygame.sprite.Group()
        self.mob_group    = pygame.sprite.Group()
        self.enemy_group  = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.power_group  = pygame.sprite.Group()
        self.explosions   = pygame.sprite.Group()
        self.x1           = 0
        self.x2           = 0
        self.y1           = 0
        self.y2           = -Config.SCREEN_HEIGHT.value
            
    def reset(self):
        self.game_over  = False    
        self.score      = 0

    def InitializeGameSpace(self):
        """Initialize Pygame"""
        pygame.init()
        LoadAudio()
        pygame.display.set_caption(Config.TITLE.value) #Set the window Title
        self.screen = pygame.display.set_mode((Config.SCREEN_WIDTH.value,Config.SCREEN_HEIGHT.value)) #Initialize the display


    def LoadBackground(self):
        """Returns a tuple contain the background Image and its Rect"""
        img_dir = path.join(Directories.IMG_DIR.value,'Background-4.jpg')
        
        background:dict[pygame.Surface,pygame.Rect] = {}
        background[Config.SURFACE.value] = pygame.image.load(img_dir).convert()
        background[Config.RECT.value] = pygame.image.load(img_dir).convert().get_rect()

        return background

    def DrawUIText(self,ui_text:str,size:int,x:int,y:int):
        """Renders UI onto the Screen
            screen,font_name,text,size,x,y
        """
        
        font = pygame.font.Font(self.font,size)
        text_surface = font.render(ui_text,True,Colors.WHITE.value)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface,text_rect)


    def DrawHealthBar(self,x,y,health):
        if health < 0:
            health = 0
        
        fill = (health / 100) * Config.BAR_LENGTH.value
        outline_rect = pygame.Rect(x,y,Config.BAR_LENGTH.value,Config.BAR_HEIGHT.value)
        fill_rect = pygame.Rect(x,y,fill,Config.BAR_HEIGHT.value)
        pygame.draw.rect(self.screen,Colors.GREEN.value,fill_rect)
        pygame.draw.rect(self.screen,Colors.WHITE.value,outline_rect,2)

    def DrawLives(self,x:int,y:int,lives:int):
        player_mini_img = pygame.image.load(Directories.PLAYER_IMG.value).convert()
        img = pygame.transform.scale(player_mini_img,(25,19))
        img.set_colorkey(Colors.BLACK.value)
        for i in range(lives):
            img_rect = img.get_rect()
            img_rect.x = x + 30 * i
            img_rect.y = y
            self.screen.blit(img,img_rect)

    