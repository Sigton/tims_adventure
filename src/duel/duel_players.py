import pygame

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

        self.image = pygame.transform.scale(self.meta.images[self.side], (300, 300) if self.side=="R" else (230, 230))
