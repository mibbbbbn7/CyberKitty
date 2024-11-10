import pygame
import os
import random
import math


'''''''''''ke skifooooooo   '''
#window_width = 1280
#
#parallax_sprites = [] #carico in una lista gli sprite del mio parallasse
#for i in range(0, 6):
#    parallax_sprite = pygame.image.load(os.path.join("data", "background", f"viola1{i}.png")).convert_alpha()
#    parallax_sprites.append(parallax_sprite)
#    
'''blit di sfondo'''
#
speed_scroll_parallax = [0, 0, 0, 0, 0, 0]
scroll_speeds = [1, 2, 3, 4, 5, 6]
#
#parallax_width = parallax_sprites[0].get_width() #calcolo il numero di sprite in "tiles" che mi servono per coprire l'animazione infinita
#tiles = math.ceil(window_width / parallax_width) + 1 #+1 come buffer

def draw_parallaxxx(window_surface, parallax_sprites, parallax_width, tiles):
    for i in range(len(speed_scroll_parallax)):
        speed_scroll_parallax[i] -= scroll_speeds[i]
        if abs(speed_scroll_parallax[i]) >= parallax_width:
            speed_scroll_parallax[i] = 0

    for i in range(len(parallax_sprites)):
        for w in range(0, tiles):
            window_surface.blit(parallax_sprites[i], ((w * parallax_width) + speed_scroll_parallax[i], 0))