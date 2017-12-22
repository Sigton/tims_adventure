import pygame

from src.entities import shadows
from src.entities.entities import EntityMeta

"""
duel_players.py

Classes that hold attributes related
to the player and enemy in duelling
"""


class DuelPlayer(EntityMeta):

    def __init__(self, player, facing):

        EntityMeta.__init__(self, player)

        self.facing = facing

        self.energy_max = self.energy
        self.energy = self.energy_max

        self.image = pygame.transform.scale(self.images[self.facing],
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
