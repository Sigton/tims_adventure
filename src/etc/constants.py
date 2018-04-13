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

default_start = (-15480, -64752)

no_spawn_chunks = ['1488', '1489', '1490', '1491', '1492', '1493',
                   '1588', '1589', '1590', '1591', '1592', '1593',
                   '1688', '1689', '1690', '1691', '1692', '1693',
                   '1788', '1789', '1790', '1791', '1792', '1793',
                   '1888', '1889', '1890', '1891', '1892', '1893',
                   '1988', '1989', '1990', '1991', '1992', '1993',
                   '1587', '1685', '1686', '1687', '1785', '1786',
                   '1787', '1885', '1886', '1887', '1985', '1986',
                   '1987', '2085', '2086', '2087', '2088', '2185',
                   '2186', '2187', '2188', '2189', '2285', '2286',
                   '2287', '2288', '2289', '2386', '2387', '2388',
                   '2389']

no_spawn_beans = ["wizard", "old_villager", "tim"]


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

evil_bean_particle_rate = 100


# Tile information

animation_thresholds = {
    "0030": 4,
    "0072": 12,
    "0073": 12
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
    "Tackle",
    "Punch"
]
positional_moves = [
    "Burn",
    "Freeze",
    "Chili Chuck"
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


footstep_types = {
    "0000": "footstep2",
    "0041": "footstep2",
    "0042": "footstep2",
    "0073": "footstep3",
    "0050": "footstep4"
}

footstep_sounds = [
    "footstep",
    "footstep2",
    "footstep3",
    "footstep4"
]

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


# Items & Quests

items = [
    "EnlightenmentPotion",
    "HealthPotion"
]

item_display_names = {
    "EnlightenmentPotion": "Enlightenment",
    "HealthPotion": "Healing"
}

healing_items = [
    "HealthPotion"
]

drinking_items = [
    "HealthPotion"
]

item_images = {
    "EnlightenmentPotion": (62, 11, 32, 32),
    "HealthPotion": (94, 11, 32, 32)
}

quest_images = {
    "talk_villagers": (0, 236, 32, 32),
    "old_man": (32, 236, 32, 32),
    "heading_north": (64, 236, 32, 32),
    "help_village": (96, 236, 32, 32),
    "liberate_village": (128, 236, 32, 32),
    "fisherman": (160, 236, 32, 32),
    "learn_fight": (192, 236, 32, 32),
    "old_man2": (32, 236, 32, 32),
}
