"""
moves.py

This file holds all of
the information about
the different moves that
a player can make.
"""

moves = [
    {"name": "Tackle", "str_mod": 1, "effects":
        "self.start_shake(18, 10, 10, {}1);self.master.sound_engine.queue_sound(('punch', 0))",
     "energy": 6, "xp": 6},
    {"name": "Burn", "str_mod": 1.4, "effects":
        """self.particle_engine.create_particle_spread('fire', 30, {}, {}, 130, 25, 20, 25, 5)
self.master.sound_engine.queue_sound(('burn', 0))""",
     "energy": 15, "xp": 15},
    {"name": "Freeze", "str_mod": 1.5, "effects":
        """self.particle_engine.create_particle_spread('snow', 50, {}, {}, 150, 6, 5, 45, 2)""",
     "energy": 20, "xp": 20},
    {"name": "Chili Chuck", "str_mod": 0.7, "effects":
        """self.particle_engine.create_particle_spread('chili', 45, {}, {}, 150, 15, 10, 10, 10)""",
     "energy": 5, "xp": 5},
    {"name": "Punch", "str_mod": 1.2, "effects":
        """self.start_shake(18, 10, 10, {}1);self.master.sound_engine.queue_sound(('punch', 0))""",
     "energy": 8, "xp": 8},
    {"name": "Snowball", "str_mod": 0.6, "effects":
        """self.particle_engine.create_particle_spread('snowball', 15, {}, {}, 150, 15, 10, 30, 2)""",
     "energy": 4, "xp": 4},
    {"name": "Feathers", "str_mod": 0.9, "effects":
        """self.particle_engine.create_particle_spread('feather', 45, {}, {}, 150, 35, 10, 5, 5)""",
     "energy": 6, "xp": 6},
    {"name": "Sneak Attack", "str_mod": 1.3, "effects":
        """self.particle_engine.create_particle_spread('leaf', 45, {}, {}, 150, 45, 10, 10, 10)
self.start_shake(18, 10, 10, {}1)""",
     "energy": 13, "xp": 13},
    {"name": "Poison Spit", "str_mod": 1.7, "effects":
        """self.particle_engine.create_particle_spread('venom', 20, {}, {}, 150, 10, 10, 40, 4)""",
     "energy": 23, "xp": 23},
    {"name": "Citrus Spray", "str_mod": 1.2, "effects":
        """self.particle_engine.create_particle_spread('lemon', 25, {}, {}, 150, 20, 10, 10, 10)""",
     "energy": 10, "xp": 10},
]
