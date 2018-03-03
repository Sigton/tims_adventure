import pygame

from src.etc import constants, tools

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
        self.force_off = False
        self.force_on = False
        self.active = False

    def update(self, active=True):

        self.active = False
        if not active or self.force_off:
            self.image = self.deactivated_image
            return

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = self.active_image
            self.active = True

            if pygame.mouse.get_pressed()[0]:
                if not self.pressed:
                    if self.command is not None:
                        self.command()
                self.pressed = True
            else:
                self.pressed = False

        elif not self.force_on:
            self.image = self.inactive_image
        else:
            self.image = self.active_image

    def draw(self, display):

        display.blit(self.image, (self.rect.x, self.rect.y))

    def set_off(self):
        self.force_off = True

    def set_on(self):
        self.force_off = False

    def force_active(self):
        self.force_on = True

    def no_force_active(self):
        self.force_on = False


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

    def __init__(self, x, y, text, center=False, text_size=32, color=constants.WHITE):

        self.color = color
        self.text_size = text_size

        if text_size != constants.default_font_size:
            self.image = constants.load_font(self.text_size, False).render(text, False, self.color)
        else:
            self.image = constants.font.render(text, False, color)
        self.rect = self.image.get_rect()

        if center:
            self.rect.centerx = x
            self.rect.centery = y
        else:
            self.rect.x = x
            self.rect.y = y

    def update(self, text):

        old_pos = self.rect.topleft

        self.image = self.image = constants.load_font(self.text_size, False).render(text, False, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = old_pos

    def draw(self, display):

        display.blit(self.image, (self.rect.x, self.rect.y))


class Fill:

    def __init__(self, x, y, width, height, color):

        self.color = color

        self.image = pygame.Surface([width, height]).convert()
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def resize(self, width, height):

        old_pos = self.rect.topleft

        self.image = pygame.Surface([width, height]).convert()
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.topleft = old_pos

    def draw(self, display):

        display.blit(self.image, (self.rect.x, self.rect.y))


class Fade:

    def __init__(self):

        self.image = pygame.Surface(constants.DISPLAY_SIZE).convert()
        self.image.fill(constants.BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.opacity = 255

    def update(self):

        pass

    def draw(self, display):

        if self.opacity == 255:
            display.blit(self.image, (self.rect.x, self.rect.y))
        elif self.opacity == 0:
            return
        else:
            tools.blit_alpha(display, self.image, self.rect.topleft, self.opacity)

    def set_opacity(self, opacity):

        self.opacity = opacity


class Image:

    def __init__(self, image_path, x=0, y=0, load_image=True):

        if load_image:
            self.image = pygame.image.load(image_path).convert()
        else:
            self.image = image_path

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, display):

        display.blit(self.image, (self.rect.x, self.rect.y))


class Tooltip:

    def __init__(self, text, x, y, size, colour, direction):

        self.text = Label(x+8, y+2, text, False, size, colour)
        self.background = Fill(x, y, self.text.rect.width+16, self.text.rect.height+8, constants.GUI_BACKING)
        self.background_fill = Fill(x+4, y+4, self.text.rect.width+8, self.text.rect.height, constants.GUI_FILL)

        self.direction = direction

        self.x = x if self.direction == "R" else x-self.background.rect.width
        self.y = y

        self.components = [
            self.background,
            self.background_fill,
            self.text
        ]

        self.on = False

    def update(self):
        pass

    def reposition(self, pos):
        self.x = pos[0] if self.direction == "R" else pos[0]-self.background.rect.width
        self.y = pos[1]

        self.background.rect.topleft = (self.x, self.y)
        self.background_fill.rect.topleft = (self.x+4, self.y+4)
        self.text.rect.topleft = (self.x+8, self.y+2)

    def draw(self, display):

        if self.on:
            [component.draw(display) for component in self.components]

    def set_on(self):
        self.on = True

    def set_off(self):
        self.on = False
