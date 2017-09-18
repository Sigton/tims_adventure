import json
import operator
import os

import pygame

from src.etc import constants, containers
from src.terrain import tiles
from src.terrain.tile_types import *

"""
chunks.py

This file handles the terrain chunks.

Chunks are 20x15 tile areas on the map.
Each chunk has it's unique seed, which is
saved in the save file and assigned to a location.
"""


def create_id(x, y):

        x = str(x)
        while len(x) < 2:
            x = "0" + x
        y = str(y)
        while len(y) < 2:
            y = "0" + y

        return x + y

    
class ChunkController:

    player = None

    def __init__(self, start_x, start_y):

        # The key is a 4 digit string
        # to locate the chunk,
        # and then the value is data
        # about the chunk.
        self.map_seeds = containers.SeedDict([])
        self.map_tiles = {}
        self.chunk_pos = {}

        # All the chunks that
        # are currently being updated
        self.live_chunks = []

        self.world_offset_x = (-start_x)+24
        self.world_offset_y = -start_y

        self.direction = ""
        self.moving = 0
        self.movement_interval = (0, 0)

        self.animation_clock = 0

        self.global_animation_threshold = max(constants.animation_thresholds.items(), key=operator.itemgetter(1))[0]

        self.current_frames = {
            "0030": 0
        }

        self.px, self.py = constants.player_pos

        tiles.load_images()

        # Check if the file is empty
        if not os.stat(os.path.join("src", "saves", "maps.json")).st_size:
            # If the file is empty then
            # run the map generator
            from src.terrain import map_generator
            map_generator.generate_map("src/resources/map.png")
            del map_generator

        with open(os.path.join("src", "saves", "maps.json"), "r") as infile:
            data = json.load(infile)
            infile.close()

            for key in list(data.keys()):
                self.map_seeds.add(containers.Seed(key, data[key]["tiles"], data[key]["decs"], None))

            del data

        # Select the 9 chunks around the players current position
        self.current_chunk = self.get_current_chunk_id()
        chunks_to_create = self.get_surrounding_chunks(self.current_chunk)

        self.old_chunk = self.current_chunk

        for n in chunks_to_create:
            self.create_chunk(n)

    def update(self, direction):

        self.direction = direction

        if self.direction and self.moving == 0:

            # If we're at the edge then don't allow moving towards the edge
            if self.world_offset_x >= -24 and "L" in self.direction:
                self.direction = self.direction.replace("L", "")
            if self.world_offset_y >= 0 and "U" in self.direction:
                self.direction = self.direction.replace("U", "")

            if self.direction:
                # Make sure we don't walk over anything we shouldn't.
                current_pos = self.get_player_tile_nums()
                if len(self.direction) == 1:
                    final_pos = list(map(operator.sub, current_pos,
                                         ([n // 48 for n in constants.dir_to_movements[self.direction]])))
                else:

                    final_pos = list(map(operator.sub, current_pos,
                                         ([n // 48 for n in list(map(operator.add,
                                                                     constants.dir_to_movements[self.direction[0]],
                                                                     constants.dir_to_movements[self.direction[1]]))])
                                         ))

                c_o = [0, 0]

                if final_pos[0] > 19:
                    c_o = [1, 0]
                    final_pos[0] %= 20
                elif final_pos[0] < 0:
                    c_o = [-1, 0]
                    final_pos[0] %= 20

                if final_pos[1] > 14:
                    c_o = [0, 1]
                    final_pos[1] %= 15
                elif final_pos[1] < 0:
                    c_o = [0, -1]
                    final_pos[1] %= 15

                current_chunk = self.get_current_chunk_id()
                final_chunk_list = list(map(operator.add, [int(current_chunk[0:2]), int(current_chunk[2:4])], c_o))
                final_chunk = create_id(final_chunk_list[0], final_chunk_list[1])

                index = final_pos[1]*20+final_pos[0]

                n = self.map_seeds[final_chunk].tiles
                target_tile = [n[i:i+4] for i in range(0, len(n), 4)][index]
                if target_tile in solid_tiles:
                    self.direction = self.direction.replace(self.direction, "")

            if self.direction:

                self.moving = constants.movement_speed

                if len(self.direction) > 1:
                    movements = [constants.dir_to_movements[d] for d in list(self.direction)]
                    movement = tuple(map(operator.add, movements[0], movements[1]))
                else:
                    movement = constants.dir_to_movements[self.direction]
                self.movement_interval = tuple(map(operator.floordiv, movement,
                                                   [self.moving for x in range(len(movement))]))

                self.player.move_history = [direction] + self.player.move_history[:4]
                self.player.create_movement_intervals()

        self.player.update(self.direction)
        self.update_chunks()

        self.animation_clock = (self.animation_clock + 1) %\
            constants.animation_thresholds[self.global_animation_threshold]
        for tile in self.current_frames.keys():
            if self.animation_clock % constants.animation_thresholds[tile] == 0:
                self.current_frames[tile] += 1

        if self.moving > 0:
            self.moving -= 1
            self.move_chunks(self.movement_interval)

        # Look for any new chunks that need to be
        # created and old ones that need removed

        self.current_chunk = self.get_current_chunk_id()

        if self.current_chunk != self.old_chunk:
            self.old_chunk = self.current_chunk

            # Player has moved chunk
            # We now removed chunks that are too far away
            # And generate new ones

            surrounding_chunks = self.get_surrounding_chunks(self.current_chunk)

            to_remove = [chunk for chunk in self.live_chunks if chunk not in surrounding_chunks]

            to_create = [chunk for chunk in surrounding_chunks if chunk not in self.live_chunks]

            for chunk in to_create:
                if "-" not in chunk and chunk in self.map_seeds:
                    # if len(to_remove):
                    #    self.reuse_chunk(to_remove.pop(), chunk)
                    # else:
                    self.create_chunk(chunk)

            # Delete any left over chunks
            for chunk in to_remove:
                self.delete_chunk(chunk)

    def update_chunks(self):

        for chunk in self.live_chunks:

            [tile.animate(self.current_frames[tile.tile_code]) for tile in self.map_tiles[chunk].tiles
             if tile.tile_code in animated_tiles]

    def create_chunk(self, chunk):

        # Creates a group of tile objects
        # from the seed of the given chunk

        seed = self.map_seeds[chunk].tiles
        new_chunk = containers.Chunk(chunk, [], [])

        # Split the string into each individual tile
        tile_data = [seed[i:i+4] for i in range(0, len(seed), 4)]
        x, y = 0, 0
        for n in tile_data:

            # Create instances of the tiles
            tile = int(n)
            if n in animated_tiles:
                new_chunk.add_tile(tiles.AnimatedTile(tile, x, y, x, y, n))
            else:
                new_chunk.add_tile(tiles.Tile(tile, x, y, x, y, n))

            x += 1
            if x % constants.chunk_w == 0:
                x = 0
                y += 1

        # Add them to the dict of tiles
        self.map_tiles[chunk] = new_chunk

        chunk_x = int(chunk[0:2]) * constants.chunk_w * constants.tile_w
        chunk_y = int(chunk[2:4]) * constants.chunk_h * constants.tile_h

        self.chunk_pos[chunk] = (chunk_x, chunk_y)

        self.live_chunks.append(chunk)

        self.assign_chunk_pos(chunk, (self.world_offset_x, self.world_offset_y))

    def reuse_chunk(self, old_chunk, new_chunk):

        print(old_chunk, new_chunk)

        # Re-purposes the existing tiles of a chunk
        # to form a new chunk.

        self.live_chunks.remove(old_chunk)
        del self.chunk_pos[old_chunk]

        seed = self.map_seeds[new_chunk].tiles

        tile_data = [seed[i:i+4] for i in range(0, len(seed), 4)]
        tile, x, y = 0, 0, 0
        for n in self.map_tiles[old_chunk].tiles:

            n.reuse(int(tile_data[tile]), x, y, x, y, tile_data[tile], self.map_tiles[old_chunk])

            x += 1
            if x % constants.chunk_w == 0:
                x = 0
                y += 1
            tile += 1
        print(len(self.map_tiles[old_chunk].tiles) if new_chunk == "0301" else "")
        self.map_tiles[new_chunk] = self.map_tiles.pop(old_chunk)

        chunk_x = int(new_chunk[0:2]) * constants.chunk_w * constants.tile_w
        chunk_y = int(new_chunk[2:4]) * constants.chunk_h * constants.tile_h

        self.chunk_pos[new_chunk] = (chunk_x, chunk_y)

        self.live_chunks.append(new_chunk)

        self.assign_chunk_pos(new_chunk, (self.world_offset_x, self.world_offset_y))

    def delete_chunk(self, chunk):

        # Removes a chunk that
        # is not currently in use

        if chunk not in self.live_chunks:
            # Make sure the chunk is currently in use
            return

        self.live_chunks.remove(chunk)
        del self.map_tiles[chunk]
        del self.chunk_pos[chunk]

    def draw(self, display):

        # Takes a group of tile sprites
        # and draws them to the display

        for chunk in self.live_chunks:
            chunk_to_draw = self.map_tiles[chunk]
            chunk_to_draw.draw(display)

    def assign_chunk_pos(self, chunk, movement):

        # Moves a single chunk
        self.chunk_pos[chunk] = (self.chunk_pos[chunk][0]+movement[0],
                                 self.chunk_pos[chunk][1]+movement[1])

        [x.realign(self.chunk_pos[chunk][0],
                   self.chunk_pos[chunk][1]) for x in self.map_tiles[chunk].tiles]

    def move_chunks(self, movement):

        # Moves all of the live chunks
        # by a certain amount.
        self.world_offset_x += movement[0]
        self.world_offset_y += movement[1]

        for chunk in self.live_chunks:
            self.chunk_pos[chunk] = (self.chunk_pos[chunk][0]+movement[0],
                                     self.chunk_pos[chunk][1]+movement[1])

            [x.realign(self.chunk_pos[chunk][0],
                       self.chunk_pos[chunk][1]) for x in self.map_tiles[chunk].tiles]

    def get_current_chunk_id(self):

        return create_id((abs(self.world_offset_x-480))//960,
                         (abs(self.world_offset_y-360))//720)

    def get_surrounding_chunks(self, chunk):

        # Creates a 2D array of the 9
        # chunks surrounding the given chunk

        chunk_x = int(chunk[0:2])
        chunk_y = int(chunk[2:4])
        x_range = range(chunk_x - 1, chunk_x + 2)
        y_range = range(chunk_y - 1, chunk_y + 2)

        return sum([[create_id(x_range[x], y_range[y])
                     for x in range(3)] for y in range(3)], [])

    def get_player_tile_nums(self):

        if self.world_offset_x % 960 > 456:
            tile_x = ((self.px - 4) + (abs(self.world_offset_x) % 960))//48
        else:
            tile_x = ((self.px - 4) - (self.world_offset_x % 960)) // 48

        if self.world_offset_y % 720 > 336:
            tile_y = ((self.py - 4) + (abs(self.world_offset_y) % 720))//48
        else:
            tile_y = ((self.py - 4) - (self.world_offset_y % 720)) // 48

        return [tile_x, tile_y]
