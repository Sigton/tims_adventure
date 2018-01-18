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

        save_dir_contents = os.listdir(self.save_dir)

        for file in save_dir_contents:

            valid = False
            if "." in file:
                if file.split(".")[1] == "meta":
                    valid = True

            if not valid:
                save_dir_contents.remove(file)

        return save_dir_contents

if __name__ == "__main__":

    save_engine = SaveEngine()
    print(save_engine.saves)
