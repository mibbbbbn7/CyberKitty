import pygame


class Dash(pygame.sprite.Sprite):
    def __init__(self, images, groups, pos):
        super().__init__(groups) 
        self.images = images
        self.frame_image = 0
        self.image = self.images[self.frame_image]
        self.pos = pos
        self.rect = self.image.get_rect(center = self.pos)
        self.spawned_at_time = pygame.time.get_ticks()
        self.mask = pygame.mask.from_surface(self.image)
        

    def update(self, delta_t, window_w, window_h):

        '''animation'''
        self.seconds_from_last_frame = int ((pygame.time.get_ticks() - self.spawned_at_time) / 40 % 8)
        if self.seconds_from_last_frame == 7:
            self.kill()

        self.image = self.images[self.seconds_from_last_frame]