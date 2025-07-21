"""
image_utils.py

Utility module for displaying images in Pygame with optional transparency.

Classes:
    ScreenImage: Loads and displays an image surface centered on the screen.
"""

import pygame

pygame.init()

class screen_image:
    """
    Loads an image and prepares it for display on a Pygame screen.

    Args:
        path (str): Path to the image file.
        transparent (bool): If True, loads image with alpha transparency. Defaults to True.
        c (tuple[int, int]): Coordinates of the center where the image will be positioned. Defaults to (640, 360).
    """

    def __init__(self, path: str, transparent: bool = True, c: tuple[int, int] = (640, 360)) -> None:
        if transparent:
            self.surf = pygame.image.load(path).convert_alpha()
        else:
            self.surf = pygame.image.load(path).convert()
        self.rect = self.surf.get_rect(center=c)

    def show(self, screen: pygame.Surface) -> None:
        """
        Draws the image onto the provided Pygame screen surface.

        Args:
            screen (pygame.Surface): The target surface (usually the main screen) to draw the image on.
        """
        screen.blit(self.surf, self.rect)