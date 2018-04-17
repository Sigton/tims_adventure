import pygame
from pygame.locals import *

import json
import operator
import os
import random
import math
import collections

import src.terrain.tile_types
from src.etc import constants, containers, tools
from src.terrain import tiles
from src.hud import hud
from src.terrain.tile_types import *
from src.entities import entities, player


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

    def __init__(self, master):

        self.master = master

        self.player = None

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

        self.world_offset_x = 0
        self.world_offset_y = 0

        self.direction = ""
        self.moving = 0
        self.movement_interval = (0, 0)

        self.movement_speed = constants.movement_speed

        self.animation_clock = 0

        self.global_animation_threshold = max(constants.animation_thresholds.items(), key=operator.itemgetter(1))[0]

        self.current_frames = {
            "0030": 0,
            "0072": 0,
            "0073": 0
        }

        self.px, self.py = constants.player_pos

        self.current_chunk = self.get_current_chunk_id()
        self.old_chunk = self.current_chunk

        tiles.load_images()

        self.entities = {}
        self.assorted_entities = []

        self.hud = None

        self.hud_on = True

        self.bean_select_popup_open = False
        self.enemy_to_duel = None

        self.update_health_counter = 0

        self.other_bean_stat_count = -1
        self.other_bean_stat_panels = []

    def load_from_save(self, save_dir):

        with open(os.path.join(save_dir, "maps.json"), "r") as infile:
            map_data = json.load(infile)

        with open(os.path.join(save_dir, "meta.json"), "r") as infile:
            entity_data = json.load(infile)

        self.world_offset_x = entity_data["position"][0]
        self.world_offset_y = entity_data["position"][1]

        self.master.story_tracker.load_from_save(entity_data["story_data"])

        self.entities = {}

        for chunk in entity_data["entities"]:
            self.entities[chunk] = [entities.create_entity_from_json(entity)
                                    for entity in entity_data["entities"][chunk]]

        for key in list(map_data.keys()):
            self.map_seeds.add(containers.Seed(key, map_data[key]["tiles"], map_data[key]["decs"], None))

        self.player = player.Player(self, [entities.EntityMeta(None, bean) for bean in entity_data["player"]])
        self.player.set_chunk_controller(self)
        self.player.load_player(entity_data["player_meta"]["trail"], entity_data["player_meta"]["move_history"])

        self.hud = hud.HUD(self.player, self)

        self.hud.save_hud("main", ["backing", "health_display", "taskbar"])
        self.hud.load_saved_hud("main")

        del map_data
        del entity_data

        # Select the 9 chunks around the players current position
        self.current_chunk = self.get_current_chunk_id()
        chunks_to_create = self.get_surrounding_chunks(self.current_chunk)

        self.old_chunk = self.current_chunk

        for n in chunks_to_create:
            self.create_chunk(n)

        self.current_chunk = self.get_current_chunk_id()
        self.old_chunk = self.current_chunk

    def close_save(self):

        json_entities = {}
        for chunk in self.entities:
            json_entities[chunk] = []
            for entity in self.entities[chunk]:
                json_entities[chunk].append(entities.create_json_from_entity(entity))

        player_data = [player.create_json_from_player(bean) for bean in self.player.beans]

        return {
            "entities": json_entities,
            "player": player_data,
            "position": [self.world_offset_x, self.world_offset_y],
            "player_meta": {"trail": self.player.get_trail(), "move_history": self.player.move_history},
            "story_data": self.master.story_tracker.get_story_data()
        }

    def set_movement_speed(self, speed):

        self.movement_speed = speed

    def update(self):

        for event in pygame.event.get():
            if event.type == QUIT:

                self.master.close_save()

                self.master.game_exit = True

            elif self.bean_select_popup_open:

                self.hud.get_component("bean_select").handle_event(event)

            elif self.hud.has_component("healing_display"):
                self.hud.get_component("healing_display").handle_event(event)

            elif event.type == constants.MUSIC_START_EVENT:

                if not self.master.sound_engine.playing_sound("music"):
                    new_music = random.choice(self.master.sound_engine.music)
                    while new_music == self.master.last_song:
                        new_music = random.choice(self.master.sound_engine.music)
                    self.master.last_song = new_music

                    self.master.sound_engine.queue_sound((new_music, 0))

            elif event.type == KEYDOWN:

                if event.key in (K_UP, K_w):
                    self.direction = "U"

                elif event.key in (K_DOWN, K_s):
                    self.direction = "D"

                elif event.key in (K_LEFT, K_a):
                    self.direction = "L"

                elif event.key in (K_RIGHT, K_d):
                    self.direction = "R"

            elif event.type == KEYUP:

                if event.key == K_ESCAPE:

                    self.master.update_save()
                    self.master.close_save()

                    self.master.game_exit = True

                elif event.key in (K_UP, K_w):
                    self.direction = self.direction.replace("U", "")

                elif event.key in (K_DOWN, K_s):
                    self.direction = self.direction.replace("D", "")

                elif event.key in (K_LEFT, K_a):
                    self.direction = self.direction.replace("L", "")

                elif event.key in (K_RIGHT, K_d):
                    self.direction = self.direction.replace("R", "")

                elif event.key == K_SPACE:

                    chunk_entities = []
                    for chunk in self.live_chunks:
                        [chunk_entities.append(entity) for entity in self.map_tiles[chunk].get_entities()]

                    entity_range = {}
                    for entity in chunk_entities:
                        distance = math.sqrt(math.pow(self.player.beans[0].rect.centerx - entity.rect.centerx, 2)
                                             + math.pow(self.player.beans[0].rect.centery - entity.rect.centery, 2))

                        if distance < constants.interaction_distance \
                                and entity.__class__.__name__ not in constants.items:
                            entity_range[distance] = entity

                    ordered_ranges = collections.OrderedDict(sorted((entity_range.items())))

                    if len(ordered_ranges):
                        self.master.sound_engine.queue_sound(["click", 0])
                        self.enemy_to_duel = list(ordered_ranges.items())[0][1]

                        if self.enemy_to_duel.meta.interaction is not None:
                            exec(self.enemy_to_duel.meta.interaction)
                        else:
                            if not self.bean_select_popup_open:
                                self.bean_select_popup_open = True

                                self.hud.open_widget("bean_select")

                elif event.key == K_F11:
                    self.master.set_full_screen()

                elif event.key == K_ESCAPE:
                    self.master.exit_to_menu()

        if self.bean_select_popup_open:
            self.update_hud()
            return

        if self.direction and self.moving == 0:

            # If we're at the edge then don't allow moving towards the edge
            if self.world_offset_x >= -24 and "L" in self.direction:
                self.direction = self.direction.replace("L", "")
            if self.world_offset_y >= 0 and "U" in self.direction:
                self.direction = self.direction.replace("U", "")

            if self.direction:
                # Make sure we don't walk over anything we shouldn't.
                current_pos = self.get_player_tile_nums()
                final_pos = list(map(operator.sub, current_pos,
                                     ([n // 48 for n in constants.dir_to_movements[self.direction]])))

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

                self.moving = self.movement_speed

                movement = constants.dir_to_movements[self.direction]
                self.movement_interval = tuple(map(operator.floordiv, movement,
                                                   [self.moving for x in range(len(movement))]))

                self.player.move_history = [self.direction] + self.player.move_history[:4]
                self.player.create_movement_intervals()

                current_tile = self.get_current_tile()

                if current_tile in constants.footstep_types:

                    [self.master.sound_engine.stop_sound(sound)
                     for sound in [s for s in constants.footstep_sounds if s != constants.footstep_types[current_tile]]]
                    if not self.master.sound_engine.playing_sound(constants.footstep_types[current_tile]):
                        self.master.sound_engine.queue_sound((constants.footstep_types[current_tile], 0))

                else:
                    [self.master.sound_engine.stop_sound(sound)
                     for sound in [s for s in constants.footstep_sounds if s != "footstep"]]
                    if not self.master.sound_engine.playing_sound("footstep"):
                        self.master.sound_engine.queue_sound(("footstep", 0))

        self.player.update(self.direction)
        self.update_chunks()

        [entity.update() for entity in self.assorted_entities]

        if self.moving > 0:
            self.moving -= 1
            self.move_chunks(self.movement_interval)
        else:
            [self.master.sound_engine.stop_sound(sound) for sound in constants.footstep_sounds]

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
                    self.create_chunk(chunk)

            # Delete any left over chunks
            for chunk in to_remove:
                self.delete_chunk(chunk)

        if not self.moving:
            for chunk in self.live_chunks:
                for entity in self.map_tiles[chunk].get_entities():
                    if entity.__class__.__name__ not in constants.items:

                        if entity.meta.to_delete and entity.meta.id not in constants.entity_delete_exceptions:
                            self.remove_stat_panel(entity)
                            self.master.particle_engine.create_particle_spread(
                                'smoke', 12, entity.rect.centerx, entity.rect.centery, 35, 10, 0, 50, 10
                            )
                            self.map_tiles[chunk].remove_entity(entity)
                        else:
                            distance = math.sqrt(math.pow(self.player.beans[0].rect.centerx - entity.rect.centerx, 2)
                                                 + math.pow(self.player.beans[0].rect.centery - entity.rect.centery, 2))

                            if distance < constants.interaction_distance:
                                if not (entity.meta.interaction == "pass" or entity.meta.important):
                                    entity.interaction_icon.on()

                                if not entity.stat_panel_active:
                                    self.other_bean_stat_count += 1
                                    entity.stat_panel_on(self.other_bean_stat_count, 0, 0)
                                    self.other_bean_stat_panels.append(entity.stat_panel)
                                    self.hud.get_component("backing").resize(self.other_bean_stat_count+1)
                            else:
                                if not (entity.meta.interaction == "pass" or entity.meta.important):
                                    entity.interaction_icon.off()

                                if entity.stat_panel_active:
                                    self.other_bean_stat_count -= 1
                                    self.other_bean_stat_panels.remove(entity.stat_panel)
                                    entity.stat_panel_off()

                                    if self.other_bean_stat_count > -1:
                                        n = 0
                                        for panel in self.other_bean_stat_panels:
                                            panel.move(5, (65*n)+275)
                                            n += 1
                                    self.hud.get_component("backing").resize(self.other_bean_stat_count + 1)

                            if entity.particle_timer == 0:
                                self.master.particle_engine.create_particle_spread(
                                    'smoke', 12, entity.rect.centerx, entity.rect.centery, 35, 10, 0, 50, 10
                                )

                    elif entity.pickup:
                        self.master.story_tracker.add_item(entity.__class__.__name__, 1)
                        self.map_tiles[chunk].remove_entity(entity)
                        self.master.sound_engine.queue_sound(("pickup", 0))

        self.animation_clock = (self.animation_clock + 1) % \
            constants.animation_thresholds[self.global_animation_threshold]
        for tile in self.current_frames.keys():
            if self.animation_clock % constants.animation_thresholds[tile] == 0:
                self.current_frames[tile] += 1

        self.update_hud()

    def start_duel(self, bean):
        self.master.duel_controller.begin_duel(self.player.beans[bean], self.enemy_to_duel)

        self.master.switch_to(1)

        self.enemy_to_duel = None

        self.bean_select_popup_open = False
        self.hud.close_widget("bean_select")

    def update_hud(self):

        if self.hud_on:
            self.hud.update()

        if self.update_health_counter % constants.health_update_rate == 0:
            for bean in self.player.beans:
                if bean.meta.hp < bean.meta.max_hp:
                    bean.meta.heal(1)
            self.update_health_counter = 0
            for chunk in self.live_chunks:
                for entity in self.map_tiles[chunk].get_entities():
                    if entity.__class__.__name__ not in constants.items:
                        if entity.meta.hp < entity.meta.max_hp:
                            entity.meta.heal(1)
        self.update_health_counter += 1

    def update_chunks(self):

        for chunk in self.live_chunks:

            [tile.animate(self.current_frames[tile.tile_code]) for tile in self.map_tiles[chunk].tiles
             if tile.tile_code in animated_tiles]

            [entity.update() for entity in self.map_tiles[chunk].entities]

    def create_chunk(self, chunk):

        # Creates a group of tile objects
        # from the seed of the given chunk

        tile_seed = self.map_seeds[chunk].tiles
        new_chunk = containers.Chunk(chunk, [], [], self.entities[chunk] if chunk in self.entities.keys() else [])

        # Split the string into each individual tile
        tile_data = [tile_seed[i:i+4] for i in range(0, len(tile_seed), 4)]
        x, y = 0, 0
        for n in tile_data:

            # Create instances of the tiles
            tile = int(n)
            if n in animated_tiles:
                new_chunk.add_tile(tiles.AnimatedTile(tile, x, y, n, True))
            else:
                new_chunk.add_tile(tiles.Tile(tile, x, y, n, True))

            x += 1
            if x % constants.chunk_w == 0:
                x = 0
                y += 1

        decs_seed = self.map_seeds[chunk].decs

        for dec in decs_seed:

            position = dec["pos"]
            tile = dec["tileid"]

            if len(position) == 4:
                x, y = int(position[0:2]), int(position[2:4])
                to_grid = True
            else:
                x, y = int(position[0:3]), int(position[3:6]),
                to_grid = False

            if tile in animated_tiles:
                new_chunk.add_dec(tiles.AnimatedTile(int(tile), x, y, tile, to_grid))
            else:
                new_chunk.add_dec(tiles.Tile(int(tile), x, y, tile, to_grid))

        # Add them to the dict of tiles
        self.map_tiles[chunk] = new_chunk

        chunk_x = int(chunk[0:2]) * constants.chunk_w * constants.tile_w
        chunk_y = int(chunk[2:4]) * constants.chunk_h * constants.tile_h

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

        layered_render = []

        for chunk in self.live_chunks:
            chunk_to_draw = self.map_tiles[chunk]
            chunk_to_draw.draw(display)

            for dec in chunk_to_draw.get_decs():
                if dec.tile_code in src.terrain.tile_types.no_layer_decs:
                    dec.draw(display)
                else:
                    layered_render.append(dec)

            [layered_render.append(entity) for entity in chunk_to_draw.get_entities()]

        [layered_render.append(bean) for bean in self.player.beans]

        for dec in sorted(layered_render, key=lambda x: x.shadow.rect.bottom if x.has_shadow else x.rect.bottom):
            if dec.__class__.__name__ not in constants.no_fade_sprites:
                if dec.tile_code not in no_fade_decs:
                    if any([dec.rect.colliderect(bean.rect) for bean in self.player.beans]):
                            if dec.has_shadow:
                                dec.shadow.draw(display)
                            tools.blit_alpha(display, dec.image, dec.rect.topleft, 180)
                    else:
                        dec.draw(display)
                else:
                    dec.draw(display)
            else:
                dec.draw(display)

        [entity.draw(display) for entity in self.assorted_entities]

        self.master.particle_engine.draw(display)

        if self.hud_on:
            self.hud.draw(display)
            if self.hud.get_component("backing").hud_open:
                [panel.draw(display) for panel in self.other_bean_stat_panels]

    def assign_chunk_pos(self, chunk, movement):

        # Moves a single chunk
        self.chunk_pos[chunk] = (self.chunk_pos[chunk][0]+movement[0],
                                 self.chunk_pos[chunk][1]+movement[1])

        [x.realign(self.chunk_pos[chunk][0],
                   self.chunk_pos[chunk][1]) for x in self.map_tiles[chunk].tiles]

        [x.realign(self.chunk_pos[chunk][0],
                   self.chunk_pos[chunk][1]) for x in self.map_tiles[chunk].decs]

        [x.realign(self.chunk_pos[chunk][0],
                   self.chunk_pos[chunk][1]) for x in self.map_tiles[chunk].entities]

    def move_chunks(self, movement):

        # Moves all of the live chunks
        # by a certain amount.
        self.world_offset_x += movement[0]
        self.world_offset_y += movement[1]

        for chunk in self.live_chunks:
            self.assign_chunk_pos(chunk, movement)

        self.master.particle_engine.realign(movement[0], movement[1])

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

    def get_current_tile(self):

        pos = self.get_player_tile_nums()
        tile_no = (pos[1]*20)+pos[0]
        current_tile = self.map_seeds[self.get_current_chunk_id()].tiles[tile_no*4:tile_no*4+4]

        return current_tile

    def locate_entity(self, entity_id):

        for chunk in self.entities:
            for entity in self.entities[chunk]:
                if entity.__class__.__name__ not in constants.items:
                    if entity.meta.id == entity_id:
                        return entity

    def delete_entity(self, entity_id):

        for chunk in self.entities:
            for entity in self.entities[chunk]:
                if entity.__class__.__name__ not in constants.items:
                    if entity.meta.id == entity_id:
                        self.entities[chunk].remove(entity)

    def remove_stat_panel(self, entity):

        if entity.stat_panel not in self.other_bean_stat_panels:
            return

        self.other_bean_stat_count -= 1
        self.other_bean_stat_panels.remove(entity.stat_panel)
        entity.stat_panel_off()

        if self.other_bean_stat_count > -1:
            n = 0
            for panel in self.other_bean_stat_panels:
                panel.move(5, (65 * n) + 275)
                n += 1
        self.hud.get_component("backing").resize(self.other_bean_stat_count + 1)

    def stop_moving(self):

        self.direction = ""
