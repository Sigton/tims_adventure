import pygame

from src.etc import constants
from src.entities import bean_image_loader, icons, shadows
from src.entities.entity_meta import entity_data
from src.hud import hud_widgets

import random
import math

"""
entities.py

This file holds the classes for on screen entities,
and metadata about entities
"""


class EntityMeta:

    def __init__(self, parent=None, json_data=None):

        if parent is not None:
            self.parent = parent

            self.bean = self.parent.bean

            self.max_hp = entity_data[self.bean]["max_hp"]
            self.hp = self.max_hp

            self.level = 1
            self.xp = 0

            self.energy = entity_data[self.bean]["energy"]

            self.moves = entity_data[self.bean]["moves"]
            self.attack = entity_data[self.bean]["attack"]

            self.images = self.parent.images

            self.interaction = None
            self.important = False

            self.evil = True

            self.display_name = entity_data[self.bean]["display_name"]
        else:
            self.bean = json_data["bean"]

            self.max_hp = json_data["max_hp"]
            self.hp = json_data["hp"]

            self.level = json_data["level"]
            self.xp = json_data["xp"]

            self.energy = json_data["energy"]

            self.moves = json_data["moves"]
            self.attack = json_data["attack"]

            self.interaction = json_data["interaction"]
            self.important = json_data["important"]

            self.evil = json_data["evil"]

            self.display_name = json_data["display_name"]

    def damage(self, amount):

        self.hp -= amount

        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):

        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def xp_gain(self, amount):

        self.xp += amount

        if self.xp > self.get_level_up_threshold():
            self.xp %= self.get_level_up_threshold()
            self.level_up(1)

    def level_up(self, levels):

        self.level += levels

    def get_level_up_threshold(self):

        return int(constants.level_up_base * (constants.level_up_multiplier ** self.level))


class RandomBean:

    def __init__(self, x, y, to_grid, bean, meta=None):

        self.bean = bean

        self.images = bean_image_loader.beans[self.bean]

        self.facing = random.choice(["R", "L"])

        self.image = self.images[self.facing]

        self.rect = self.image.get_rect()
        if to_grid:
            self.rect.x = x * constants.tile_w
            self.rect.y = y * constants.tile_h
        else:
            self.rect.x = x
            self.rect.y = y

        self.offset_x = self.rect.x
        self.offset_y = self.rect.y

        if self.bean in constants.bean_image_offset.keys():
            self.image_offset_x, self.image_offset_y = constants.bean_image_offset[self.bean]
        else:
            self.image_offset_x, self.image_offset_y = (0, 0)

        if meta is not None:
            self.meta = meta
            self.meta.parent = self
            self.meta.images = self.images
        else:
            self.meta = EntityMeta(self)
        self.shadow = shadows.Shadow(self)

        if not self.meta.important:
            self.interaction_icon = icons.PressSpace(self.rect.centerx, self.rect.y - 35)
            self.interaction_icon.off()
        else:
            self.interaction_icon = icons.ImportantPressSpace(self.rect.centerx, self.rect.y - 35)
            self.interaction_icon.on()

        self.stat_panel = None
        self.stat_panel_active = False

        if self.meta.evil:
            self.image = self.images["G" + self.facing]
        else:
            self.image = self.images[self.facing]

    def create_images(self, main_img):

        self.images.clear()

        self.images["R"] = main_img
        self.images["L"] = pygame.transform.flip(main_img, True, False)

    def update_image(self):

        if self.meta.evil:
            self.image = self.images["GR"]
        else:
            self.image = self.images["R"]

    def realign(self, x, y):

        self.rect.x = x + self.offset_x
        self.rect.y = y + self.offset_y

        if self.interaction_icon is not None:
            self.interaction_icon.realign(x, y)

        self.shadow.update()

    def update(self):

        if self.interaction_icon is not None:
            self.interaction_icon.update()

        if self.stat_panel is not None:
            self.stat_panel.update()

    def draw(self, display):

        self.shadow.draw(display)

        display.blit(self.image, (self.rect.x-self.image_offset_x, self.rect.y-self.image_offset_y))

        if self.interaction_icon is not None:
            self.interaction_icon.draw(display)

    def stat_panel_on(self, panel_id, x, y):

        self.stat_panel = hud_widgets.EnemyStat(self, x+5, y+(65*panel_id)+275)
        self.stat_panel_active = True

    def stat_panel_off(self):

        self.stat_panel = None
        self.stat_panel_active = False


class Item(icons.Icon):

    def __init__(self, image, x, y):

        icons.Icon.__init__(self, image, x*constants.tile_w, y*constants.tile_h)

        self.shadow = shadows.Shadow(self)
        self.has_shadow = True

        self.pickup = False

    def update(self):

        dist = math.sqrt(math.pow((constants.DISPLAY_CENTER[0]-self.rect.centerx), 2) +
                         math.pow((constants.DISPLAY_CENTER[1]-self.rect.centery), 2))
        if dist < 30:
            self.pickup = True

    def realign(self, x, y):

        self.rect.x = x + self.offset_x
        self.rect.y = y + self.offset_y

        self.shadow.update()

    def draw(self, display):

        self.shadow.draw(display)

        display.blit(self.image, self.rect.topleft)


class EnlightenmentPotion(Item):

    def __init__(self, x, y):

        Item.__init__(self, icons.sprite_sheet.get_image(54, 0, 48, 48), x, y)


class HealthPotion(Item):

    def __init__(self, x, y):

        Item.__init__(self, icons.sprite_sheet.get_image(86, 0, 48, 48), x, y)


items = {
    "EnlightenmentPotion": EnlightenmentPotion,
    "HealthPotion": HealthPotion
}


def create_entity_from_json(entity_json):

    if "item" not in list(entity_json.keys()):
        meta = EntityMeta(None, entity_json["meta"])

        new_entity = RandomBean(entity_json["pos"][0], entity_json["pos"][1], True, meta.bean, meta)

        return new_entity
    else:
        return items[entity_json["item"]](entity_json["pos"][0], entity_json["pos"][1])


def create_json_from_entity(entity):

    if entity.__class__.__name__ not in constants.items:
        return {
            "pos": [entity.offset_x//constants.tile_w,
                    entity.offset_y//constants.tile_h],
            "meta": {
                "bean": entity.meta.bean,
                "max_hp": entity.meta.max_hp,
                "moves": entity.meta.moves,
                "attack": entity.meta.attack,
                "energy": entity.meta.energy,
                "hp": entity.meta.hp,
                "xp": entity.meta.xp,
                "level": entity.meta.level,
                "interaction": entity.meta.interaction,
                "important": entity.meta.important,
                "evil": entity.meta.evil,
                "display_name": entity.meta.display
            }
        }
    else:
        return {
            "pos": [entity.rect.x // constants.tile_w,
                    entity.rect.y // constants.tile_h],
            "item": entity.__class__.__name__
        }


def create_random_entity(pos):

    bean = random.choice(list(entity_data.keys()))

    return {
        "pos": pos,
        "meta": {
            "bean": bean,
            "max_hp": entity_data[bean]["max_hp"],
            "moves": entity_data[bean]["moves"],
            "attack": entity_data[bean]["attack"],
            "energy": entity_data[bean]["energy"],
            "hp": entity_data[bean]["max_hp"],
            "xp": 0,
            "level": 1,
            "interaction": None,
            "important": False,
            "evil": True,
            "display_name": entity_data[bean]["display_name"]
        }
    }


def create_random_item(pos):

    return {
        "pos": pos,
        "item": random.choice(list(items.keys()))
    }
