import pygame


class Death_enemy(pygame.sprite.Sprite):
    def __init__(self, pos, images, groups, type_enemy, font_pixel, window_surface):
        super().__init__(groups) 
        self.images = images
        self.frame_image = 0
        self.image = self.images[self.frame_image]
        self.pos = pos
        self.rect = self.image.get_frect(midleft = self.pos)
        self.spawned_at_time = pygame.time.get_ticks()
        self.type_enemy = type_enemy
        self.font_pixel = font_pixel
        self.window_surface = window_surface
        self.seconds_from_last_frame = 0
        
    def show_added_points(self,):
        if self.type_enemy == "red_minion":
            self.added_points_text = self.font_pixel.render("+20", False, (255 - self.seconds_from_last_frame * 30, 255 - self.seconds_from_last_frame * 30, 255 - self.seconds_from_last_frame * 30))
        elif self.type_enemy == "wizard":
            self.added_points_text = self.font_pixel.render("+40", False, (255 - self.seconds_from_last_frame * 30, 255 - self.seconds_from_last_frame * 30, 255 - self.seconds_from_last_frame * 30))
        self.window_surface.blit(self.added_points_text, (self.rect.centerx, self.rect.centery - 10 - self.seconds_from_last_frame * 5))

    def update(self, delta_t, window_w, window_h):
        self.show_added_points()
        '''animation'''
        self.seconds_from_last_frame = int ((pygame.time.get_ticks() - self.spawned_at_time) / 80 % 8)
        if self.seconds_from_last_frame == 7:
            self.kill()

        self.image = self.images[self.seconds_from_last_frame]