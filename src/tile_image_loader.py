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
path_1 = (0, 48, 48, 48)
path_2 = (48, 48, 48, 48)
path_3 = (96, 48, 48, 48)
path_4 = (144, 48, 48, 48)
path_5 = (192, 48, 48, 48)
path_6 = (240, 48, 48, 48)
path_7 = (288, 48, 48, 48)
path_8 = (336, 48, 48, 48)
path_9 = (0, 96, 48, 48)
path_10 = (48, 96, 48, 48)
path_11 = (96, 96, 48, 48)
path_12 = (144, 96, 48, 48)
path_13 = (192, 96, 48, 48)
path_14 = (240, 96, 48, 48)
path_15 = (288, 96, 48, 48)
dark_ground = (96, 0, 48, 48)
wall_1 = (0, 144, 48, 48)
wall_2 = (48, 144, 48, 48)
wall_3 = (96, 144, 48, 48)

tiles = [generic_ground, water, path_1,
         path_2, path_3, path_4, path_5,
         path_6, path_7, path_8, path_9,
         path_10, path_11, path_12,
         path_13, path_14, path_15,
         dark_ground, wall_1, wall_2,
         wall_3]
images = []

sprite_sheet = None


def load_images():

    global sprite_sheet, images

    sprite_sheet = spritesheet.SpriteSheet("src/resources/terrain.png")

    images += [sprite_sheet.get_image(tile[0],
                                      tile[1],
                                      tile[2],
                                      tile[3]) for tile in tiles]
