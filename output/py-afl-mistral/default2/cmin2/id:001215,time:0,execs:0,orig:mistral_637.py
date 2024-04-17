
# Import required Pygame modules
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 500
HEIGHT = 400
FPS = 60

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame Example')

# Set up the clock
clock = pygame.time.Clock()

# Create a variable to store whether or not the mouse button is pressed
mouse_pressed = False

# Main game loop
running = True
while running:
    # Get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True

    # Handle mouse press
    if mouse_pressed:
        message = "Mouse Button Down!"
        color = (255, 0, 0)
    else:
        message = "Click the Mouse Button"
        color = (0, 0, 255)

    # Fill the background with white
    window.fill((255, 255, 255))

    # Draw a text message on the screen
    large_text = pygame.font.SysFont(None, 70).render(message, True, color)
    window.blit(large_text, (100, 100))

    # Update the display
    pygame.display.flip()

    # Cap framerate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()