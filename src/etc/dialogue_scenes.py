"""
dialogue_scenes.py

This file holds all of the
conversations between the beans.
"""

scenes = {
    "villager1": [
        ("What's happening here?", 0),
        ("They're coming!", 1),
        ("Who is?", 0),
        ("We have to run!", 1)
    ],
    "villager2": [
        ("We can't stay here anymore.", 1),
        ("Why not?", 0),
        ("They'll be here soon, we need to leave now.", 1)
    ],
    "villager3": [
        ("Strange things are happening here.", 1),
        ("What is happening?", 0),
        ("I'm not sure, I just know it's bad. Try to find the old man, he is wise and might know more.", 1),
        ("He will be somewhere in the town. Good luck.", 1)
    ],
    "old_man": [
        ("You came to see me?", 1),
        ("Yes, what is happening here?", 0),
        ("Dark things are happening. Dark, dark things...", 1),
        ("It all started when they arrived in the land.", 1),
        ("Who?", 0),
        ("The formidable, corrupted Jelly Monster.", 1)
    ]
}
