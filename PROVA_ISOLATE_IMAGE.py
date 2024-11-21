import pygame
import os

# Initialize pygame
pygame.init()

# Load the image
image = pygame.image.load(os.path.join("data", "kitty", "kittySheet.png"))

# Define the rectangle (left, top, width, height)
rect = pygame.Rect(100, 100, 300, 300)

# Create a subsurface
isolated_image = image.subsurface(rect)

# Create a window to display the image
window = pygame.display.set_mode((500, 500))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with a color
    window.fill((255, 255, 255))

    # Blit the isolated image onto the window
    window.blit(isolated_image, (50, 50))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()