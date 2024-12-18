import pygame

class Spell(pygame.sprite.Sprite):
    def __init__(self, images, groups, pos):
        super().__init__(groups) 
        self.type = "spell"
        self.images = images
        self.frame_image = 0
        self.image = self.images[self.frame_image]
        self.pos = pos
        self.rect = self.image.get_rect(midleft = self.pos)
        self.rect.x += 22
        self.rect.y += 14
        self.spawned_at_time = pygame.time.get_ticks()
        self.health = 2
        self.kitty_x = 0
        self.kitty_y = 0
        self.direction = pygame.Vector2(-1, 0)
        self.speed = 1
    
    def get_kitty_x(self, x):
        self.kitty_x = x

    def get_kitty_y(self, y):
        self.kitty_y = y
        
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()

    def move(self):
        self.direction.x = (self.kitty_x - self.rect.centerx)
        self.direction.y = (self.kitty_y - self.rect.centery)
        #if self.kitty_x < self.rect.centerx:
        #    self.direction.x = -1
        #elif self.kitty_x > self.rect.centerx:
        #    self.direction.x = 1
        #if self.kitty_y < self.rect.centery:
        #    self.direction.y = -1
        #elif self.kitty_y > self.rect.centery:
        #    self.direction.y = 1
        self.direction.normalize()

    def update(self, delta_t, window_w, window_h):
        self.seconds_from_last_frame = int (pygame.time.get_ticks() / 120 % 3)
        self.image = self.images[self.seconds_from_last_frame]
        self.move()
        #gestisco velocita, senza l if che setta speed a 2 il proiettile in prossimita del player va trooppo lento
        if (self.kitty_x - self.rect.centerx < 0 and self.kitty_x - self.rect.centerx > -200) or (self.kitty_x - self.rect.centerx > 0 and self.kitty_x - self.rect.centerx < 200):
            self.speed = 1.6
        else:
            self.speed = 1
        self.rect.center += self.direction * self.speed * delta_t
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.spawned_at_time > 3000:
            self.kill()