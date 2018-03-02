"""
story_tracker.py

This file holds information about
the players current tasks and inventory
"""


class StoryTracker:

    def __init__(self):

        self.inventory = {}
        self.quests = {}

    def load_from_save(self, save_data):

        self.inventory = save_data["inventory"]
        self.quests = save_data["inventory"]

    def get_story_data(self):

        return {"inventory": self.inventory,
                "quests": self.quests}