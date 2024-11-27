import pygame
import random


class Dust(pygame.sprite.Sprite):
    def __init__(self, images, pos, groups):
        super().__init__(groups) 
        self.images = images
        self.frame_image = 0
        self.image = self.images[0]
        self.pos = pos
        self.rect = self.image.get_frect(bottomright = self.pos)
        
        self.spawned_at_time = pygame.time.get_ticks()
        

    def update(self, delta_t, window_w, window_h):
        
        self.seconds_from_last_frame = int ((pygame.time.get_ticks() - self.spawned_at_time) / 120 % 4)
        if self.seconds_from_last_frame == 3:
            self.kill()
        
        self.image = self.images[(self.seconds_from_last_frame +1)%2]
        self.rect.centerx -= (self.seconds_from_last_frame ) * 4
        self.rect.centery -= 1