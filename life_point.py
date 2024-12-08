import pygame


class Life_point(pygame.sprite.Sprite):
    def __init__(self, pos, images, groups, i):
        super().__init__(groups) 
        self.images = images
        self.frame_image = 0
        self.image = self.images[self.frame_image]
        self.pos = pos
        self.rect = self.image.get_frect(midleft = self.pos)
        self.spawned_at_time = pygame.time.get_ticks()
        self.seconds_from_last_frame = 0

    def update(self, delta_t, window_w, window_h):
        self.seconds_from_last_frame = int (((pygame.time.get_ticks()) / 120) % 4)
        self.image = self.images[self.seconds_from_last_frame]
   