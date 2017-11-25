import pygame

from src.etc import spritesheet

"""
duel_gui.py

This loads the components of the
user interface for the duel scenes
"""


class SpriteSheetData:

    attack_main_button = [
        (0, 460, 202, 41),
        (202, 460, 202, 41)
    ]

    attack_alt_button = [
        (0, 501, 202, 41),
        (202, 501, 202, 41)
    ]

    item_button = [
        (0, 542, 202, 41),
        (202, 542, 202, 41)
    ]

    retreat_button = [
        (0, 583, 202, 41),
        (202, 583, 202, 41)
    ]


def load_images():

    sprite_sheet = spritesheet.SpriteSheet("src/resources/duel_gui_buttons.png")

    images = {
        "attack_main_button": [sprite_sheet.get_image(image[0],
                                                      image[1],
                                                      image[2],
                                                      image[3]) for image in SpriteSheetData.attack_main_button],
        "attack_alt_button": [sprite_sheet.get_image(image[0],
                                                     image[1],
                                                     image[2],
                                                     image[3]) for image in SpriteSheetData.attack_main_button],
        "item_button": [sprite_sheet.get_image(image[0],
                                               image[1],
                                               image[2],
                                               image[3]) for image in SpriteSheetData.attack_main_button],
        "retreat_button": [sprite_sheet.get_image(image[0],
                                                  image[1],
                                                  image[2],
                                                  image[3]) for image in SpriteSheetData.attack_main_button],
        "background": pygame.image.load("src/resources/duel_gui.png").convert()
    }

    return images
