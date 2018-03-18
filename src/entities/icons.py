from src.etc import spritesheet

"""
icons.py

This file defines class for various
small icons that appear about the place
"""

sprite_sheet = None


def load_sprite_sheet():

    global sprite_sheet
    sprite_sheet = spritesheet.SpriteSheet("src/resources/icons.png")


class Icon:

    def __init__(self, image, x, y, flash=False, flash_threshold=0):

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y

        self.offset_x = self.rect.x
        self.offset_y = self.rect.y

        self.flash = flash
        self.flash_threshold = flash_threshold
        self.flash_counter = 0

        self.visible = True
        self.force_off = False

    def update(self):

        if self.flash:
            self.flash_counter += 1

            if self.flash_counter > self.flash_threshold:
                self.flash_counter = 0
                self.visible = False if self.visible else True

    def draw(self, display):

        if self.visible and not self.force_off:
            display.blit(self.image, (self.rect.x, self.rect.y))

    def realign(self, x, y):

        self.rect.x = x + self.offset_x
        self.rect.y = y + self.offset_y

    def off(self):
        self.force_off = True

    def on(self):
        self.force_off = False


class PressSpace(Icon):

    def __init__(self, x, y):

        Icon.__init__(self, sprite_sheet.get_image(0, 0, 40, 28), x, y, True, 40)


class ArrowPointer(Icon):

    def __init__(self, x, y):

        Icon.__init__(self, sprite_sheet.get_image(40, 0, 7, 14), x, y)

    def realign(self, x, y):

        self.rect.x = x
        self.rect.y = y


class ImportantPressSpace(Icon):

    def __init__(self, x, y):

        Icon.__init__(self, sprite_sheet.get_image(0, 28, 56, 28), x, y, True, 40)


class ExclamationMark(Icon):

    def __init__(self, x, y):

        Icon.__init__(self, sprite_sheet.get_image(50, 28, 4, 28), x, y, True, 25)


class ArrowIndicator(Icon):

    def __init__(self, x, y):

        Icon.__init__(self, sprite_sheet.get_image(180, 132, 40, 40), x, y, True, 25)
