import pygame
from pygame.locals import *

from src.duel import duel_players

"""
dialogue.py

Handles interactions between characters.
"""


class DialogueController:

    def __init__(self, master):

        self.master = master

        self.scenes = {

        }

        self.player = None
        self.other_bean = None

    def start_scene(self, entity1, entity2, scene, exit_func, after_controller):

        self.player = duel_players.DuelPlayer(entity1, "R")
        self.other_bean = duel_players.DuelPlayer(entity2, "L")

    def update(self):

        for event in pygame.event.get():

            if event.type == QUIT:
                self.master.game_exit = True

    def draw(self, display):

        display.blit(self.player.image, (50, 400))
        display.blit(self.other_bean.image, (500, 50))
