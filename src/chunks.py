import pygame
import json
import os

from src import constants, tiles

"""
chunks.py

This file handles the terrain chunks.

Chunks are 20x15 tile areas on the map.
Each chunk has it's unique seed, which is
saved in the save file and assigned to a location.
"""


class ChunkController:

    def __init__(self, start_x, start_y):

        # The key is a 4 digit string
        # to locate the chunk,
        # and then the value is data
        # about the chunk.
        self.map_seeds = {}
        self.map_tiles = {}
        self.chunk_pos = {}

        # All the chunks that
        # are currently being updated
        self.live_chunks = []

        self.world_offset_x = start_x+24
        self.world_offset_y = start_y+0

        # Select the 9 chunks around the players current position
        current_chunk = self.get_current_chunk_id()

        chunk_x = int(current_chunk[0:2])
        chunk_y = int(current_chunk[2:4])
        x_range = range(chunk_x-1, chunk_x+2)
        y_range = range(chunk_y-1, chunk_y+2)

        chunks_to_create = [[self.create_id(x_range[x], y_range[y])
                             for x in range(3)] for y in range(3)]

        for n in chunks_to_create:
            for m in n:
                self.create_chunk(m)

    def create_chunk(self, chunk):

        # Loads a chunk from the save data

        # Open the save file
        with open(os.path.join("saves", "maps.json"), "r") as infile:
            data = json.load(infile)
            infile.close()

        self.map_seeds[chunk] = data[chunk]

        # Creates a group of tile objects
        # from the seed of the given chunk

        seed = self.map_seeds[chunk]
        new_chunk = pygame.sprite.Group()

        # Split the string into each individual tile
        tile_data = [seed[i:i+2] for i in range(0, len(seed), 2)]
        x, y = 0, 0
        for n in tile_data:

            # Create instances of the tiles
            tile = tiles.tiles[int(n)]
            new_chunk.add(tiles.Tile(tile, x, y, x, y))

            x += 1
            if x % constants.chunk_w == 0:
                x = 0
                y += 1

        # Add them to the dict of tiles
        self.map_tiles[chunk] = new_chunk

        chunk_x = int(chunk[0:2])*constants.chunk_w*constants.tile_w
        chunk_y = int(chunk[2:4])*constants.chunk_h*constants.tile_h

        self.chunk_pos[chunk] = (chunk_x, chunk_y)

        self.live_chunks.append(chunk)

        self.assign_chunk_pos(chunk, (self.world_offset_x, self.world_offset_y))

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
                   self.chunk_pos[chunk][1]) for x in self.map_tiles[chunk].sprites()]

    def move_chunks(self, movement):

        # Moves all of the live chunks
        # by a certain amount.
        self.world_offset_x += movement[0]
        self.world_offset_y += movement[1]

        for chunk in self.live_chunks:
            self.chunk_pos[chunk] = (self.chunk_pos[chunk][0]+movement[0],
                                     self.chunk_pos[chunk][1]+movement[1])

            [x.realign(self.chunk_pos[chunk][0],
                       self.chunk_pos[chunk][1]) for x in self.map_tiles[chunk].sprites()]

    def get_current_chunk_id(self):

        return self.create_id((abs(self.world_offset_x-480))//960,
                              (abs(self.world_offset_y-360))//720)

    @staticmethod
    def create_id(x, y):

        x = str(x)
        while len(x) < 2:
            x = "0" + x
        y = str(y)
        while len(y) < 2:
            y = "0" + y

        return x + y
