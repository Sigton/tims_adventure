import pygame

"""
Constants.py

This file defines variables
that will remain unchanged
throughout the entirety of
the program.
"""

# Display dimensions

DISPLAY_WIDTH = 960
DISPLAY_HEIGHT = 720
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
DISPLAY_CENTER = (DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2)

# Colours

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

HEALTH_BAR_GREEN = (88, 152, 68)
HEALTH_BAR_RED = (172, 71, 71)
XP_BAR_CYAN = (78, 165, 215)
XP_BAR_BLUE = (19, 82, 196)
ENERGY_BAR_YELLOW = (225, 241, 45)
ENERGY_BAR_ORANGE = (193, 110, 29)

GUI_BACKING = (40, 48, 48)
GUI_FILL = (248, 248, 216)

# Terrain Generation Constants

tile_w = 48
tile_h = 48

chunk_w = 20
chunk_h = 15
num_tiles = chunk_w * chunk_h

default_start = (-16344, -66240)


# Entity Spawning data

weights = [0, 0, 0, 1]

entity_selection_matrix = [int(x) for x in sum([list(x * y) for x, y in zip(["0", "1", "2", "3"], weights)], [])]


# Assorted variables

dir_to_movements = {
    "U": (0, 48),
    "D": (0, -48),
    "R": (-48, 0),
    "L": (48, 0)
}


# Player constants
movement_speed = 12  # Must be a factor of 48

player_pos_x = 460
player_pos_y = 340

player_pos = (player_pos_x, player_pos_y)

max_trail_offset = [0, 1, 2, 3, 4]

shadow_offset = 0.85

interaction_distance = 75

health_update_rate = 120


# Tile information

animation_thresholds = {
    "0030": 4
}

no_fade_sprites = [
    "Bean",
    "RandomBean",
    "EnlightenmentPotion",
    "HealthPotion"
]


# Entity constants
level_up_base = 50
level_up_multiplier = 1.5


# The global font to write with
font = None
default_font_size = 32


def load_font(font_size=default_font_size, set_global=True):

    global font

    if set_global:
        font = pygame.font.Font("src/resources/font.otf", font_size)
    else:
        return pygame.font.Font("src/resources/font.otf", font_size)


# Data used in dueling engine

shake_moves = [
    "Tackle"
]
positional_moves = [
    "Burn",
    "Freeze"
]

turn_cool_down = 60


# User Events

MUSIC_END_EVENT = pygame.USEREVENT+1
MUSIC_START_EVENT = pygame.USEREVENT+2


# Save Engine vars

DEFAULT_SAVE_DIRECTORY = "src\\saves\\gamesaves"


# etc

FPS = 45

LOADING_SCREEN_TIME = 45
PARTICLE_LIFE_MULTIPLIER = 0.75


# Performance control

performance_profiles = [
    {"fps": 60, "loading": 60, "particle": 1, "cooldown": 80, "movement": 16},
    {"fps": 45, "loading": 45, "particle": 0.75, "cooldown": 60, "movement": 12},
    {"fps": 30, "loading": 30, "particle": 0.5, "cooldown": 40, "movement": 8},
    {"fps": 15, "loading": 15, "particle": 0.25, "cooldown": 20, "movement": 4}
]


def load_performance_profile(idx):

    global FPS, LOADING_SCREEN_TIME, PARTICLE_LIFE_MULTIPLIER, turn_cool_down, movement_speed

    profile = performance_profiles[idx]

    FPS = profile["fps"]
    LOADING_SCREEN_TIME = profile["loading"]
    PARTICLE_LIFE_MULTIPLIER = profile["particle"]
    turn_cool_down = profile["cooldown"]
    movement_speed = profile["movement"]


# Bean related

bean_image_offset = {
    "carrot": (0, 3),
    "wizard": (0, 10)
}


# Items

items = [
    "EnlightenmentPotion",
    "HealthPotion"
]

item_display_names = {
    "EnlightenmentPotion": "Enlightenment",
    "HealthPotion": "Healing"
}

item_images = {
    "EnlightenmentPotion": (62, 11, 32, 32),
    "HealthPotion": (94, 11, 32, 32)
}
