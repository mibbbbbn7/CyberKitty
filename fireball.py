import pygame
import random


class Fire_ball(pygame.sprite.Sprite):
    def __init__(self, images, pos, groups):
        super().__init__(groups) 
        self.images = images
        self.frame_image = 0
        self.image = self.images[self.frame_image]
        self.pos = pos
        self.rect = self.image.get_frect(midleft = self.pos)
        self.rect.x -= 20
        self.spawned_at_time = pygame.time.get_ticks()
        

    def update(self, delta_t, window_w, window_h):
        
        self.rect.centerx -= 5
        #self.current_time = pygame.time.get_ticks()
        #if self.current_time - self.spawned_at_time >= 40:
        #    self.kill()