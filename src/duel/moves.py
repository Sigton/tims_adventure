"""
moves.py

This file holds all of
the information about
the different moves that
a player can make.
"""

moves = [
    {"name": "Tackle", "str_mod": 1, "effects":
        "self.start_shake(18, 10, 10, {}1);self.master.sound_engine.queue_sound((self.master.sound_engine.punch, 0))",
     "energy": 5, "xp": 5},
    {"name": "Burn", "str_mod": 1.4, "effects":
        """self.particle_engine.create_particle_spread('fire', 30, {}, {}, 130, 25, 20, 25, 5)
self.master.sound_engine.queue_sound((self.master.sound_engine.burn, 0))""",
     "energy": 15, "xp": 15},
    {"name": "Freeze", "str_mod": 1.5, "effects":
        """self.particle_engine.create_particle_spread('snow', 50, {}, {}, 150, 6, 5, 45, 2)""",
     "energy": 20, "xp": 20},
    {"name": "Chili Chuck", "str_mod": 0.7, "effects":
        """self.particle_engine.create_particle_spread('chili', 15, {}, {}, 150, 10, 0, 10, 10)""",
     "energy": 4, "xp": 4}
]
