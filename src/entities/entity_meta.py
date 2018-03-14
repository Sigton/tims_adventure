"""
entity_meta.py

This file holds information about
all of the different beans, eg
their max hp, moves, starting damage.
"""

entity_data = {
    "chili": {"max_hp": 100, "moves": [1, 0], "attack": 10, "energy": 100, "display_name": "Chili"},
    "cool": {"max_hp": 100, "moves": [0, 2], "attack": 10, "energy": 100, "display_name": "Cool"},
    "pickle": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Pickle"},
    "strawberry": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Strawberry"},
    "lemon": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Lemon"},
    "rainbow": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Rainbow"},
    "unicorn": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Unicorn"},
    "hedgehog": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Hedgehog"},
    "poison": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Poison"},
    "carrot": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Carrot"},
    "rabbit": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Rabbit"},
    "what": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "What"},
    "chicken": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Chicken"},
    "wizard": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Wizard"},
    "old_villager": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Old"}
}

item_effects = {
    "EnlightenmentPotion": "",
    "HealthPotion": "self.player.meta.heal(20)"
}
