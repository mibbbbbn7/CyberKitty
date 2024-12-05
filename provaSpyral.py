import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spiral Movement")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Sprite settings
sprite_radius = 10  # Radius of the sprite (for visualization as a circle)
sprite_color = WHITE

# Spiral settings
a = 4  # Initial radius offset
b = 4  # Controls the spacing between loops
angle = 0  # Initial angle
angle_speed = 0.1  # Speed of angle increase

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Calculate spiral position
    r = a + b * angle  # Spiral radius
    x = int(WIDTH / 2 + r * math.cos(angle))  # Convert to Cartesian X
    y = int(HEIGHT / 2 + r * math.sin(angle))  # Convert to Cartesian Y

    # Draw the sprite
    pygame.draw.circle(screen, sprite_color, (x, y), sprite_radius)

    # Update the angle to move the sprite
    angle += angle_speed

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
