#VIDEO ARRIVATO A 3:31:00

'''
====================================================================================
sprite piskel nuvola 32px
esportato in 128px (4x)
====================================================================================
'''

'''
| ======================== : TO DO LIST ANTIKITTY : ======================== |

-   cuore che indica energia
-   rifai sprite pixel perfect
-   aggiungi suono
-   aggiungi animazioni sprite
-   nemici che sparano
-   nemici che sparano con colpi che inseguono

| ========================================================================== |
'''
import pygame
import os
import random
import math
import playerKitty
import minionEnemy
from background import draw_parallaxxx
import time

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
minion_image = pygame.image.load(os.path.join("data", "minion", "minion0.png")).convert_alpha()
bullet_heart_image = pygame.image.load(os.path.join("data", "ammo", "ammonition0.png")).convert_alpha()
kitty_image = pygame.image.load(os.path.join("data", "kitty", "kittyx40.png")).convert_alpha() #1100/4=27.5
parallax_sprites = [] #carico in una lista gli sprite del mio parallasse
for i in range(0, 6):
    parallax_sprite = pygame.image.load(os.path.join("data", "background", f"viola1{i}.png")).convert_alpha()
    parallax_sprites.append(parallax_sprite)
font_pixel = pygame.font.Font(os.path.join("data", "fonts", "04B_30__.ttf"), 30)





antiKitty_txt = font_pixel.render('AntiKitty', False, (255, 255, 255)) #testo da scrivere, anti aliasing, colore
    
'''blit di sfondo'''

speed_scroll_parallax = [0, 0, 0, 0, 0, 0]
scroll_speeds = [1, 2, 3, 4, 5, 6]

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
    speed_scroll_parallax[5] -= scroll_speeds[5]
    if abs(speed_scroll_parallax[5]) >= parallax_width:
        speed_scroll_parallax[5] = 0
    for w in range(0, tiles):
            window_surface.blit(parallax_sprites[5], ((w * parallax_width) + speed_scroll_parallax[5], 0))


'''disegno nel group my sprites'''
my_sprites = pygame.sprite.Group()
my_bullets = pygame.sprite.Group()
kitty = playerKitty.Kitty(kitty_image, my_sprites, (window_width / 2), (window_height / 2), bullet_heart_image, my_bullets) #per argomenti vedi definizione Kitty in playerKitty


my_minions = pygame.sprite.Group()
minion_spawn_event = pygame.event.custom_type()
pygame.time.set_timer(minion_spawn_event, 3000)

def collisions():
    if pygame.sprite.spritecollide(kitty, my_minions, True, pygame.sprite.collide_mask):
        print("Kitty hit")
        quit()
            
    for minion in pygame.sprite.Group.sprites(my_minions):
        if (pygame.sprite.spritecollide(minion, my_bullets, True)):
            minion.hit()

    
def show_minion_health():
    for minion in pygame.sprite.Group.sprites(my_minions):
        minion_health = font_pixel.render(f"{minion.get_minion_health()}", False, (255, 255, 255))
        window_surface.blit(minion_health, (minion.rect.centerx - 27, minion.rect.centery - 50))

def show_general_text():
    window_surface.blit(antiKitty_txt, (window_width/2 - 90, 10))
    number_of_bullets = len(my_bullets)
    bullet_num_txt = font_pixel.render(f"{number_of_bullets}", False, (255, 255, 255)) #testo da scrivere, anti aliasing, colore
    bullet_num_rect = bullet_num_txt.get_frect( midbottom = (window_width/2, 100))

    window_surface.blit(bullet_num_txt, bullet_num_rect) #testo da blittare, posizione
    pygame.draw.rect(window_surface, (255, 255, 255), bullet_num_rect.inflate(20, 30).move(-2, 0), 5, 10)

def take_screen_shot(window_surface):
    screen_shot_time = time.asctime(time.localtime(time.time()))
    screen_shot_time = screen_shot_time.replace(" ", "_")
    screen_shot_time = screen_shot_time.replace(":", "_")
    path_screen_shot = "screenshots/" + screen_shot_time + ".png"
    pygame.image.save(window_surface, path_screen_shot)

execute = True
#==================================================================================================


while execute:
    dt = clock.tick(60) / 1000 # DELTA TIME, 60 fps

    '''events'''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:     #chiude quando pigio (1)
                execute = False
        if event.type == minion_spawn_event:
             minionEnemy.Minion(minion_image, (my_sprites, my_minions), (window_width + 20), int(random.randint(0, window_height)))
    
    '''screen'''
    draw_parallax()
    my_sprites.update(dt, window_width, window_height)
    collisions()
    my_sprites.draw(window_surface)
    draw_parallax_front_layer()

    show_minion_health()
    show_general_text()
    pygame.display.update()

pygame.QUIT