import pygame

class Fire_ball(pygame.sprite.Sprite):
    def __init__(self, images, groups, pos):
        super().__init__(groups) 
        self.images = images
        self.frame_image = 0
        self.image = self.images[self.frame_image]
        self.pos = pos
        self.rect = self.image.get_rect(midleft = self.pos)
        self.rect.x += 22
        self.rect.y += 14
        self.spawned_at_time = pygame.time.get_ticks()
        self.type = "fireball"
        
    def hit(self):
        self.kill()

    def update(self, delta_t, window_w, window_h):
        
        self.seconds_from_last_frame = int (pygame.time.get_ticks() / 120 % 3)
        self.image = self.images[self.seconds_from_last_frame]
        if self.seconds_from_last_frame == 2:
            self.rect.centery += 3
        if self.seconds_from_last_frame == 1:
            self.rect.centery -= 2
        if self.seconds_from_last_frame == 0:
            self.rect.centery -= 1
        self.rect.centerx -= 5
        self.current_time = pygame.time.get_ticks()
        if self.rect.right <= 0:
            self.kill()