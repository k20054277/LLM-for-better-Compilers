
# Import required modules
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 500, 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_text(surface, text, pos, color=WHITE):
    """This function will draw text on the given surface."""
    font = pygame.font.Font(None, 32)
    text_surface = font.render(text, False, color)
    rect = text_surface.get_rect()
    rect.topleft = pos
    surface.blit(text_surface, rect)

def main():
    # Set up the display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("None and Pygame example")

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Draw some text using the draw_text function with None as a default color
        draw_text(screen, "Hello World!", (50, 50))
        draw_text(screen, "None is a placeholder value in Python", (50, 100), None)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
