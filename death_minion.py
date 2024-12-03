import pygame


class Death_minion(pygame.sprite.Sprite):
    def __init__(self, pos, images, groups):
        super().__init__(groups) 
        self.images = images
        self.frame_image = 0
        self.image = self.images[self.frame_image]
        self.pos = pos
        self.rect = self.image.get_frect(midleft = self.pos)
        self.spawned_at_time = pygame.time.get_ticks()
        

    def update(self, delta_t, window_w, window_h):

        '''animation'''
        self.seconds_from_last_frame = int ((pygame.time.get_ticks() - self.spawned_at_time) / 80 % 5)
        if self.seconds_from_last_frame == 4:
            self.kill()

        self.image = self.images[self.seconds_from_last_frame]