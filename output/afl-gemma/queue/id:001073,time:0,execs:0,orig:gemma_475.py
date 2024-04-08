
import pygame
import sys

# Initialize the pygame library
pygame.init()

# Create a 640x480 pixel screen
size = (640, 480)
screen = pygame.display.set_mode(size)

# Define the clock variable
clock = pygame.time.Clock()

# Loop until the user clicks the close button
running = True
while running:

    # Clock tick
    clock.tick(60)

    # Event queue
    for event in pygame.event.get():
        # Check if the event is a quit event
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
