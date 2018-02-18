from src.etc import spritesheet

"""
bean_image_loader.py

This file loads all 
the bean images
"""

sprite_sheet = None

chili = lambda: sprite_sheet.get_image(0, 0, 40, 40)
cool = lambda: sprite_sheet.get_image(40, 0, 40, 40)
green = lambda: sprite_sheet.get_image(80, 0, 40, 40)
strawberry = lambda: sprite_sheet.get_image(120, 0, 40, 40)
lemon = lambda: sprite_sheet.get_image(160, 0, 40, 40)

beans = {
    "chili": chili,
    "cool": cool,
    "green": green,
    "strawberry": strawberry,
    "lemon": lemon
}


def load_sprite_sheet():

    global sprite_sheet
    sprite_sheet = spritesheet.SpriteSheet("src/resources/beans.png")
