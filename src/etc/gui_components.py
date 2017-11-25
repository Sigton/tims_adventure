import pygame

from src.etc import constants

"""
gui_components.py

This file holds generic items
found on most gui's
"""


class Button:

    def __init__(self, images, x, y, command):

        self.inactive_image = images[0]
        self.active_image = images[1]

        self.image = self.inactive_image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.command = command

    def update(self):

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = self.active_image

            if pygame.mouse.get_pressed()[0]:
                self.command()

        else:
            self.image = self.inactive_image

    def draw(self, display):

        display.blit(self.image, (self.rect.x, self.rect.y))


class ProgressBar:

    def __init__(self, x, y, length, width, colors):

        self.back_color = colors[0]
        self.fill_color = colors[1]

        self.width = width
        self.length = length

        self.start_image = pygame.Surface([length, width]).convert()
        self.new_image = None

        pygame.draw.line(self.start_image, self.back_color, (0, width//2), (length, width//2), width)

        self.image = self.start_image
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y - width//2

    def update(self, percent):

        if percent == 0:
            return

        self.new_image = self.start_image.copy()

        pygame.draw.line(self.new_image, self.fill_color,
                         (0, self.width//2), (self.length*percent, self.width//2),
                         self.width)

        self.image = self.new_image

    def draw(self, display):

        display.blit(self.image, (self.rect.x, self.rect.y))


class Label:

    def __init__(self, x, y, text):

        self.image = constants.font.render(text, False, constants.WHITE)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def draw(self, display):

        display.blit(self.image, (self.rect.x, self.rect.y))
