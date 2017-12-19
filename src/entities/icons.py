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
        self.rect.x = x
        self.rect.y = y

        self.flash = flash
        self.flash_threshold = flash_threshold
        self.flash_counter = 0

        self.visible = True

    def update(self):

        self.flash_counter += 1

        if self.flash_counter > self.flash_threshold:
            self.flash_counter = 0
            self.visible = False if self.visible else True

    def draw(self, display):

        if self.visible:
            display.blit(self.image, (self.rect.x, self.rect.y))


class PressSpace(Icon):

    def __init__(self):

        Icon.__init__(self, sprite_sheet.get_image(0, 0, 40, 28), 0, 0, True, 40)
