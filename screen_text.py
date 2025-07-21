"""
Module for displaying styled text on the screen using pygame.

Classes:
- ScreenText: A class to render and display text using a specific font, size, color, and position.
"""

import pygame
pygame.init()

class screen_text:
    """
    Represents a text element rendered on a Pygame surface.

    Attributes:
    - text (str): The text to display.
    - color (tuple): The RGB color of the text.
    - surf (pygame.Surface): The rendered text surface.
    - rect (pygame.Rect): The rectangle defining the position of the text on screen.

    Methods:
    - show(screen): Draws the text surface onto the given screen.
    """

    def __init__(self, text, font_size=25, cent=(640, 420), color=(225, 238, 242)):
        """
        Initializes the ScreenText object.

        Parameters:
        - text (str): The text content.
        - font_size (int): Font size of the text (default is 25).
        - cent (tuple): The (x, y) position where the text will be centered.
        - color (tuple): RGB color of the text (default is light blue).
        """
        main_font_dir = 'fonts/CascadiaMonoRegular.otf'
        base_font = pygame.font.Font(main_font_dir, font_size)
        self.color = color
        self.text = text
        self.surf = base_font.render(text, True, self.color)
        self.rect = self.surf.get_rect(center=cent)

    def show(self, screen: pygame.Surface) -> None:
        """
        Draws the text onto the given screen.

        Parameters:
        - screen (pygame.Surface): The Pygame screen to draw the text on.
        """
        screen.blit(self.surf, self.rect)