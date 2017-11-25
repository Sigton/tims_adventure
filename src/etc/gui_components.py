import pygame

"""
gui_components.py

This file holds generic items
found on most gui's
"""


class Button:

    def __init__(self, images, x, y):

        self.inactive_image = images[0]
        self.active_image = images[1]

        self.image = self.inactive_image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = self.active_image
        else:
            self.image = self.inactive_image

    def draw(self, display):

        display.blit(self.image, (self.rect.x, self.rect.y))
