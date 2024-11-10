import pygame
import os

'''
    if (
    len(pygame.sprite.Group.sprites(active_bullets))
    >= settings.MAX_ACTIVE_BULLET_COUNT
'''

class Bullet_heart (pygame.sprite.Sprite):
    def __init__(self, image, groups, pos):
        super().__init__(groups)
        self.original_image = image
        self.image = self.original_image
        self.rect = self.image.get_frect(midleft = pos)
        self.exist_duration_time = 6000
        self.creation_time = pygame.time.get_ticks()
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 900
        self.rotation = 0

    def update(self, delta_t, window_w, window_h):
        self.rect.centerx += self.speed * delta_t
        self.actual_time = pygame.time.get_ticks()
        if (self.actual_time - self.creation_time) >= self.exist_duration_time:
            self.kill()
            '''aggiungi energia: cuore che si riempe quando numero di bullet e prossimo a 0 e si svuota quando e prossimo a un tetto massimo da decidere'''
            '''aggiungi un suono di cuore che si riempe'''
            '''il codice cosi va bene, quando hitto i minion il cuore si andrebbe a riempire'''
        self.rotation += 500 * delta_t
        self.image = pygame.transform.rotate(self.original_image, self.rotation)
        self.rect = self.image.get_frect(center = self.rect.center)