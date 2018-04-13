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
    "villager5": [
        ("Hello young man.", 1),
        ("Do you know what is happening here?", 0),
        ("No, I don't bother myself with such things. You'll have to ask somebody else.", 1)
    ],
    "villager6": [
        ("Oi you, I don't want any trouble. Take your problems someplace else!", 1),
        ("Of course, my bad.", 0)
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
        ("You must find the fisherman, he has more information for you.", 1),
        ("But I'm not brave, I can't do thi-", 0),
        ("Be brave, young Tim. You are the last chance for all the land.", 1),
        ("Okay, where can I find this fisherman?", 0),
        ("Look at the pier by the lake, he shall be working.", 1),
        ("Good luck, young bean.", 1)
    ],
    "north_bean": [
        ("Help! Our village is under attack! We need help!", 1),
        ("What's happening?", 0),
        ("Those evil beans, they're attacking our homes!", 1),
        ("Evil beans?", 0),
        ("The ones from the Jelly Monster! We need someone to save us!", 1),
        ("Can you please help?", 1),
        ("Where is your village?", 0),
        ("""Just follow this path to the east, you'll be there in no time.
But please hurry, we won't be able to defend ourselves for much longer.""", 1)
    ],
    "help_village_bean": [
        ("Help us, our village is being raided!", 1),
        ("There are 6 evil beans in the village, can you defeat them for us?", 1),
        ("I'll try!", 0)
    ],
    "fisherman1": [
        ("Can I help you?", 1),
        ("Yes, I'm looking for the elder bean.", 0),
        ("Do I look that old to you?", 1),
        ("Apologies, sir.", 0)
    ],
    "fisherman2": [
        ("Hello, Mr. Fisherman.", 0),
        ("Whatcha want, kid.", 1),
        ("""The elder villager told me to come and talk to you. He said you had information 
for me.""", 0),
        ("Information? Who are you?", 1),
        ("I'm Tim, and I've bean set on an adventure to conquer the Jelly Monster.", 0),
        ("The Jelly Monster? You are brave.", 1),
        ("Yeah, well about tha-", 0),
        ("Do you know how to fight?", 1),
        ("No, I don't.", 0),
        ("""Meet me at the beach on the other side of town. We'll sort that out, and soon 
you'll be a fantastic fighter.""", 1)
    ],
    "fisherman_duel2": [
        ("Right kid, time to learn to fight.", 1),
        ("There are some rules to fighting around here, you gotta make sure you stick to them. Got it?", 1),
        ("First of all, we take it turns to attack or defend. You'll start, and then I go next.", 1),
        ("What moves have you got?", 1),
        ("Erm, I don't know any.", 0),
        ("Right, I'll teach you how to tackle and how to throw a punch.", 1),
        ("""You can only use those two moves, as well as any potions you pick up along the way.
Using potions does count as your move, however.""", 1),
        ("Make sure you conserve your energy, because without energy you can make moves!", 1),
        ("""I'll go easy on you kid, just cause it's your first time. You still gotta beat me before I let you move on,
 though.""", 1),
        ("Once you have learned to fight, return to the old man. He'll tell you where to go next.", 1)
    ],
    "fisherman_duel1": [
        ("Hello, Mr. Fisherman.", 0),
        ("Whatcha want, kid.", 1),
        ("""The elder villager told me to come and talk to you. He said you had information 
for me.""", 0),
        ("Information? Who are you?", 1),
        ("I'm Tim, and I've bean set on an adventure to conquer the Jelly Monster.", 0),
        ("The Jelly Monster? You are brave.", 1),
        ("Yeah, well about tha-", 0),
        ("Do you know how to fight?", 1),
        ("No, I don't.", 0),
        ("Right kid, time to learn to fight.", 1),
        ("There are some rules to fighting around here, you gotta make sure you stick to them. Got it?", 1),
        ("First of all, we take it turns to attack or defend. You'll start, and then I go next.", 1),
        ("What moves have you got?", 1),
        ("Erm, I don't know any.", 0),
        ("Right, I'll teach you how to tackle and how to throw a punch.", 1),
        ("""You can only use those two moves, as well as any potions you pick up along the way.
Using potions does count as your move, however.""", 1),
        ("Make sure you conserve your energy, because without energy you can make moves!", 1),
        ("""I'll go easy on you kid, just cause it's your first time. You still gotta beat me before I let you move on,
 though.""", 1),
        ("Once you have learned to fight, return to the old man. He'll tell you where to go next.", 1)
    ],
    "old_man2": [
        ("I see you have completed your trainnig. You are now ready to begin your adventure.", 1),
        ("Brilliant, where do I go?", 0),
        ("From here, head North.", 1),
        ("Just North? Not to the lair of the Jelly Monster or anything?", 0),
        ("""Patience, Tim. It is a long way to the Jelly Monster from here. Follow the Northern path, you shall meet 
someone on the trail.""", 1)
    ]
}


quests = {
    "talk_villagers": "Talk to the villagers.",
    "old_man": "Find the elder villager.",
    "heading_north": "Explore to the north.",
    "help_village": "Help the village!",
    "liberate_village": "Liberate the village.",
    "fisherman": "Find the fisherman.",
    "learn_fight": "Learn to fight!",
    "old_man2": "Talk to the elder villager.",
    "dan": "Talk to Dan."
}


completion_criteria = {
    "talk_villagers": ["scene/villager3", "scene/villager4"],
    "old_man": ["scene/old_man"],
    "heading_north": ["scene/north_bean"],
    "help_village": ["scene/help_village_bean"],
    "liberate_village": ("duel/6", "duel/7", "duel/8", "duel/9", "duel/10", "duel/11"),
    "fisherman": ["scene/fisherman2", "scene/fisherman_duel1"],
    "learn_fight": ["duel/14"],
    "old_man2": ["scene/old_man2"],
    "dan": []
}


quest_path = {
    "talk_villagers": ["old_man"],
    "old_man": ["fisherman"],
    "heading_north": ["help_village"],
    "help_village": ["liberate_village"],
    "liberate_village": ["dan"],
    "fisherman": ["learn_fight"],
    "learn_fight": ["old_man2"],
    "old_man2": ["heading_north"],
    "dan": []
}
