'''
#VIDEO ARRIVATO A 3:31:00 ma guarda animazioni corrette a 5:04:00
'''
'''
====================================================================================
sprite piskel nuvola 32px
esportato in 128px (4x)
====================================================================================
'''

'''
| ======================== : TO DO LIST ANTIKITTY : ======================== |

-   aggiungi la scritta +10, +20, +30 alla morte del minion, senza questa non si capisce di aver guadagnato dei punti 
-   ----------------------------------------------------------------------------CREA GRUPPO PER PROIETTILI DEI MINION
-   ----------------------------------------------------------------------------aggiungi array di stati per gli sprite del minion
-   ----------------------------------------------------------------------------aggiungi scintille quando il player spara
-   ----------------------------------------------------------------------------aggiungi nuvolette dietro il player
-   cuore che indica energia +++ modifica bullet systema
-   ----------------------------------------------------------------------------rifai sprite pixel perfect
-   aggiungi suono
-   ----------------------------------------------------------------------------nemici che sparano
-   nemici che sparano con colpi che inseguono
-   guarda a cosa mi servivano le mask
-   rispetto al punteggi permetti spawn di nemici più forti, ex 0-100 minon | 100-200 minion, minion wizard | 200-300 minion, minion wizard, minion tank
-   -----------------------------------------------------------------------------URGENTE  bloccare il player ai bordi dello schermo
-   -----------------------------------------------------------------------------aggiungi animazioni sprite 

| ========================================================================== |
'''
import pygame
import os
import random
import math
import player_kitty
import minion_enemy
import dust
import time
import points_system

os.environ['SDL_VIDEO_CENTERD'] = '1'


pygame.init()
info = pygame.display.Info()
window_width = 1280
window_height = 720
window_surface = pygame.display.set_mode((window_width, window_height)) #aggiungi questo alla fine:      ,pygame.NOFRAME
pygame.display.set_caption("AntiKitty")

clock = pygame.time.Clock()
#===========================================
'''imports'''

red_minion_sprites = [] #1100/4=27.5
for i in range(0, 4):
    minion_sprite = pygame.image.load(os.path.join("data", "minion_red", "flying", f"flying{i}.png")).convert_alpha()
    minion_sprite = pygame.transform.scale(minion_sprite, (112, 96))
    red_minion_sprites.append(minion_sprite)

for i in range(0, 4):
    minion_sprite = pygame.image.load(os.path.join("data", "minion_red", "attack", f"attack{i}.png")).convert_alpha()
    minion_sprite = pygame.transform.scale(minion_sprite, (112, 96))
    red_minion_sprites.append(minion_sprite)

red_minion_death_sprites = []
for i in range(0, 5):
    red_minion_death_sprite = pygame.image.load(os.path.join("data", "minion_red_death", f"death{i}.png")).convert_alpha()
    red_minion_death_sprite = pygame.transform.scale(red_minion_death_sprite, (112, 96))
    red_minion_death_sprites.append(red_minion_death_sprite)

fireball_sprites = []
for i in range(0, 3):
    fireball_sprite = pygame.transform.scale(pygame.image.load(os.path.join("data", "fireball", f"fireball{i}.png")).convert_alpha(), (20, 20))
    fireball_sprites.append(fireball_sprite)

bullet_heart_image = pygame.transform.scale(pygame.image.load(os.path.join("data", "bullet", "bullet0.png")).convert_alpha(), (20, 20))

fire_sprites = []
for i in range(0, 3):
    fire_sprite = pygame.transform.scale(pygame.image.load(os.path.join("data", "fire", f"fire{i}.png")).convert_alpha(), (60, 96))
    fire_sprites.append(fire_sprite)

dust_sprites = []
for i in range(0, 4):
    dust_sprite = pygame.transform.scale(pygame.image.load(os.path.join("data", "dust", f"dust{i}.png")).convert_alpha(), (32, 32))
    dust_sprites.append(dust_sprite)

kitty_sprites = [] #1100/4=27.5
for i in range(0, 4):
    kitty_sprite = pygame.image.load(os.path.join("data", "kitty", "no_contour", f"kittyx{i}.png")).convert_alpha()
    kitty_sprite = pygame.transform.scale(kitty_sprite, (112, 96))
    kitty_sprites.append(kitty_sprite)

parallax_layer_number = 5
parallax_sprites = [] #carico in una lista gli sprite del mio parallasse
#---------nuvola
#for i in range(0, parallax_layer_number):
#    parallax_sprite = pygame.transform.scale(pygame.image.load(os.path.join("data", "background", "nuvola", f"nuvola1{i}.png")).convert_alpha(), (window_width, window_height))
#    parallax_sprites.append(parallax_sprite)
#---------demon_woods
#for i in range(0, parallax_layer_number):
#    parallax_sprite = pygame.transform.scale(pygame.image.load(os.path.join("data", "background", "demon_woods", f"demon_woods1{i}.png")).convert_alpha(), (window_width, window_height))
#    parallax_sprites.append(parallax_sprite)
#---------industrial
#for i in range(0, parallax_layer_number):
#    parallax_sprite = pygame.transform.scale(pygame.image.load(os.path.join("data", "background", "industrial", f"industrial1{i}.png")).convert_alpha(), (window_width, window_height))
#    parallax_sprites.append(parallax_sprite)
#---------night_forest
for i in range(0, parallax_layer_number):
    parallax_sprite = pygame.transform.scale(pygame.image.load(os.path.join("data", "background", "night_forest", f"night_forest1{i}.png")).convert_alpha(), (window_width, window_height))
    parallax_sprites.append(parallax_sprite)

font_pixel = pygame.font.Font(os.path.join("data", "fonts", "04B_30__.ttf"), 30)

antiKitty_txt = font_pixel.render('AntiKitty', False, (255, 255, 255)) #testo da scrivere, anti aliasing, colore


'''blit di sfondo'''
speed_scroll_parallax = []
for i in range(0, parallax_layer_number):
    speed_scroll_parallax.append(0)

scroll_speeds = []
for i in range(0, parallax_layer_number):
    scroll_speeds.append(i + 2)

parallax_width = parallax_sprites[0].get_width() #calcolo il numero di sprite in "tiles" che mi servono per coprire l'animazione infinita
tiles = math.ceil(window_width / parallax_width) + 1 #+1 come buffer

def draw_parallax():
    for i in range(len(speed_scroll_parallax) - 1):
        speed_scroll_parallax[i] -= scroll_speeds[i]
        if abs(speed_scroll_parallax[i]) >= parallax_width:
            speed_scroll_parallax[i] = 0

    for i in range(len(parallax_sprites) - 1):
        for w in range(0, tiles):
            window_surface.blit(parallax_sprites[i], ((w * parallax_width) + speed_scroll_parallax[i], 0))

def draw_parallax_front_layer():
    speed_scroll_parallax[parallax_layer_number - 1] -= scroll_speeds[parallax_layer_number - 1]
    if abs(speed_scroll_parallax[parallax_layer_number - 1]) >= parallax_width:
        speed_scroll_parallax[parallax_layer_number - 1] = 0
    for w in range(0, tiles):
            window_surface.blit(parallax_sprites[parallax_layer_number - 1], ((w * parallax_width) + speed_scroll_parallax[parallax_layer_number - 1], 0))


'''disegno nel group my sprites'''
my_sprites = pygame.sprite.Group()
my_bullets = pygame.sprite.Group()
my_fireballs = pygame.sprite.Group()
dust_from_kitty_event = pygame.event.custom_type()
pygame.time.set_timer(dust_from_kitty_event, 180)
kitty = player_kitty.Kitty(kitty_sprites, my_sprites, (window_width / 2), (window_height / 2), bullet_heart_image, my_bullets, fire_sprites) #per argomenti vedi definizione Kitty in player_kitty



my_minions = pygame.sprite.Group()
minion_spawn_event = pygame.event.custom_type()
pygame.time.set_timer(minion_spawn_event, 3500)

'''game systems'''
points_tot = 0
points_from_time = 0
points_from_actions = 0

def collisions():
    if pygame.sprite.spritecollide(kitty, my_minions, True, pygame.sprite.collide_mask):
        print("Kitty minion hit")
        kitty.get_damage()
      
    for minion in pygame.sprite.Group.sprites(my_minions):
        if (pygame.sprite.spritecollide(minion, my_bullets, True)):
            minion.hit()
            if minion.health <= 0:
                kitty.add_ten_points()
        
        
    if pygame.sprite.spritecollide(kitty, my_fireballs, True, pygame.sprite.collide_mask):
        print("Kitty fireball hit")
        kitty.get_damage()
        


def show_points():
    points_text = font_pixel.render(f"{points_tot}", False, (255, 255, 255))
    window_surface.blit(points_text, (100, window_height - 100))

def show_minion_health():
    for minion in pygame.sprite.Group.sprites(my_minions):
        minion_health = font_pixel.render(f"{minion.get_minion_health()}", False, (255, 255, 255))
        window_surface.blit(minion_health, (minion.rect.centerx - 27, minion.rect.centery - 50))

def show_kitty_health():
    kitty_health = font_pixel.render(f"{kitty.get_kitty_health()}", False, (255, 255, 255))
    window_surface.blit(kitty_health, (kitty.rect.centerx - 27, kitty.rect.centery - 80))

def show_general_text():
    window_surface.blit(antiKitty_txt, (window_width/2 - 90, 10))
    number_of_bullets = len(my_bullets)
    bullet_num_txt = font_pixel.render(f"{number_of_bullets}", False, (255, 255, 255)) #testo da scrivere, anti aliasing, colore
    bullet_num_rect = bullet_num_txt.get_frect( midbottom = (window_width/2, 100))

    window_surface.blit(bullet_num_txt, bullet_num_rect) #testo da blittare, posizione
    pygame.draw.rect(window_surface, (255, 255, 255), bullet_num_rect.inflate(20, 30).move(-2, 0), 5, 10)

def render_text():
    show_kitty_health()
    show_general_text()
    show_minion_health()
    show_points()



execute = True
#==================================================================================================

pygame.mouse.set_visible(False)
while execute:
    dt = clock.tick(60) / 1000 # DELTA TIME, 60 fps
    time_from_start = pygame.time.get_ticks()
    '''events'''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:     #chiude quando pigio (1)
                execute = False
        if event.type == minion_spawn_event:
            minion_enemy.Minion(red_minion_sprites, (my_sprites, my_minions), (window_width + 20), int(random.randint(150, window_height - 200)), red_minion_death_sprites, my_sprites, fireball_sprites, my_fireballs)
        if event.type == dust_from_kitty_event:
            dust.Dust(dust_sprites, kitty.get_bottomleft(), my_sprites)
    '''screen'''
    draw_parallax()
    my_sprites.update(dt, window_width, window_height)
    collisions()
    my_sprites.draw(window_surface)
    draw_parallax_front_layer() 
    render_text()
    pygame.display.update()

    points_from_time = int(time_from_start / 100)
    points_from_actions = kitty.get_action_points()
    points_tot = points_from_time + points_from_actions

pygame.QUIT

#          ._____.  ___.  ___.  ___.  ___.           
#     _____ |__\_ |__\_ |__\_ |__\_ |__\_ |__   ____  
#    /     \|  || __ \| __ \| __ \| __ \| __ \ /    \ 
#   |  Y Y  \  || \_\ \ \_\ \ \_\ \ \_\ \ \_\ \   |  \
#   |__|_|  /__||___  /___  /___  /___  /___  /___|  /
#         \/        \/    \/    \/    \/    \/     \/ 
   
