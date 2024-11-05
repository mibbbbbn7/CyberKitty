import pygame
import os


class Bullet_heart (pygame.sprite.Sprite):
    def __init__(self, bullet_surface, pos, groups):
        super().__init__(groups)
        self.image = bullet_surface
        self.rect = self.image.get_frect(midleft = pos)

