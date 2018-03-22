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
    "villager4": [
        ("Can you help me?", 0),
        ("I'm not the one to be asking, I'm new here. I think there's an elder in the town, try him.", 1)
    ],
    "old_man": [
        ("You came to see me?", 1),
        ("Yes, what is happening here?", 0),
        ("Dark things are happening. Dark, dark things...", 1),
        ("It all started when they arrived in the land.", 1),
        ("Who?", 0),
        ("The formidable, corrupted Jelly Monster. It came to our lands, and brought its negativity with it.", 1),
        ("""The three wizard guardians of the land tried to stop the monster, but its negativity was too strong for 
even the wizard's magical power.""", 1),
        ("""Before the wizard's themselves were dragged into darkness, they united their 
power and built gates between the sections of the land.""", 1),
        ("Despite the wizard's efforts, there is still little hope for the land. There is evil everywhere.", 1),
        ("""This village is one of the last standing. All of the villagers are worried; there is not long left until 
the evil beans reach here.""", 1),
        ("What will happen once they reach the village?", 0),
        ("""These villagers will become corrupted. Their minds cast into darkness, and they will join the ranks of the 
jelly monsters army.""", 1),
        ("We need a brave, brave warrior to stop the jelly monster and its evil beans.", 1),
        ("Someone who will not be scared by the face of evil, someone who will not stop no matter what.", 1),
        ("Who could this warrior be?", 0),
        ("Well done for volunteering, brave young bean.", 1),
        ("Wait wha-", 0),
        ("I knew you could do it!", 1),
        ("Head north from here - an adventure awaits you!", 1),
        ("But I'm not brave, I can't do thi-", 0),
        ("You must hurry; you are our only hope.", 1)
    ]
}


quests = {
    "talk_villagers": "Talk to the villagers",
    "old_man": "Find the elder villager"
}


completion_criteria = {
    "talk_villagers": ["scene/villager3", "scene/villager4"],
    "old_man": ["scene/old_man"]
}


quest_path = {
    "talk_villagers": ["old_man"],
    "old_man": []
}
