import pygame


class Black_flash(pygame.sprite.Sprite):
    def __init__(self, images, groups):
        super().__init__(groups) 
        self.images = images
        self.frame_image = 0
        self.windows_width = 1280
        self.windows_height = 720
        self.image = self.images[self.frame_image]
        self.rect = self.image.get_rect(center = (self.windows_width / 2, self.windows_height / 2))
        self.spawned_at_time = pygame.time.get_ticks()
        

    def update(self, delta_t, window_w, window_h):

        self.seconds_from_last_frame = int ((pygame.time.get_ticks() - self.spawned_at_time) / 50 % 6)
        if self.seconds_from_last_frame == 5:
            self.kill()
        self.image = self.images[self.seconds_from_last_frame]