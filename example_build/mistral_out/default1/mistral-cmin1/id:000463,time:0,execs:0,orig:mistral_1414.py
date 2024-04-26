
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    # Create the game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Game loop flag
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        # Draw a red rectangle every frame (for demonstration purposes)
        rect = pygame.Rect(50, 50, 100, 100)
        pygame.draw.rect(screen, (255, 0, 0), rect)

        # Flip the display
        pygame.display.flip()

    # Quit Pygame and clean up
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

# Assert statements for debugging
def check_event(event):
    assert event.type in [pygame.QUIT], "Unexpected event type: {}".format(event.type)

# Example usage of the check_event function
for event in pygame.event.get():
    check_event(event)
