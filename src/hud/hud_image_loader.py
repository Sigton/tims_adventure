from src.etc import spritesheet

"""
hud_image_loader.py

Loads various images that are used in the hud widgets
"""


sprite_sheet = None


sprite_sheet_data = {
    "inventory_button": [
        (0, 56, 60, 60),
        (0, 116, 60, 60),
        (0, 176, 60, 60)
    ],
    "journal_button": [
        (60, 60, 60, 52),
        (60, 120, 60, 52),
        (60, 180, 60, 52)
    ],
    "map_button": [
        (120, 56, 60, 60),
        (120, 116, 60, 60),
        (120, 176, 60, 60)
    ],
    "open_hud_button": [
        (180, 56, 16, 38),
        (196, 56, 16, 38),
        (212, 56, 16, 38)
    ],
    "close_hud_button": [
        (180, 94, 16, 38),
        (196, 94, 16, 38),
        (212, 94, 16, 38)
    ],
    "health_button": [
        (228, 56, 60, 60),
        (228, 116, 60, 60),
        (228, 176, 60, 60)
    ],
    "compass": [
        (288, 0, 148, 148)
    ]
}


def load_sprite_sheet():

    global sprite_sheet
    sprite_sheet = spritesheet.SpriteSheet("src/resources/icons.png")


def load_images(image):

    return [sprite_sheet.get_image(i[0],
                                   i[1],
                                   i[2],
                                   i[3]) for i in sprite_sheet_data[image]]
