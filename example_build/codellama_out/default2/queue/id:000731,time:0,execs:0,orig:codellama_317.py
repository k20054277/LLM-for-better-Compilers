import pygame

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((640, 480))

# Set the title of the window
pygame.display.set_caption("My Game")

# Loop until the user closes the window
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw some text
    myfont = pygame.font.SysFont("Arial", 18)
    text = "Hello World!"
    text_rect = myfont.render(text, True, (255, 255, 255))
    screen.blit(text_rect, (10, 10))

    # Update the display
    pygame.display.flip()

# Close pygame
pygame.quit()