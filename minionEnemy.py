import pygame
import os

'''
versione modificata di https://xzany.itch.io/flying-demon-2d-pixel-art
'''

class Minion(pygame.sprite.Sprite):
    def __init__(self, images, groups, spawn_x, spawn_y):
        super().__init__(groups) 
        self.images = images
        self.frame_image = 0
        self.image = self.images[self.frame_image]
        self.rect = self.image.get_frect(center = (spawn_x, spawn_y))
        self.direction = pygame.Vector2(0, 0)
        self.speed = 200 
        self.spawned_at_time = pygame.time.get_ticks()
        self.life_time = 7000
        self.health = 5
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, delta_t, window_w, window_h):

        '''animation'''
        self.seconds_from_last_frame = int (pygame.time.get_ticks() / 120 % 4)
        self.image = self.images[self.seconds_from_last_frame]
        
        '''2 second kill'''
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.spawned_at_time >= self.life_time:
            self.kill()

        '''si muove destra e sinistra'''
        if self.rect.centerx <= (window_w / 2) :
            self.direction.x = 1
    
        elif self.rect.centerx >= window_w :
            self.direction.x = -1

        self.rect.center += self.direction * self.speed * delta_t
        

    def hit(self):
        self.health -= 1
        if self.health == 0:
            self.kill()
        if self.health == 1:
            self.image = pygame.transform.grayscale(self.image)
    

    def get_minion_health(self):
        return self.health
    
