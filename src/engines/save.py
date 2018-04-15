from src.etc import constants
from src.terrain.generators import map_generator
from src.terrain.tile_types import *
from src.entities import entities

import json
import os
import gzip
import shutil
import random

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

        open(os.path.join(save_path, "maps.json"), "w").close()

        with gzip.open("src/saves/default_decs.json.gz", 'rb') as infile:
            decs_data = json.loads(infile.read().decode())

        with open(os.path.join(save_path, "decs.json"), 'w') as outfile:
            json.dump(decs_data, outfile)
            del decs_data

        shutil.copy("src/saves/default_entities.json", os.path.join(save_path, "entities.json"))

        map_generator.generate_map("src/resources/map.png", os.path.join(save_path, "maps.json"))

        with open(os.path.join(save_path, "entities.json"), "r") as infile:
            entity_data = json.load(infile)

        entity_data["new_save"] = True
        entity_data["position"] = constants.default_start

        with open(os.path.join(save_path, "meta.json"), "w") as outfile:
            json.dump(entity_data, outfile)

        gen_random_entities(save_path)

        os.remove(os.path.join(save_path, "decs.json"))
        os.remove(os.path.join(save_path, "entities.json"))

    def delete_save(self, name):

        if name not in self.get_saves():
            return

        save_path = os.path.join(self.save_dir, name)
        shutil.rmtree(save_path)

    def dump_to_save(self, name, save_data):

        save_path = os.path.join(self.save_dir, name)

        with open(os.path.join(save_path, "meta.json"), 'r') as infile:
            entity_data = json.load(infile)

        entity_data["entities"] = save_data["entities"]
        entity_data["player"] = save_data["player"]
        entity_data["position"] = save_data["position"]
        entity_data["player_meta"] = save_data["player_meta"]
        entity_data["story_data"] = save_data["story_data"]

        with open(os.path.join(save_path, "meta.json"), 'w') as outfile:
            json.dump(entity_data, outfile)


def gen_random_entities(save_path):

    with open(os.path.join(save_path, "maps.json"), "r") as infile:
        map_data = json.load(infile)

    with open(os.path.join(save_path, "meta.json"), "r") as infile:
        entity_data = json.load(infile)

    entity_id = 500

    for chunk in map_data.keys():
        if chunk not in entity_data["entities"]:
            entity_data["entities"][chunk] = []

        if chunk not in constants.no_spawn_chunks:
            for n in range(random.choice(constants.entity_selection_matrix)):
                entity_x = random.randint(0, 19)
                entity_y = random.randint(0, 14)

                attempts = 0
                valid = [False, False]

                while not all(valid):

                    valid = [False, False]

                    entity_x = random.randint(0, 19)
                    entity_y = random.randint(0, 14)
                    tile_no = (entity_y*20)+entity_x

                    if not any([[entity_x, entity_y] == x["pos"] for x in entity_data["entities"][chunk]]):
                        valid[0] = True

                    if map_data[chunk]["tiles"][tile_no * 4:tile_no * 4 + 4] in spawn_tiles:
                        valid[1] = True

                    attempts += 1
                    if attempts > 10:
                        break

                if attempts < 10:
                    entity_data["entities"][chunk].append(
                        entities.create_random_entity([entity_x, entity_y], entity_id)
                    )
                    entity_id += 1

        for n in range(random.choice(([0, 1, 1, 1, 2, 2]))):
            item_x = random.randint(0, 19)
            item_y = random.randint(0, 14)

            attempts = 0

            valid = [False, False]

            while not all(valid):

                valid = [False, False]

                item_x = random.randint(0, 19)
                item_y = random.randint(0, 14)

                tile_no = (item_y*20)+item_x

                if not any([[item_x, item_y] == x["pos"] for x in entity_data["entities"][chunk]]):
                    valid[0] = True

                if map_data[chunk]["tiles"][tile_no*4:tile_no*4+4] in spawn_tiles:
                    valid[1] = True

                attempts += 1
                if attempts > 10:
                    break

            if attempts < 10:
                entity_data["entities"][chunk].append(entities.create_random_item([item_x, item_y]))

    with open(os.path.join(save_path, "meta.json"), "w") as outfile:
        json.dump(entity_data, outfile)


if __name__ == "__main__":

    save_engine = SaveEngine()
    print(save_engine.saves)
    save_engine.create_save("save1")
