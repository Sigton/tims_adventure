"""
entity_meta.py

This file holds information about
all of the different beans, eg
their max hp, moves, starting damage.
"""

entity_data = {
    "chili": {"max_hp": 100, "moves": [1, 3], "attack": 10, "energy": 100, "display_name": "Chili Bean"},
    "cool": {"max_hp": 100, "moves": [0, 2], "attack": 10, "energy": 100, "display_name": "Cool Bean"},
    "pickle": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Pickle Bean"},
    "strawberry": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Strawberry Bean"},
    "lemon": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Lemon Bean"},
    "rainbow": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Rainbow Bean"},
    "unicorn": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Unicorn Bean"},
    "hedgehog": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Hedgehog Bean"},
    "poison": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Poison Bean"},
    "carrot": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Carrot Bean"},
    "rabbit": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Rabbit Bean"},
    "what": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "What Beam"},
    "chicken": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Chicken Bean"},
    "wizard": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Wizard Bean"},
    "old_villager": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Old Bean"},
    "tim": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Tim"},
    "fisherman": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Fisherman"},
    "pig": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Pig"},
    "dan": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Dan"},
    "hermit": {"max_hp": 100, "moves": [0, 1], "attack": 10, "energy": 100, "display_name": "Hermit Bean"}
}

item_effects = {
    "EnlightenmentPotion": "",
    "HealthPotion": "self.player.meta.heal(40)",
    "LifePotion": "self.player.meta.heal(75)",
    "WitherPotion": "self.enemy.meta.damage(25);self.master.sound_engine.queue_sound(('potion_fizz', 0))",
    "DeathPotion": "self.enemy.meta.damage(50);self.master.sound_engine.queue_sound(('potion_fizz', 0))"
}
