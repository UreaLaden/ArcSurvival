import pygame

#Interesting note. If we import from a module thats importing from us we'll run into issues
sprite_group:pygame.sprite.Group = pygame.sprite.Group()
mob_group:pygame.sprite.Group = pygame.sprite.Group()
bullet_group:pygame.sprite.Group = pygame.sprite.Group()
