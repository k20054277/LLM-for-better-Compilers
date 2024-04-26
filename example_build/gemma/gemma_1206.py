
import pygame
import sys

# Initialize the game engine
pygame.init()

# Define the game loop flag
running = True

# Set up the clock
clock = pygame.time.Clock()

# Create the screen
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Define the character image
character = pygame.Surface((50, 50))
character.fill((255, 0, 0))

# Position the character
character_x, character_y = 100, 100

# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the clock
    clock.tick(60)

    # Render the screen
    screen.fill((0, 0, 0))
    screen.blit(character, (character_x, character_y))
    pygame.display.flip()

# Quit pygame
pygame.quit()
