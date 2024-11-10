#VIDEO ARRIVATO A 2:24:00

'''
====================================================================================
sprite piskel nuvola 32px
esportato in 128px (4x)
====================================================================================
'''
import pygame
import os
import random
import math
import playerKitty
import minionEnemy
from background import draw_parallaxxx

os.environ['SDL_VIDEO_CENTERD'] = '1'


pygame.init()
info = pygame.display.Info()
window_width = 1280
window_height = 720
window_surface = pygame.display.set_mode((window_width, window_height), pygame.NOFRAME)
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
    
'''blit di sfondo'''

speed_scroll_parallax = [0, 0, 0, 0, 0, 0]
scroll_speeds = [1, 2, 3, 4, 5, 6]

parallax_width = parallax_sprites[0].get_width() #calcolo il numero di sprite in "tiles" che mi servono per coprire l'animazione infinita
tiles = math.ceil(window_width / parallax_width) + 1 #+1 come buffer

def draw_parallaxxx():
    for i in range(len(speed_scroll_parallax)):
        speed_scroll_parallax[i] -= scroll_speeds[i]
        if abs(speed_scroll_parallax[i]) >= parallax_width:
            speed_scroll_parallax[i] = 0

    for i in range(len(parallax_sprites)):
        for w in range(0, tiles):
            window_surface.blit(parallax_sprites[i], ((w * parallax_width) + speed_scroll_parallax[i], 0))


'''disegno nel group my sprites'''
my_sprites = pygame.sprite.Group()
kitty = playerKitty.Kitty(kitty_image, my_sprites, (window_width / 2), (window_height / 2), bullet_heart_image) #per argomenti vedi definizione Kitty in playerKitty

'''EVENTO SPAWN MINION'''
minion_event = pygame.event.custom_type()
pygame.time.set_timer(minion_event, 3000)

execute = True

#==================================================================================================


while execute:
    dt = clock.tick(60) / 1000 # DELTA TIME, 60 fps

    '''EVENTS'''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:     #chiude quando pigio (1)
                execute = False
        if event.type == minion_event:
             print("spawn minion")
             minionEnemy.Minion(minion_image, my_sprites, int(random.randint(0, window_width)), int(random.randint(0, window_height)))
    
    draw_parallaxxx()
    my_sprites.update(dt, window_width, window_height)
    my_sprites.draw(window_surface)

    pygame.display.update()

pygame.QUIT()