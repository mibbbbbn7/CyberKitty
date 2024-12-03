import pygame
import os
import death_minion
import fireball
import random

'''
versione modificata di https://xzany.itch.io/flying-demon-2d-pixel-art
'''

class Minion(pygame.sprite.Sprite):
    def __init__(self, images, groups, spawn_x, spawn_y, death_images, my_sprite_blit_group, fireball_images, my_fireball_group, window_w):
        super().__init__(groups) 
        self.images = images
        self.frame_image = 0
        self.image = self.images[self.frame_image]
        self.rect = self.image.get_frect(center = (spawn_x, spawn_y))
        self.direction = pygame.Vector2(-1, 0)
        self.speed = 200
        self.spawned_at_time = pygame.time.get_ticks()
        self.health = 5
        self.mask = pygame.mask.from_surface(self.image)
        self.my_sprite_blit_group = my_sprite_blit_group #qua mi serve solo per passarlo a death minion 
        self.death_images = death_images
        self.fireball_images = fireball_images
        self.can_count_time = True
        self.can_fire = True
        self.time_since_stopping = 0
        self.states = ["flying", "attack"]
        self.current_state = self.states[0]
        self.my_fireball_group = my_fireball_group
        self.stop_at = random.randint(int(window_w/2), int(window_w - 100))



    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()
            death_minion.Death_minion(self.rect.midleft, self.death_images, self.my_sprite_blit_group)
        self.image = self.images[self.seconds_from_last_frame + 8]
    
    def get_minion_health(self):
        return self.health
    
    def minion_move_and_shoot(self, delta_t, window_w, window_h):
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
            #if self.can_fire:
            #    self.can_fire = False
            #    self.time_of_last_fire = pygame.time.get_ticks()
            if self.image == self.images[5] and self.can_fire:
                fireball.Fire_ball(self.fireball_images,(self.my_sprite_blit_group, self.my_fireball_group), self.rect.midleft)
                self.can_fire = False
            if self.image == self.images[7]:
                self.can_fire = True
            #if pygame.time.get_ticks() - self.time_of_last_fire >= 2000:
            #    self.can_fire = True
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
        self.minion_move_and_shoot(delta_t, window_w, window_h)

