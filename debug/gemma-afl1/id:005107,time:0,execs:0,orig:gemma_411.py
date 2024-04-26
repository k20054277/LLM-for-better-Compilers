
import pygame
import sys

# Initialize Pygame
pygame.init()

# Create a 640x480 pixel screen
screen = pygame.display.set_mode((640, 480))

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Set the background color
screen.fill((0, 0, 0))

# Create a variable to track whether the game is running
running = True

# Game loop
while running:
    # Handle events
    for event in pygame.event.get():
        # Quit the game if the user clicks the close button
        if event.type == pygame.QUIT:
            running = False

    # Update the clock
    clock.tick(60)

    # Render the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
