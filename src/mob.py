from src.utils import *
import random

def GetMeteors() -> pygame.Surface:
    """Take all of our meteor images to a list for later"""
    meteor_dir = path.join(IMG_DIR,'Meteors')
    meteor_list = listdir(path.join(IMG_DIR,'Meteors'))
    meteors = []
    for img in meteor_list:
        meteors.append(pygame.image.load(path.join(meteor_dir,img)).convert())
    return meteors


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(GetMeteors())
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width *.85 / 2)
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        #pygame.draw.circle(self.image, RED, self.rect.center,self.radius)
        self.rect.y = random.randrange(-200,-40)
        self.speedy = random.randrange(1,9)
        self.speedx = random.randrange(-3,3)
        self.rot = 0 #Rotation
        self.rot_speed = random.randrange(-8,8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig,self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        #Good opportunity to discuss combined conditions
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 20:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speed = random.randrange(1,10)


def SpawnMob(sprite_group:pygame.sprite.Group,mob_group:pygame.sprite.Group):
    m = Mob()
    sprite_group.add(m)
    mob_group.add(m)
