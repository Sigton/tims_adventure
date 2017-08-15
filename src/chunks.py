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

        # Open the save file
        with open(os.path.join("saves", "maps.json"), "r") as infile:
            self.data = json.load(infile)
            infile.close()

        # Select the 9 chunks around the players current position
        self.current_chunk = self.get_current_chunk_id()
        chunks_to_create = self.get_surrounding_chunks(self.current_chunk)

        self.old_chunk = self.current_chunk

        for n in chunks_to_create:
            self.create_chunk(n)

    def update(self):

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
            for chunk in to_remove:
                self.delete_chunk(chunk)

            to_create = [chunk for chunk in surrounding_chunks if chunk not in self.live_chunks]
            for chunk in to_create:
                if "-" not in chunk:
                    self.create_chunk(chunk)

    def create_chunk(self, chunk):

        # Loads a chunk from the save data

        if chunk not in self.data:
            return

        self.map_seeds[chunk] = self.data[chunk]

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

    def get_surrounding_chunks(self, chunk):

        # Creates a 2D array of the 9
        # chunks surrounding the given chunk

        chunk_x = int(chunk[0:2])
        chunk_y = int(chunk[2:4])
        x_range = range(chunk_x - 1, chunk_x + 2)
        y_range = range(chunk_y - 1, chunk_y + 2)

        return sum([[self.create_id(x_range[x], y_range[y])
                     for x in range(3)] for y in range(3)], [])

    @staticmethod
    def create_id(x, y):

        x = str(x)
        while len(x) < 2:
            x = "0" + x
        y = str(y)
        while len(y) < 2:
            y = "0" + y

        return x + y
