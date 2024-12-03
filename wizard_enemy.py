import pygame
import os
import death_enemy
import spell
import random

class Wizard(pygame.sprite.Sprite):
    def __init__(self, images, groups, spawn_x, spawn_y, death_images, my_sprite_blit_group, my_spells_group, spell_images, my_enemies_hittable, window_w):
        super().__init__(groups)
        self.type = "wizard"
        self.images = images
        self.frame_image = 0
        self.image = self.images[self.frame_image]
        self.rect = self.image.get_frect(center = (spawn_x, spawn_y))
        self.direction = pygame.Vector2(-1, 0)
        self.speed = 300
        self.spawned_at_time = pygame.time.get_ticks()
        self.health = 10
        self.mask = pygame.mask.from_surface(self.image)
        self.can_count_time = True
        self.can_fire = True
        self.time_since_stopping = 0
        self.states = ["flying", "attack"]
        self.current_state = self.states[0]
        self.stop_at = random.randint(int(window_w/2), int(window_w - 100))

        self.death_images = death_images
        self.my_sprite_blit_group = my_sprite_blit_group
        self.my_spells_group = my_spells_group
        self.spell_images = spell_images
        self.my_enemies_hittable = my_enemies_hittable

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()
            death_enemy.Death_minion(self.rect.midleft, self.death_images, self.my_sprite_blit_group)
        self.image = self.images[self.seconds_from_last_frame + 8]#"<------------------- piu quanto?"
    
    def get_wizard_health(self):
        return self.health
    
    def wizard_move_and_shoot(self, delta_t, window_w, window_h):
        '''MOVIMENTO AVANTI E INDIETRO MAGARI RIUTILIZZA'''
#        if self.rect.centerx <= (window_w / 2) :
#            self.direction.x = 1
#    
#        elif self.rect.centerx >= window_w :
#            self.direction.x = -1
        
        if self.rect.centerx <= self.stop_at:
            self.direction.x = 0
            self.current_state = self.states[1]
            if self.can_count_time:
                self.time_since_stopping = pygame.time.get_ticks()
                self.can_count_time = False

        if self.direction.x == 0:
            if self.image == self.images[5] and self.can_fire:
                spell.Spell(self.spell_images,(self.my_sprite_blit_group, self.my_spells_group, self.my_enemies_hittable), self.rect.midleft)
                self.can_fire = False
            if self.image == self.images[7]:
                self.can_fire = True
            if pygame.time.get_ticks() - self.time_since_stopping >= 4000:
                self.direction.x = 1.5
                self.current_state = self.states[0]
        
        self.rect.center += self.direction * self.speed * delta_t

    def update(self, delta_t, window_w, window_h):

        '''animation'''
        if self.current_state == self.states[0]:
            self.seconds_from_last_frame = int (pygame.time.get_ticks() / 120 % 4)
            self.image = self.images[self.seconds_from_last_frame]

        if self.current_state == self.states[1]:
            self.seconds_from_last_frame = int (pygame.time.get_ticks() / 180 % 7)
            self.image = self.images[self.seconds_from_last_frame + 1]
            if self.seconds_from_last_frame % 2 == 0:
                self.rect.y -= 0.8
            if self.seconds_from_last_frame % 2 == 1:
                self.rect.y += 1

        if self.direction.x == 1.5:
            self.image = pygame.transform.flip(self.image, True, False)
        
        self.current_time = pygame.time.get_ticks()
        
        '''auto kill'''
        if self.rect.centerx > window_w + 100 and self.direction.x == 1:
            self.kill()
        
        '''movement'''
        self.wizard_move_and_shoot(delta_t, window_w, window_h)