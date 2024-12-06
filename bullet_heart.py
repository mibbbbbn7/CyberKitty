import pygame
import os
import random

'''
    if (
    len(pygame.sprite.Group.sprites(active_bullets))
    >= settings.MAX_ACTIVE_BULLET_COUNT
'''

class Bullet_heart (pygame.sprite.Sprite):
    def __init__(self, image, groups, pos):
        super().__init__(groups)
        self.image = image
        self.kitty_rifle = pos
        self.random_spawn_height = [pos[0], float(random.randint( int(pos[1] - 10), int(pos[1] + 10)))]
        self.rect = self.image.get_frect(midleft = self.random_spawn_height)
        self.creation_time = pygame.time.get_ticks()
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 1400

    def update(self, delta_t, window_w, window_h):
        self.rect.centerx += self.speed * delta_t
        '''aggiungi energia: cuore che si riempe quando numero di bullet e prossimo a 0 e si svuota quando e prossimo a un tetto massimo da decidere'''
        '''aggiungi un suono di cuore che si riempe'''
        '''il codice cosi va bene, quando hitto i minion il cuore si andrebbe a riempire'''
        if self.rect.left > window_w + 30:
            self.kill()
       
        self.rect = self.image.get_frect(center = self.rect.center)