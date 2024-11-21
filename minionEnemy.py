import pygame
import os


class Minion(pygame.sprite.Sprite):
    def __init__(self, image, groups, spawn_x, spawn_y):
        super().__init__(groups) 
        self.image = image
        self.rect = self.image.get_frect(center = (spawn_x, spawn_y))
        self.direction = pygame.Vector2(0, 0)
        self.speed = 200 
        self.spawned_at_time = pygame.time.get_ticks()
        self.life_time = 7000
        self.health = 5
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, delta_t, window_w, window_h):

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
    
