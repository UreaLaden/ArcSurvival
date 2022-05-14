from src.gamemanager import *
import random
from os import listdir

def GetEnemies() -> pygame.Surface:
    """Take all of our alien images to a list for later"""
    enemy_dir = path.join(IMG_DIR,'Enemies')
    enemy_list = listdir(path.join(IMG_DIR,'Enemies'))
    enemies = []
    for img in enemy_list:
        enemies.append(pygame.image.load(path.join(enemy_dir,img)).convert())
    return enemies

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(random.choice(GetEnemies()),(100,60))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-200,-40)
        self.speedy = random.randrange(1,13)
        self.speedx = random.randrange(-3,3)
        self.last_update = pygame.time.get_ticks()

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if (
            (self.rect.top > SCREEN_HEIGHT + 10) or 
            (self.rect.left < -25) or 
            (self.rect.right > SCREEN_WIDTH + 20)
            ):
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speed = random.randrange(1,10)

def SpawnFireTeam(game:GameManager):
    """Instantiate a new Meteor Mob and add to Sprite group and Mob group"""
    e = Enemy()
    game.all_sprites.add(e)
    game.enemy_group.add(e)
