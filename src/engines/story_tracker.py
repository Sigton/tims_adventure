from src.etc import constants, story_data

"""
story_tracker.py

This file holds information about
the players current tasks and inventory
"""


class StoryTracker:

    def __init__(self, master):

        self.master = master

        self.inventory = {}
        self.quests = {}
        self.quests_completed = {}
        self.completed_quests = {}
        self.objective_progress = {}

        self.quests_been_updated = False

        self.quest_updates = {
            "learn_fight": self.update_old_man,
            "liberate_village": self.update_dan,
            "defend_wizard": self.update_wizard
        }

    def load_from_save(self, save_data):

        self.inventory = save_data["inventory"]
        self.quests = save_data["quests"]
        self.quests_completed = save_data["quests_completed"]
        self.completed_quests = save_data["completed_quests"]
        self.objective_progress = save_data["objective_progress"]

        if len(self.quests.keys()) > 0:
            self.set_quest_updated()

    def get_story_data(self):

        return {"inventory": self.inventory,
                "quests": self.quests,
                "quests_completed": self.quests_completed,
                "completed_quests": self.completed_quests,
                "objective_progress": self.objective_progress}

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

            if type(story_data.completion_criteria[quest]) is tuple:
                new_quest = {}
                for criteria in story_data.completion_criteria[quest]:
                    new_quest[criteria] = False

                self.objective_progress[quest] = new_quest

            self.quests[quest] = story_data.quests[quest]
            self.set_quest_updated()

    def remove_quest(self, quest):

        if quest in self.quests.keys():

            # if quest in self.objective_progress:
            #     del self.objective_progress[quest]

            del self.quests[quest]
            self.set_quest_updated()

    def follow_path(self, quest):

        for new_quest in story_data.quest_path[quest]:
            self.add_quest(new_quest)

        self.mark_completed(quest)

    def set_quest_updated(self):

        self.quests_been_updated = True

    def set_quests_seen(self):

        self.quests_been_updated = False

    def to_see_quests(self):

        return self.quests_been_updated

    def mark_completed(self, quest):

        self.quests_completed[quest] = True
        self.completed_quests[quest] = story_data.quests[quest]
        self.remove_quest(quest)

    def is_complete(self, quest):

        return self.quests_completed[quest]

    def purge_completed(self):

        self.completed_quests.clear()

    def check_complete(self, quest_criteria):

        quests_to_follow = []

        for path in story_data.quest_path.items():
            if quest_criteria[1] in path[1] and not self.is_complete(path[0]):
                quests_to_follow += [path[0]]

        [self.follow_path(quest) for quest in quests_to_follow]

        for quest in self.quests.items():
                for criteria in story_data.completion_criteria[quest[0]]:
                    if criteria.split("/") == quest_criteria:
                        if quest[0] in self.objective_progress:
                            self.objective_progress[quest[0]][criteria] = True

                            if all([n[1] for n in list(self.objective_progress[quest[0]].items())]):
                                quests_to_follow += [quest[0]]
                                if quest[0] in self.quest_updates:
                                    self.quest_updates[quest[0]]()
                        else:
                            quests_to_follow += [quest[0]]
                            if quest[0] in self.quest_updates:
                                self.quest_updates[quest[0]]()

        [self.follow_path(quest) for quest in quests_to_follow]

    def update_dan(self):

        self.master.chunk_controller.locate_entity(12).meta.interaction = \
            """self.master.dialogue_controller.start_scene(self.player.beans[0], self.enemy_to_duel, 'dan', 
None, 0);self.master.switch_to(3)"""

    def update_old_man(self):
        e = self.master.chunk_controller.locate_entity(3)

        e.meta.interaction = \
            """self.master.dialogue_controller.start_scene(self.player.beans[0], self.enemy_to_duel, 'old_man2', None, 0)
self.master.switch_to(3)"""
        e.set_important()

    def update_wizard(self):
        e = self.master.chunk_controller.locate_entity(20)
        e.meta.interaction = \
            """self.master.dialogue_controller.start_scene(self.player.beans[0], self.enemy_to_duel, 'wizard', None, 0)
self.master.switch_to(3)"""
        e.set_important()
