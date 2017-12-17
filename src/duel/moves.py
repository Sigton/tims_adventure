"""
moves.py

This file holds all of
the information about
the different moves that
a player can make.
"""

moves = [
    {"name": "Tackle", "str_mod": 1, "effects":
        "self.start_shake_{}(18, 10, 10, {}1)",
     "energy": 5, "xp": 5},
    {"name": "Burn", "str_mod": 1.4, "effects":
        """self.particle_engine.create_particle_spread('fire', 30, {}, {}, 130, 25, 20, 25, 5)""",
     "energy": 15, "xp": 15}
]
