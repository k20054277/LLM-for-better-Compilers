
import pygame
import sys

# Set up some constants
WIDTH = 500
HEIGHT = 500
CROSS_SIZE = 100

# Initialize Pygame and set the display mode
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame False Example')

# Define a function for drawing a cross on the screen
def draw_cross(surface):
    pygame.draw.line(surface, (255, 0, 0), (WIDTH // 2, HEIGHT // 2), (WIDTH // 2 + CROSS_SIZE, HEIGHT // 2), 10)
    pygame.draw.line(surface, (255, 0, 0), (WIDTH // 2, HEIGHT // 2), (WIDTH // 2, HEIGHT // 2 + CROSS_SIZE), 10)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill((255, 255, 255))
    
    # Draw a cross in the center of the screen
    draw_cross(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame and clean up resources
pygame.quit()
sys.exit()
