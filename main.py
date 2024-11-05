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

os.environ['SDL_VIDEO_CENTERD'] = '1'

class Heart_Ammo(pygame.sprite.Sprite):
    def __init__(self, surf, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join("data", "ammo", "ammonition.png")).convert_alpha()

#class Cloud(pygame.sprite.Sprite):
#    def __init__(self, groups):
#        super().__init__(groups)
#        self.image = pygame.image.load(os.path.join("data", "clouds", "sprite_0.png")).convert_alpha()
#        self.rect = self.image.get_frect(center = ( random.randint(20, window_width - 20), random.randint(20, window_height - 20)))


pygame.init()
info = pygame.display.Info()
window_width = 1280
window_height = 720
window_surface = pygame.display.set_mode((window_width, window_height), pygame.NOFRAME)
pygame.display.set_caption("AntiKitty")

clock = pygame.time.Clock()
#===========================================
'''blit di sfondo'''

speed_scroll_parallax0 = 0
speed_scroll_parallax1 = 0
speed_scroll_parallax2 = 0
speed_scroll_parallax3 = 0
speed_scroll_parallax4 = 0
speed_scroll_parallax5 = 0

parallax_sprites = [] #carico in una lista gli sprite del mio parallasse
for i in range(0, 6):
    parallax_sprite = pygame.image.load(os.path.join("data", "background", f"viola1{i}.png")).convert_alpha()
    parallax_sprites.append(parallax_sprite)

parallax_width = parallax_sprites[0].get_width() #calcolo il numero di sprite in "tiles" che mi servono per coprire l'animazione infinita
tiles = math.ceil(window_width / parallax_width) + 1 #+1 come buffer

def draw_parallax0():
    for w in range(0, tiles):
            window_surface.blit(parallax_sprites[0], ((w * parallax_width) + speed_scroll_parallax0, 0))
def draw_parallax1():
    for w in range(0, tiles):
            window_surface.blit(parallax_sprites[1], ((w * parallax_width) + speed_scroll_parallax1, 0))
def draw_parallax2():
    for w in range(0, tiles):
            window_surface.blit(parallax_sprites[2], ((w * parallax_width) + speed_scroll_parallax2, 0))
def draw_parallax3():
    for w in range(0, tiles):
            window_surface.blit(parallax_sprites[3], ((w * parallax_width) + speed_scroll_parallax3, 0))
def draw_parallax4():
    for w in range(0, tiles):
            window_surface.blit(parallax_sprites[4], ((w * parallax_width) + speed_scroll_parallax4, 0))
def draw_parallax5():
    for w in range(0, tiles):
            window_surface.blit(parallax_sprites[5], ((w * parallax_width) + speed_scroll_parallax5, 0))

def draw_parallax_full():
     draw_parallax0()
     draw_parallax1()
     draw_parallax2()
     draw_parallax3()
     draw_parallax4()



'''disegno nel group my sprites'''

bullet_heart_image = pygame.image.load(os.path.join("data", "ammo", "ammonition0.png")).convert_alpha()

my_sprites = pygame.sprite.Group()
kitty = playerKitty.Kitty(my_sprites, (window_width / 2), (window_height / 2), bullet_heart_image) #per argomenti vedi definizione Kitty in playerKitty


execute = True


'''EVENTO SPAWN MINION'''
#GURADA CONTINUA QUESTE DUE RIGHE SOTTO DA VIDEO
minion_event = pygame.event.custom_type()
pygame.time.set_timer(minion_event, 3000)

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
    '''infinite parallax scroll!'''
    speed_scroll_parallax0 -= 1
    speed_scroll_parallax1 -= 2
    speed_scroll_parallax2 -= 3
    speed_scroll_parallax3 -= 4
    speed_scroll_parallax4 -= 5
    speed_scroll_parallax5 -= 6 #diminuisco peche uso il sistema cartesiano di pygame --> 0,0 angolo alto a sx
    if abs(speed_scroll_parallax0) >= parallax_width:
        speed_scroll_parallax0 = 0
    if abs(speed_scroll_parallax1) >= parallax_width:
        speed_scroll_parallax1 = 0
    if abs(speed_scroll_parallax2) >= parallax_width:
        speed_scroll_parallax2 = 0
    if abs(speed_scroll_parallax3) >= parallax_width:
        speed_scroll_parallax3 = 0
    if abs(speed_scroll_parallax4) >= parallax_width:
        speed_scroll_parallax4 = 0
    if abs(speed_scroll_parallax5) >= parallax_width:
        speed_scroll_parallax5 = 0
    
    
    draw_parallax_full()
    my_sprites.update(dt, window_width, window_height)
    my_sprites.draw(window_surface)
    draw_parallax5()

    pygame.display.update()

pygame.QUIT()