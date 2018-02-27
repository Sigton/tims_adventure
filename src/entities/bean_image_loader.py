from src.etc import spritesheet

"""
bean_image_loader.py

This file loads all 
the bean images
"""

sprite_sheet = None

chili = (0, 0, 40, 40)
cool = (40, 0, 40, 40)
pickle = (80, 0, 40, 40)
strawberry = (120, 0, 40, 40)
lemon = (160, 0, 40, 40)
rainbow = (200, 0, 40, 40)
unicorn = (240, 0, 40, 40)
hedgehog = (280, 0, 40, 40)
poison = (320, 0, 40, 40)
carrot = (0, 40, 42, 46)
rabbit = (360, 0, 40, 40)
what = (42, 40, 40, 40)
chicken = (82, 40, 40, 40)

beans = {}


def load_sprite_sheet():

    global sprite_sheet, beans
    sprite_sheet = spritesheet.SpriteSheet("src/resources/beans.png")

    beans = {
        "chili": chili,
        "cool": cool,
        "pickle": pickle,
        "strawberry": strawberry,
        "lemon": lemon,
        "rainbow": rainbow,
        "unicorn": unicorn,
        "hedgehog": hedgehog,
        "poison": poison,
        "carrot": carrot,
        "rabbit": rabbit,
        "what": what,
        "chicken": chicken
    }

