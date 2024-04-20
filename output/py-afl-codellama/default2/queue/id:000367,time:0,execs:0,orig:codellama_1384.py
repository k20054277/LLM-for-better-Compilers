import pygame

# Initialize pygame
pygame.init()

# Set the screen dimensions
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Assert and Pygame Example")

# Load a font object
font = pygame.font.SysFont(None, 32)

# Define a function to draw text on the screen
def draw_text(text):
    # Create a surface object from the given text
    surface = font.render(text, True, (0, 0, 0))
    
    # Get the width and height of the text
    text_width, text_height = surface.get_size()
    
    # Draw the text on the screen at position (10, 10)
    screen.blit(surface, (10, 10))
    
# Define a function to handle key presses
def handle_keypress(event):
    if event.type == pygame.KEYDOWN:
        # Check if the user pressed the space bar
        if event.key == pygame.K_SPACE:
            # Draw some text on the screen
            draw_text("You pressed the space bar!")
        else:
            # Print an error message to the console
            print("Invalid key press.")

# Main game loop
while True:
    # Handle events (keyboard presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        handle_keypress(event)
    
    # Flip the display buffer to show what has been drawn on it
    pygame.display.flip()