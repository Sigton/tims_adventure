from src.etc import constants, story_data

"""
story_tracker.py

This file holds information about
the players current tasks and inventory
"""


class StoryTracker:

    def __init__(self):

        self.inventory = {}
        self.quests = {}

        self.quests_been_updated = False

    def load_from_save(self, save_data):

        self.inventory = save_data["inventory"]
        self.quests = save_data["quests"]

        if len(self.quests.keys()) > 0:
            self.set_quest_updated()

    def get_story_data(self):

        return {"inventory": self.inventory,
                "quests": self.quests}

    def add_item(self, item, amount):

        if item in self.inventory.keys():
            self.inventory[item][0] += amount
        else:
            self.inventory[item] = [amount, constants.item_display_names[item]]

    def can_use_item(self, item, amount):

        if item not in self.inventory.keys():
            self.add_item(item, 0)
            return False
        else:
            return amount > self.get_amount_of(item)

    def get_amount_of(self, item):

        return 0 if item not in self.inventory.keys() else self.inventory[item][0]

    def use_item(self, item, amount):

        self.inventory[item][0] -= amount

        if not self.get_amount_of(item):
            self.delete_item(item)

    def delete_item(self, item):

        del self.inventory[item]

    def add_quest(self, quest):

        if quest not in self.quests.keys():
            self.quests[quest] = story_data.quests[quest]
            self.set_quest_updated()

    def remove_quest(self, quest):

        if quest in self.quests.keys():
            del self.quests[quest]
            self.set_quest_updated()

    def follow_path(self, quest):

        for new_quest in story_data.quest_path[quest]:
            self.add_quest(new_quest)

        self.remove_quest(quest)

    def set_quest_updated(self):

        self.quests_been_updated = True

    def set_quests_seen(self):

        self.quests_been_updated = False

    def to_see_quests(self):

        return self.quests_been_updated
