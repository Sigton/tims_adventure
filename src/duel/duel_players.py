import pygame

from src.entities import shadows

"""
duel_players.py

Classes that hold attributes related
to the player and enemy in duelling
"""


class DuelPlayer:

    def __init__(self, player, facing):

        self.meta = player.meta
        self.facing = facing

        self.energy = self.meta.energy

        self.image = pygame.transform.scale(self.meta.images["G" + self.facing if self.meta.evil else self.facing],
                                            (300, 300) if self.facing == "R" else (230, 230))

        self.rect = self.image.get_rect()
        self.rect.x = 75 if self.facing == "R" else 640
        self.rect.y = 368 if self.facing == "R" else 53

        self.default_x = self.rect.x
        self.default_y = self.rect.y

        self.tile_code = "duel_{}".format("player" if self.facing == "R" else "enemy")

        self.shadow = shadows.Shadow(self)

        self.shake = 0
        self.shake_distance = 0
        self.shake_w = 0
        self.shake_shift = 0
        self.shake_timer = 0
        self.shake_direction = 0

        self.terrain_entity = player
