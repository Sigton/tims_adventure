from src.etc import spritesheet

"""
menu_image_loader.py

This file loads the different images
used in the main menu
"""


class SpriteSheetData:

    play_button = [
        (0, 0, 212, 92),
        (212, 0, 212, 92),
        (424, 0, 212, 92)
    ]

    options_button = [
        (0, 92, 212, 92),
        (212, 92, 212, 92),
        (424, 92, 212, 92)
    ]

    quit_button = [
        (0, 184, 212, 92),
        (212, 184, 212, 92),
        (424, 92, 212, 92)
    ]


def load_images():

    sprite_sheet = spritesheet.SpriteSheet("src/resources/menu_buttons.png")

    images = {

    }

    return images
