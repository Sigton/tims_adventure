import math
import operator
import random

import pygame

from src.entities import shadows, bean_image_loader, entities
from src.etc import constants

"""
player.py

This is the player you see on screen.
"""


class Player(pygame.sprite.Sprite):

    chunk_controller = None

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.beans = [Bean(random.choice(list(bean_image_loader.beans.keys()))) for n in range(3)]

        self.trail = [[0, 0],
                      [-1, 0],
                      [-2, 0],
                      [-3, 0],
                      [-4, 0]]

        self.move_history = ["R", "R", "R", "R", "R"]
        self.movement_intervals = [(0, 0), (0, 0), (0, 0), (0, 0)]

        n = 0
        head_bean = self.beans[0]
        for bean in self.beans:
            bean.rect.centerx = head_bean.rect.centerx + 48 * self.trail[n][0]
            n += 1

        self.drawn = False

    def update(self, direction):

        [self.beans[n].set_image(self.move_history[n]) for n in range(len(self.beans))]

        if self.chunk_controller.moving:

            n = 0
            for bean in self.beans:
                if not self.beans.index(bean) == 0:
                    bean.rect.x += self.movement_intervals[n][0]
                    bean.rect.y += self.movement_intervals[n][1]
                    n += 1

        [bean.shadow.update() for bean in self.beans]

    def create_movement_intervals(self):

        for n in range(len(self.movement_intervals)):
            current_move = self.move_history[0]
            old_move = self.move_history[n+1]

            if len(current_move) > 1:
                new_movement = tuple(map(operator.add,
                                         constants.dir_to_movements[current_move[0]],
                                         constants.dir_to_movements[current_move[1]]))
            else:
                new_movement = constants.dir_to_movements[current_move]

            if len(old_move) > 1:
                old_movement = tuple(map(operator.add,
                                         constants.dir_to_movements[old_move[0]],
                                         constants.dir_to_movements[old_move[1]]))
            else:
                old_movement = constants.dir_to_movements[old_move]

            new_movement = tuple(map(operator.sub, (0, 0), new_movement))
            old_movement = tuple(map(operator.sub, (0, 0), old_movement))

            movement = tuple(map(operator.sub, old_movement, new_movement))
            self.movement_intervals[n] = tuple(map(operator.floordiv, movement,
                                                   [constants.movement_speed for x in range(len(movement))]))

    def set_chunk_controller(self, ref):

        self.chunk_controller = ref
        for bean in self.beans:
            bean.chunk_controller = ref

    def draw(self, display):

        [bean.draw(display) for bean in self.beans]


class Bean(pygame.sprite.Sprite):

    def __init__(self, bean):

        pygame.sprite.Sprite.__init__(self)
        self.chunk_controller = None

        self.bean = bean

        self.images = {}

        self.create_images(bean_image_loader.beans[self.bean]())

        self.image = self.images["R"]

        self.rect = self.image.get_rect()
        self.rect.center = constants.DISPLAY_CENTER

        self.meta = entities.EntityMeta(self)

        self.shadow = shadows.Shadow(self)

    def set_image(self, direction):

        if direction == "R":
            self.image = self.images["R"]
        elif direction == "L":
            self.image = self.images["L"]

    def create_images(self, main_image):

        self.images.clear()

        self.images["R"] = main_image
        self.images["L"] = pygame.transform.flip(main_image, True, False)

    def draw(self, display):

        self.shadow.draw(display)

        wobble_x = math.cos((((self.chunk_controller.world_offset_y + (self.rect.x % 13)) % 48) + 180) * 2) * 4
        wobble_y = math.sin(((self.chunk_controller.world_offset_x - 24 + (self.rect.x % 13)) % 48) * 2) * 4
        display.blit(self.image,
                     (self.rect.x + wobble_x,
                      self.rect.y + wobble_y))
