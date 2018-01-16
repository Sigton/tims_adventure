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

    new_save_button = [
        (0, 276, 196, 85),
        (196, 276, 196, 85),
        (392, 276, 196, 85)
    ]

    load_save_button = [
        (0, 361, 196, 85),
        (196, 361, 196, 85),
        (392, 361, 196, 85),
    ]

    delete_save_button = [
        (0, 446, 196, 85),
        (196, 446, 196, 85),
        (392, 446, 196, 85)
    ]

    cancel_save_button = [
        (0, 531, 196, 85),
        (196, 531, 196, 85),
        (392, 531, 196, 85)
    ]


def load_images():

    sprite_sheet = spritesheet.SpriteSheet("src/resources/menu_buttons.png")

    images = {
        "play_button": [sprite_sheet.get_image_src_alpha(image[0],
                                                         image[1],
                                                         image[2],
                                                         image[3]) for image in
                        SpriteSheetData.play_button],
        "option_button": [sprite_sheet.get_image_src_alpha(image[0],
                                                           image[1],
                                                           image[2],
                                                           image[3]) for image in
                          SpriteSheetData.options_button],
        "quit_button": [sprite_sheet.get_image_src_alpha(image[0],
                                                         image[1],
                                                         image[2],
                                                         image[3]) for image in
                        SpriteSheetData.quit_button],
        "new_save_button": [sprite_sheet.get_image_src_alpha(image[0],
                                                             image[1],
                                                             image[2],
                                                             image[3]) for image in
                            SpriteSheetData.new_save_button],
        "load_save_button": [sprite_sheet.get_image_src_alpha(image[0],
                                                              image[1],
                                                              image[2],
                                                              image[3]) for image in
                             SpriteSheetData.load_save_button],
        "delete_save_button": [sprite_sheet.get_image_src_alpha(image[0],
                                                                image[1],
                                                                image[2],
                                                                image[3]) for image in
                               SpriteSheetData.delete_save_button],
        "cancel_save_button": [sprite_sheet.get_image_src_alpha(image[0],
                                                                image[1],
                                                                image[2],
                                                                image[3]) for image
                               in SpriteSheetData.cancel_save_button]
    }

    return images
