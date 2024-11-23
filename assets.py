import os
import pygame

window_width = 800  # Ensure this is defined or imported properly
window_height = 600  # Ensure this is defined or imported properly

minion_sprites = [] #1100/4=27.5
for i in range(0, 4):
    minion_sprite = pygame.image.load(os.path.join("data", "minion_red", "flying", f"flying{i}.png")).convert_alpha()
    minion_sprite = pygame.transform.scale(minion_sprite, (112, 96))
    minion_sprites.append(minion_sprite)

bullet_heart_image = pygame.transform.scale(pygame.image.load(os.path.join("data", "bullet", "bullet0.png")).convert_alpha(), (20, 20))

kitty_sprites = [] #1100/4=27.5
for i in range(0, 4):
    kitty_sprite = pygame.image.load(os.path.join("data", "kitty", f"kittyx{i}.png")).convert_alpha()
    kitty_sprite = pygame.transform.scale(kitty_sprite, (112, 96))
    kitty_sprites.append(kitty_sprite)

parallax_sprites = [] #carico in una lista gli sprite del mio parallasse
for i in range(0, 6):
    parallax_sprite = pygame.transform.scale(pygame.image.load(os.path.join("data", "background", f"viola1{i}.png")).convert_alpha(), (window_width, window_height))
    parallax_sprites.append(parallax_sprite)

font_pixel = pygame.font.Font(os.path.join("data", "fonts", "04B_30__.ttf"), 30)

antiKitty_txt = font_pixel.render('AntiKitty', False, (255, 255, 255))