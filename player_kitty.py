import pygame
import bullet_heart
import fire
import dash
import icon_button
import player_kitty_death
import player_kitty_hit
import life_point

class Kitty(pygame.sprite.Sprite):
    def __init__(self, images, groups, spawn_x, spawn_y, kitty_sounds, bullet_heart_image, my_bullets, fire_images, dash_images, my_dash_clouds, icons_images, player_kitty_death_images, player_kitty_hit_images, life_point_images):
        super().__init__(groups) #eredito da pygame.sprite.Sprite
 
        self.images = images
        self.frame_image = 0
        self.image = self.images[self.frame_image]
        self.rect = self.image.get_rect(center = (spawn_x, spawn_y))
            #le classi Sprite ereditano dal parent pygame.sprite.Sprite
            #al quale sostituisco i self.surf e self rect con la superficie 
            #e il rect del mio player(nell init infati inizializzo anche il super)
        self.direction = pygame.Vector2(0, 0)
        self.speed = 700 
        self.health = 6
        self.groups = groups
        self.kitty_sounds = kitty_sounds

        #shrink cool down
        self.can_shrink = True
        self.shrink_time = 0
        self.shrink_cooldown = 1500
        self.is_shrinking_call = False
        self.for_next_shrink_cooldown = 5000

        #fire cool down
        self.can_fire = True
        self.fire_time = 0
        self.fire_cooldown = 100

        #dash cool down
        self.can_dash = True
        self.dash_time = 0
        self.dash_cooldown = 2000


        self.bullet_heart_image = bullet_heart_image
        self.my_bullets = my_bullets
        self.fire_images = fire_images
        self.dash_images = dash_images
        self.my_dash_clouds = my_dash_clouds
        self.icons_images = icons_images
        self.player_kitty_hit_images = player_kitty_hit_images
        self.player_kitty_death_images = player_kitty_death_images
        self.life_point_images = life_point_images

        self.mask = pygame.mask.from_surface(self.image)
        self.action_points = 0

        #life
        self.life_points = []
        for i in range(0, self.health):
           self.life_points.append(life_point.Life_point((50 + i * 50, 720 - 50) ,self.life_point_images, self.groups, i))
        
        self.k_button = icon_button.Icon_button(self.icons_images, self.groups, (1280 - 96, 50), 0)
        self.space_button = icon_button.Icon_button(self.icons_images, self.groups, (1280 - 224, 50), 2)
        
    def kitty_dead(self):
        if self.health <= 0:
            return True
        return False
    
    def get_damage(self):
        self.kitty_sounds[0].play()  
        self.health -= 1
        self.life_points[self.health].kill()
        player_kitty_hit.Player_kitty_hit(self.player_kitty_hit_images, self.groups)
        if self.health <= 1:
            player_kitty_death.Player_kitty_death(self.player_kitty_death_images, self.groups)
        if self.health <= 0:
            self.kill()
            self.kitty_sounds[1].play()
    
    def get_kitty_health(self):
        return self.health
    
    def get_action_points(self):
        return self.action_points
    
    def get_x(self):
        return self.rect.centerx
    
    def get_y(self):
        return self.rect.centery
    
    def add_points(self, type):
        if type == "red_minion":
            self.action_points += 20
        if type == "wizard":
            self.action_points += 40
        if type == "menu_button":
            self.action_points += 1

    def shrink_timer(self):
        if not self.can_shrink:
            self.speed = 900
            current_time = pygame.time.get_ticks()
            if current_time - self.shrink_time >= self.shrink_cooldown:
                if self.is_shrinking_call : dash.Dash(self.dash_images, (self.groups, self.my_dash_clouds), self.rect.center)
                self.is_shrinking_call = False
                self.speed = 700
    
    def for_next_shrink_timer(self):
        if not self.can_shrink:
            current_time = pygame.time.get_ticks()
            if current_time - self.shrink_time >= self.for_next_shrink_cooldown:
                self.can_shrink = True

    def fire_timer(self):
        #scandisce la velocita con cui il player può sparare
        if not self.can_fire:
            current_time = pygame.time.get_ticks()
            if current_time - self.fire_time >= self.fire_cooldown:
                self.can_fire = True

    def dash_timer(self):
        #scandisce la velocita con cui il player può sparare
        if not self.can_dash:
            current_time = pygame.time.get_ticks()
            if current_time - self.dash_time >= self.dash_cooldown:
                self.can_dash = True

    def get_bottomleft(self):
        return self.rect.bottomleft
    
    def set_icon_buttons_state(self):
        if self.can_shrink:
            self.k_button.on()
        else:
            self.k_button.off()

        if self.can_dash:
            self.space_button.on()
        else:
            self.space_button.off()

    def update(self, delta_t, window_w, window_h):
        '''animation and definition of shrink or normal'''
        seconds_from_last_frame = int (pygame.time.get_ticks() / 120 % 4)
        if pygame.key.get_pressed()[pygame.K_p] and self.can_shrink and not self.is_shrinking_call:
            self.kitty_sounds[3].play()
            self.is_shrinking_call = True
            self.can_shrink = False
            self.shrink_time = pygame.time.get_ticks()
        if self.is_shrinking_call: #animazione quando è piccolo
            self.image = self.images[seconds_from_last_frame + 4]
            self.rect = self.image.get_rect(center = (self.rect.centerx, self.rect.centery))
            self.mask = pygame.mask.from_surface(self.image)
        if not self.is_shrinking_call: #animazione quando è grande
            self.image = self.images[seconds_from_last_frame]
            self.rect = self.image.get_rect(center = (self.rect.centerx, self.rect.centery))
            self.mask = pygame.mask.from_surface(self.image)

        '''dash'''
        if pygame.key.get_pressed()[pygame.K_SPACE] and self.can_dash and not self.is_shrinking_call:
            dash.Dash(self.dash_images, self.groups, self.rect.center)
            self.kitty_sounds[2].play()
            if pygame.key.get_pressed()[pygame.K_w]:
                self.rect.centery -= 150
            if pygame.key.get_pressed()[pygame.K_s]:
                self.rect.centery += 150
            if pygame.key.get_pressed()[pygame.K_a]:
                self.rect.centerx -= 200
            if pygame.key.get_pressed()[pygame.K_d]:
                self.rect.centerx += 200
            if not pygame.key.get_pressed()[pygame.K_w] and not pygame.key.get_pressed()[pygame.K_a] and not pygame.key.get_pressed()[pygame.K_s] and not pygame.key.get_pressed()[pygame.K_d] :
                self.rect.centerx += 200
            self.can_dash = False
            self.dash_time = pygame.time.get_ticks()
            dash.Dash(self.dash_images, (self.groups, self.my_dash_clouds), self.rect.center)
        '''movement'''
        key = pygame.key.get_pressed()
            #kye[pygame.K_tasto] sono dei booleani quindi se li sommo in 
            #questo modo trasformati in int mi danno la direzione corrette,
            #inoltre quando i tasti non sono premuti assumono False che è 0
            #percio il player se ne ritorna con la direction x e/o y a 0 :D
        self.direction.x = int(key[pygame.K_d]) - int(key[pygame.K_a])
        self.direction.y = int(key[pygame.K_s]) - int(key[pygame.K_w])

            #per limitare il movimento del player allinterno dello schermo
        if self.rect.right > window_w + 70:
            self.rect.right = window_w + 70
        if self.rect.left < -70:
            self.rect.left = -70
        if self.rect.bottom > 750:
            self.rect.bottom = 750
        if self.rect.top < -40:
            self.rect.top = -40
    
        
        if self.direction:        #un vector restituisce true quando è diverso da 0
            self.direction = self.direction.normalize()
            #se la player_direction è diversa da 0 la normalizzo, ovvero
            #anche quando mi muovo diagonalmente ho la stessa velocità normalizzata
        else:
            self.direction = self.direction
        self.rect.center += self.direction * self.speed * delta_t
    
        '''fire'''
        if pygame.key.get_pressed()[pygame.K_l] and self.can_fire and not self.is_shrinking_call:
            self.kitty_sounds[4].play()
            fire.Fire(self.fire_images, self.rect.midright, self.groups)
            bullet_heart.Bullet_heart(self.bullet_heart_image, (self.groups, self.my_bullets), self.rect.midright)
            self.can_fire = False
            self.fire_time = pygame.time.get_ticks()
        
        
        self.dash_timer()
        self.shrink_timer()
        self.for_next_shrink_timer()
        self.fire_timer()
        self.set_icon_buttons_state()