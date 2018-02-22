import pygame
from pygame.locals import *

"""
dialogue.py

Handles interactions between characters.
"""


class DialogueController:

    def __init__(self, master):

        self.master = master

        self.scenes = {

        }

    def start_scene(self, entity1, entity2, scene, exit_func, after_controller):

        pass

    def update(self):

        for event in pygame.event.get():

            if event.type == QUIT:
                self.master.game_exit = True

    def draw(self, display):

        pass
