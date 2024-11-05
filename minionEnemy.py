import pygame
import os


class Minion(pygame.sprite.Sprite):
    def __init__(self, groups, spawn_x, spawn_y):
        super().__init__(groups) 
        self.image = pygame.image.load(os.path.join("data", "minion", "minion0.png")).convert_alpha()
        self.rect = self.image.get_frect(center = (spawn_x, spawn_y))
        self.direction = pygame.Vector2(0, 0)
        self.speed = 200 
    

    def update(self, delta_t, window_w, window_h):

        
        if self.rect.centerx <= (window_w / 2) :
            self.direction.x = 1
        

        elif self.rect.centerx >= window_w :
            self.direction.x = -1

        self.rect.center += self.direction * self.speed * delta_t
