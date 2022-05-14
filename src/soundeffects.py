import pygame
from src.constants import *
from enum import Enum

pygame.mixer.init()
shoot_sound = pygame.mixer.Sound(path.join(AUDIO_DIR,'Laser1.wav'))
shield_sound = pygame.mixer.Sound(path.join(AUDIO_DIR,'shieldPowerup.wav'))
powerup_sound = pygame.mixer.Sound(path.join(AUDIO_DIR,'gunPowerup.wav'))
explosion = pygame.mixer.Sound(path.join(AUDIO_DIR,'Explosion2.wav'))
player_die_sound = pygame.mixer.Sound(path.join(AUDIO_DIR,'playerExplosion.wav'))
shoot_sound.set_volume(0.5)

def LoadAudio():
    pygame.mixer.music.load(path.join(AUDIO_DIR,'Orbital Colossus.mp3'))
    # Include in pygame.__init__ to address module import error os.add_dll_directory(pygame_dir)
    #https://github.com/pygame/pygame/issues/2647
    pygame.mixer.music.play(loops = -1)