from src import spritesheet

'''
tile_image_loader.py

This file loads all of the tile images,
so they can be quickly accessed to improve performance.
'''

# Sprite sheet data
# This is where each tile can be found on terrain.png

generic_ground = (0, 0, 48, 48)
water = (48, 0, 48, 48)

tiles = [generic_ground, water]
images = []

sprite_sheet = None


def load_images():

    global sprite_sheet, images

    sprite_sheet = spritesheet.SpriteSheet("resources/terrain.png")

    images += [sprite_sheet.get_image(tile[0],
                                      tile[1],
                                      tile[2],
                                      tile[3]) for tile in tiles]
