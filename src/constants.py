from os import path

CURRENT_FILE_DIR = path.dirname(__file__)
ROOT_DIR = path.realpath(path.join(CURRENT_FILE_DIR,'..'))
IMG_DIR = path.join(ROOT_DIR,'assets\img')
PLAYER_IMG = path.join(IMG_DIR,'player_ship.png')

FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 480
PLAYER_HEIGHT = 80
PLAYER_WIDTH = 48
PLAYER_RADIUS = 20

MOB_SIZE = 8


