import pygame

# Initialize pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((640, 480))

# Set the title of the window
pygame.display.set_caption("My Game")

# Loop until the user clicks the close button
done = False
while not done:
    # Handle events (keyboard and mouse)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen to a blue color
    screen.fill((0, 0, 255))

    # Draw some text on the screen
    text_surface = font.render("Hello World!", True, (255, 255, 255))
    screen.blit(text_surface, (100, 100))

    # Update the screen
    pygame.display.flip()