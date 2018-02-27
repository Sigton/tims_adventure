from src.etc import spritesheet

"""
bean_image_loader.py

This file loads all 
the bean images
"""

sprite_sheet = None

chili = lambda: sprite_sheet.get_image(0, 0, 40, 40)
cool = lambda: sprite_sheet.get_image(40, 0, 40, 40)
pickle = lambda: sprite_sheet.get_image(80, 0, 40, 40)
strawberry = lambda: sprite_sheet.get_image(120, 0, 40, 40)
lemon = lambda: sprite_sheet.get_image(160, 0, 40, 40)
rainbow = lambda: sprite_sheet.get_image(200, 0, 40, 40)
unicorn = lambda: sprite_sheet.get_image(240, 0, 40, 40)
hedgehog = lambda: sprite_sheet.get_image(280, 0, 40, 40)
poison = lambda: sprite_sheet.get_image(320, 0, 40, 40)
carrot = lambda: sprite_sheet.get_image(0, 40, 42, 46)
rabbit = lambda: sprite_sheet.get_image(360, 0, 40, 40)
what = lambda: sprite_sheet.get_image(42, 40, 40, 40)
chicken = lambda: sprite_sheet.get_image(82, 40, 40, 40)

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


def load_sprite_sheet():

    global sprite_sheet
    sprite_sheet = spritesheet.SpriteSheet("src/resources/beans.png")

def create_images(bean):

    pass
