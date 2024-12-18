import pygame

class Menu_button(pygame.sprite.Sprite):
    def __init__(self, pos, images, groups, kitty_sounds):
        super().__init__(groups) 
        self.images = images
        self.frame_image = 0
        self.image = self.images[self.frame_image]
        self.pos = pos
        self.rect = self.image.get_rect(center = self.pos)
        self.health = 5
        self.type = "menu_button"
        self.kitty_sounds = kitty_sounds


    def hit(self):
        self.kitty_sounds[0].play()
        self.health -= 1
        if self.health <= 0:
            self.kitty_sounds[1].play()
            self.kill()           
            
        self.image = self.images[1]
    
    def get_health(self):
        return self.health

    def update(self, delta_t, window_w, window_h):
        self.image = self.images[0]