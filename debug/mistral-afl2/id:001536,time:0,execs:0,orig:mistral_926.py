
import pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BUTTON_WIDTH, BUTTON_HEIGHT = 150, 50
MARGIN = 20

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Example")

def draw_button(screen, text, x, y):
    button_surface = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
    button_surface.fill(WHITE)
    small_text = pygame.font.SysFont(None, 18).render(text, (0, 0, 0), WHITE)
    button_rect = button_surface.get_rect()
    screen.blit(button_surface, (x, y))
    screen.blit(small_text, (x + BUTTON_WIDTH / 2 - small_text.get_width() / 2, y + BUTTON_HEIGHT / 2))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw and handle Button1 clicks
    button1_x, button1_y = MARGIN, MARGIN * 2 + BUTTON_HEIGHT
    pygame.draw.rect(screen, (0, 128, 0), (button1_x, button1_y, BUTTON_WIDTH, BUTTON_HEIGHT))
    mouse_pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] and (button1_x <= mouse_pos[0] <= button1_x + BUTTON_WIDTH and button1_y <= mouse_pos[1] <= button1_y + BUTTON_HEIGHT):
        print("You clicked Button1!")
    draw_button(screen, "Button1", button1_x, button1_y)

    # Draw and handle Button2 clicks
    button2_x, button2_y = MARGIN * 3 + BUTTON_WIDTH + MARGIN, MARGIN * 2 + BUTTON_HEIGHT
    pygame.draw.rect(screen, (128, 0, 0), (button2_x, button2_y, BUTTON_WIDTH, BUTTON_HEIGHT))
    if pygame.mouse.get_pressed()[0] and (button2_x <= mouse_pos[0] <= button2_x + BUTTON_WIDTH and button2_y <= mouse_pos[1] <= button2_y + BUTTON_HEIGHT):
        print("You clicked Button2!")
    draw_button(screen, "Button2", button2_x, button2_y)

    pygame.display.flip()

pygame.quit()
