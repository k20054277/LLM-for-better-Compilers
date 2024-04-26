
import pygame
import unittest

# Initialize pygame
pygame.init()

# Define a test case
class TestPygame(unittest.TestCase):

    def setUp(self):
        self.screen = pygame.display.set_mode((640, 480))

    def test_pygame_surface(self):
        # Create a surface and fill it with red
        surface = pygame.Surface((100, 100))
        surface.fill((255, 0, 0))

        # Check if the surface is red
        self.assertEqual(surface.get_color((0, 0, 0)), (255, 0, 0))

    def tearDown(self):
        pygame.quit()

# Run the tests
unittest.main()
