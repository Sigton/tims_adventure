import pygame

"""
duel_gui.py

This loads the components of the
user interface for the duel scenes
"""


class SpriteSheetData:

    enemy_back_plate = (0, 0, 480, 150)
    player_back_plate = (0, 150, 480, 310)

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
