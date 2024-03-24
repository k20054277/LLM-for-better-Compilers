import pygame

# Initialize pygame
pygame.init()

# Set up the window and title
window_width = 640
window_height = 480
title = "And Example"
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(title)

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Draw a rectangle on the screen
rectangle = pygame.Rect(100, 100, 300, 300)
pygame.draw.rect(screen, BLACK, rectangle)

# Set up the user input events
events = pygame.event.get()
for event in events:
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Get the position of the mouse click
        pos = pygame.mouse.get_pos()
        
        # Check if the click was within the rectangle
        if rectangle.collidepoint(pos):
            print("Clicked inside the rectangle!")
        else:
            print("Clicked outside the rectangle.")