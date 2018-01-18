from src.etc import constants

import json
import os

"""
save.py

This is the game save engine
that will keep your progress safe
"""


class SaveEngine:

    def __init__(self):

        self.save_dir = constants.DEFAULT_SAVE_DIRECTORY

        self.saves = self.get_saves()

    def get_saves(self):

        return os.listdir(self.save_dir)
