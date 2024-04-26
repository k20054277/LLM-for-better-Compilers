
import pygame

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 640
HEIGHT = 480
FPS = 60

# Create a Pygame display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Get the current window object and name it 'window'
window = pygame.display.get_wm_id()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the window title every frame
    pygame.display.set_caption(f"Pygame Window - Frame {pygame.time.get_frames()}")

    # Fill the screen with a solid color
    screen.fill((30, 30, 30))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(FPS)

# Quit Pygame
pygame.quit()
