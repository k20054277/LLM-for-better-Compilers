
import pygame
from pygame.locals import *

# Initialize the game engine
pygame.init()

# Set up the game screen
size = 500, 500
screen = pygame.display.set_mode(size)

# Define the colors we will use in RGB format
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Loop until the user clicks the close button
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Fill the screen with blue
    screen.fill(blue)

    # Draw a red rectangle
    pygame.draw.rect(screen, red, (100, 100, 200, 200))

    # Draw a green circle
    pygame.draw.circle(screen, green, (200, 200), 50)

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
