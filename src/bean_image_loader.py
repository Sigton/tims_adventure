from src import spritesheet

"""
bean_image_loader.py

This file loads all 
the bean images
"""

sprite_sheet = None


def load_sprite_sheet():

    global sprite_sheet
    sprite_sheet = spritesheet.SpriteSheet("src/resources/beans.png")
