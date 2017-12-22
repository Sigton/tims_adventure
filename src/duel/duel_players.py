import pygame

from src.entities import shadows

"""
duel_players.py

Classes that hold attributes related
to the player and enemy in duelling
"""


class DuelPlayer:

    def __init__(self, player, side):

        self.meta = player.meta
        self.side = side

        self.energy_max = self.meta.energy
        self.energy = self.energy_max

        self.image = pygame.transform.scale(self.meta.images[self.side], (300, 300) if self.side == "R" else (230, 230))

        self.rect = self.image.get_rect()
        self.rect.x = 75 if self.side == "R" else 640

        self.default_x = self.rect.x

        self.shadow = shadows.Shadow(self)

        self.shake = 0
        self.shake_distance = 0
        self.shake_w = 0
        self.shake_shift = 0
        self.shake_timer = 0
        self.shake_direction = 0
