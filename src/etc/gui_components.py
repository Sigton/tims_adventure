import pygame

from src.etc import constants

"""
gui_components.py

This file holds generic items
found on most gui's
"""


class Button:

    def __init__(self, images, x, y, command, active=True):

        self.inactive_image = images[0]
        self.active_image = images[1]
        self.deactivated_image = images[2]

        self.image = self.inactive_image if active else self.deactivated_image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.command = command

        self.pressed = False

    def update(self, active=True):

        if not active:
            self.image = self.deactivated_image
            return

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = self.active_image

            if pygame.mouse.get_pressed()[0]:
                if not self.pressed:
                    self.command()
                self.pressed = True
            else:
                self.pressed = False

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
            self.image = self.start_image
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

    def update(self, text):

        old_pos = self.rect.topleft

        self.image = constants.font.render(text, False, constants.WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = old_pos

    def draw(self, display):

        display.blit(self.image, (self.rect.x, self.rect.y))
