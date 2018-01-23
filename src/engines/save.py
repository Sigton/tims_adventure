from src.etc import constants
from src.terrain.generators import map_generator

import json
import os
import shutil

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

        for save in save_dir_contents:

            valid = False
            for file in os.listdir(os.path.join(self.save_dir, save)):
                if "." in file:
                    if file.split(".")[1] == "meta":
                        valid = True

            if not valid:
                save_dir_contents.remove(save)

        return save_dir_contents

    def create_save(self, name):

        if name in self.get_saves():
            return

        save_path = os.path.join(self.save_dir, name)
        os.mkdir(save_path)

        open(os.path.join(save_path, name+".meta"), "w").close()
        open(os.path.join(save_path, "progress.json"), "w").close()
        open(os.path.join(save_path, "maps.json"), "w").close()
        shutil.copy("src/saves/default_decs.json", os.path.join(save_path, "decs.json"))

        map_generator.generate_map("src/resources/map.png", os.path.join(save_path, "maps.json"))


if __name__ == "__main__":

    save_engine = SaveEngine()
    print(save_engine.saves)
    save_engine.create_save("save2")
