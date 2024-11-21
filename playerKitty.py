import pygame
import os
import bullet_heart

#class Bullet_heart (pygame.sprite.Sprite):
#    def __init__(self, image, groups, pos):
#        super().__init__(groups)
#        self.image = image
#        self.rect = self.image.get_frect(midleft = pos)
#    
#    def update(self, delta_t, window_w, window_h):
#        self.rect.centerx += 1700 * delta_t
#        if self.rect.left > window_w:
#            self.kill()



class Kitty(pygame.sprite.Sprite):
    def __init__(self, images, groups, spawn_x, spawn_y, bullet_heart_image, my_bullets):
        super().__init__(groups) #eredito da pygame.sprite.Sprite
        '''usando gli array'''
        #self.images = images
        #self.frame_image = 0
        #self.image = images[self.frame_image]
        '''usando gli spritesheet'''
        self.images = images
        #self.rect = self.image.get_frect(center = (spawn_x, spawn_y))
            #le classi Sprite ereditano dal parent pygame.sprite.Sprite
            #al quale sostituisco i self.surf e self rect con la superficie 
            #e il rect del mio player(nell init infati inizializzo anche il super)
        self.bullet_heart_image = bullet_heart_image
        self.my_bullets = my_bullets
        self.direction = pygame.Vector2(0, 0)
        self.speed = 800 

        self.gruppo = groups

        #dash cool down
        self.can_dash = True
        self.dash_time = 0
        self.dash_cooldown = 5000

        #fire cool down
        self.can_fire = True
        self.fire_time = 0
        self.fire_cooldown = 150

        #mask
        #mask = pygame.mask.from_surface(self.image)
        #mask_surf = mask.to_surface()
        #mask_surf.set_colorkey((0, 0, 0))
        #self.image = mask_surf
        self.mask = pygame.mask.from_surface(self.image)
        
    
    def dash_timer(self):
        '''dash ready'''
        if not self.can_dash:
            current_time = pygame.time.get_ticks() #millisecondi passati dall'avvio del gioco
            if current_time - self.dash_time >= self.dash_cooldown:
                self.can_dash = True

    def fire_timer(self):
        #scandisce la velocita con cui il player può sparare
        if not self.can_fire:
            current_time = pygame.time.get_ticks()
            if current_time - self.fire_time >= self.fire_cooldown:
                self.can_fire = True


    def update(self, delta_t, window_w, window_h):
        
        

        seconds_from_last_frame = int (pygame.time.get_ticks() / 120 % 4)
        print(seconds_from_last_frame)

        self.image = self.images[seconds_from_last_frame]

        key = pygame.key.get_pressed()

        self.direction.x = int(key[pygame.K_d]) - int(key[pygame.K_a])
        self.direction.y = int(key[pygame.K_s]) - int(key[pygame.K_w])
            #kye[pygame.K_tasto] sono dei booleani quindi se li sommo in 
            #questo modo trasformati in int mi danno la direzione corrette,
            #inoltre quando i tasti non sono premuti assumono False che è 0
            #percio il player se ne ritorna con la direction x e/o y a 0
        
        if self.direction:        #un vector restituisce true quando è diverso da 0
            self.direction = self.direction.normalize()
            #se la player_direction è diversa da 0 la normalizzo, ovvero
            #anche quando mi muovo diagonalmente ho la stessa velocità normalizzata
        else:
            self.direction = self.direction
        self.rect.center += self.direction * self.speed * delta_t
    
        '''fire'''

        if pygame.key.get_pressed()[pygame.K_k] and self.can_fire and len(self.my_bullets) < 17:
            bullet_heart.Bullet_heart(self.bullet_heart_image, (self.gruppo, self.my_bullets), self.rect.midright)
            self.can_fire = False
            self.fire_time = pygame.time.get_ticks()

        '''dash'''
        if pygame.key.get_pressed()[pygame.K_e] and self.can_dash:
            self.can_dash = False
            self.dash_time = pygame.time.get_ticks()
        
        self.dash_timer()
        self.fire_timer()