import pygame
from pygame.locals import *

from src.duel import duel_players
from src.etc import gui_components, constants

"""
dialogue.py

Handles interactions between characters.
"""


class DialogueController:

    def __init__(self, master):

        self.master = master

        self.scenes = {
            "test_scene": [
                            ("Wow I can speak!", 0),
                            ("Ayy me too!", 1),
                            ("That crazy man...", 0),
                            ("Sure is bruh", 1)
                          ]
        }

        self.background = pygame.image.load("src/resources/dialogue_background.png").convert()

        self.player = None
        self.other_bean = None

        self.text_box_background = gui_components.Fill(0, 0, 350, 262, constants.GUI_BACKING)
        self.text_box_fill = gui_components.Fill(5, 5, 340, 252, constants.GUI_FILL)

        self.components = [
            self.text_box_background,
            self.text_box_fill
        ]

        self.current_scene = []

    def start_scene(self, entity1, entity2, scene, exit_func, after_controller):

        self.player = duel_players.DuelPlayer(entity1, "R")
        self.other_bean = duel_players.DuelPlayer(entity2, "L")

        self.current_scene = self.scenes[scene]

    def update(self):

        for event in pygame.event.get():

            if event.type == QUIT:
                self.master.game_exit = True

    def draw(self, display):

        display.blit(self.background, (0, 0))

        self.player.shadow.draw(display)
        self.other_bean.shadow.draw(display)

        display.blit(self.player.image, (75, 368))
        display.blit(self.other_bean.image, (640, 53))

        [component.draw(display) for component in self.components]
