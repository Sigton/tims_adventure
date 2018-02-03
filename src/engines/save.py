from src.etc import constants
from src.terrain.generators import map_generator

import json
import os
import gzip
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

    def refresh(self):

        self.saves = self.get_saves()

    def get_saves(self):

        save_dir_contents = os.listdir(self.save_dir)

        for save in save_dir_contents:

            valid = False
            if "meta.json" in os.listdir(os.path.join(self.save_dir, save)):
                valid = True

            if not valid:
                save_dir_contents.remove(save)

        return save_dir_contents

    def create_save(self, name):

        if name in self.get_saves():
            return

        save_path = os.path.join(self.save_dir, name)
        os.mkdir(save_path)

        open(os.path.join(save_path, "meta.json"), "w").close()
        open(os.path.join(save_path, "maps.json"), "w").close()

        with gzip.open("src/saves/default_decs.json.gz", 'rb') as infile:
            decs_data = json.loads(infile.read().decode())

        with open(os.path.join(save_path, "decs.json"), 'w') as outfile:
            json.dump(decs_data, outfile)
            del decs_data

        shutil.copy("src/saves/default_entities.json", os.path.join(save_path, "entities.json"))

        map_generator.generate_map("src/resources/map.png", os.path.join(save_path, "maps.json"))
        os.remove(os.path.join(save_path, "decs.json"))
        os.remove(os.path.join(save_path, "entities.json"))

    def delete_save(self, name):

        if name not in self.get_saves():
            return

        save_path = os.path.join(self.save_dir, name)
        shutil.rmtree(save_path)


if __name__ == "__main__":

    save_engine = SaveEngine()
    print(save_engine.saves)
    save_engine.create_save("save1")
