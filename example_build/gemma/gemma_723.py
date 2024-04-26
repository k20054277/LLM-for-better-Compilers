
import pygame
import sys

# Initialize the game engine
pygame.init()

# Define the game loop flag
running = True

# Set up the screen
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Define the clock
clock = pygame.time.Clock()

# Game loop
while running:
    # Clock tick
    clock.tick(60)

    # Event handling
    for event in pygame.event.get():
        # Quit if the user clicks the close button
        if event.type == pygame.QUIT:
            running = False

    # Render the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()
