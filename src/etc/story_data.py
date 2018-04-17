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
    "villager7": [
        ("Excuse me, do you know what is happening here.", 0),
        ("I've heard rumours, which I believe are being spread by that nonsense-speaking old man!", 1),
        ("Do you know where he is?", 0),
        ("Eh, he'll be about the village. You'll find him somewhere.", 1)
    ],
    "villager8": [
        ("Hello!", 0),
        ("Sorry, I'm afraid I can't talk. I'm in a hurry and got places to be.", 1),
        ("No problem.", 0)
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
        ("Mr. Fisherman, sir?", 0),
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
Using potions will use up your move, however.""", 1),
        ("Make sure you conserve your energy, because without energy you can't make moves!", 1),
        ("""I'll go easy on you kid, just cause it's your first time. You still gotta beat me before I let you move on,
 though.""", 1),
        ("Once you have learned to fight, return to the old man. He'll tell you where to go next.", 1)
    ],
    "fisherman_duel1": [
        ("Mr. Fisherman, sir?", 0),
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
Using potions will use up your move, however.""", 1),
        ("Make sure you conserve your energy, because without energy you can't make moves!", 1),
        ("""I'll go easy on you kid, just cause it's your first time. You still gotta beat me before I let you move on,
 though.""", 1),
        ("Once you have learned to fight, return to the old man. He'll tell you where to go next.", 1)
    ],
    "old_man2": [
        ("I see you have completed your training. You are now ready to begin your adventure.", 1),
        ("Brilliant, where do I go?", 0),
        ("From here, head North.", 1),
        ("North? Is that where the lair of the Jelly Monster is?", 0),
        ("""Patience, Tim. It is a long way to the Jelly Monster from here. Follow the Northern path, you shall meet 
someone on the trail.""", 1),
        ("Good luck, Tim.", 1)
    ],
    "dan": [
        ("Thank you for liberating our village! We will be forever grateful.", 1),
        ("Don't worry about it, just tryna help.", 0),
        ("Who are you, anyway?", 1),
        ("I'm Tim, and you are?", 0),
        ("Dan. What brings you out here?", 1),
        ("I'm on an adventure, I suppose.", 0),
        ("Ooh, an adventure? I love adventures! What are you adventuring for?", 1),
        ("I've been set a quest to conquer the Jelly Monster.", 0),
        ("The Jelly Monster? It's real?", 1),
        ("Yeah, it was the Jelly Monster that sent these evil beans to attack your village.", 0),
        ("Who else is with you on your adventure?", 1),
        ("Um, no-one. It's just me.", 0),
        ("Well, count me in. You'll need some company.", 1),
        ("Are you sure? It's a long way from here.", 0),
        ("""Yes. There's no future for me here. I'd just become a farmer or a fisherman like everyone else. I want to do
 something special!""", 1),
        ("Well, welcome to the adventure crew, Dan!", 0),
        ("Where are we going next?", 1),
        ("Erm, I'm not sure. Where did these evil beans come from?", 0),
        ("They came from the north-west... Oh no! That's where Dermot lives!", 1),
        ("Dermot?", 0),
        ("He's a bit of a hermit, he lives in the forest. We should go check if he's all okay.", 1),
        ("Okay, let's go!", 0)
    ],
    "hermit": [
        ("Mr Dermot?", 0),
        ("What have you come here to bother me with?", 1),
        ("We were just stopping by to see if you're alright.", 0),
        ("If I'm alright? Well of course I'm alright! Why wouldn't I be alright?", 1),
        ("""Well, there were some evil beans that came from this direction and we were wondering if they had done 
anything to you.""", 0),
        ("I'm too crabbit already for any of those horrible things to have any effect on me.", 1),
        ("Ah well, that's good I suppose.", 0),
        ("Yes, now if you wouldn't mind could I have some peace and quiet?", 1),
        ("""I didn't move to this forest just to have you pesky kids come knocking on my door to ask useless questions 
all day!""", 1),
        ("One moment, sir. Do you know perhaps where the evil beans came from?", 0),
        ("I don't know and neither do I wan't to know! Ask the wizard, he'll know!", 1),
        ("Wizard? Where is this wizard?", 0),
        ("In a lonely and isolated location, just like me. He resides over the hidden lake. Good luck finding it.", 1),
        ("Thank you very much.", 0),
        ("Now go away, I don't want no more of your nonsense business.", 1)
    ],
    "lake_warning": [
        ("Where are you headed, young travellers?", 1),
        ("We're looking for the hidden lake.", 0),
        ("You have found the hidden lake, but I cannot let you pass any further.", 1),
        ("Why not?", 0),
        ("A hoard of evil beans just passed across this bridge.", 1),
        ("What are they looking for?", 0),
        ("I fear that they have come to slay the wizard.", 1),
        ("They have been hunting down the last few wizards of the land, that have now all dropped into hiding.", 1),
        ("Can we not help the wizard?", 0),
        ("It is too dangerous. Those were strong evil beans that marched this way.", 1),
        ("Well, we're going to help this wizard.", 0),
        ("You will not return over this bridge. It shall be the end of both of you.", 1)
    ],
    "wizard": [
        ("Hello there, young travellers.", 1),
        ("Thank you for defending me from those evil beans. I do not have the strength I once did, you saved me.", 1),
        ("Now, I must ask, why have you sought me out?", 1),
        ("Dermot sent us here, he said you might know about the evil beans.", 0),
        ("Ahh, Dermot. That's a face I haven't seen in a long time. I must give him a visit sometime...", 1),
        ("Excuse me, sir, the evil beans?", 0),
        ("""Yes, sorry. Got a little bit distracted there. I do it quite a lot sometimes actua- Ah I'm doing it again, 
aren't I?""", 1),
        ("Right. The evil beans. What do you wish to know?", 1),
        ("Where are they coming from?", 0),
        ("""They come from the North, that is where the gate to this land is. The once magnificent gates between the 
lands are now painted black with evil.""", 1),
        ("""They allow the passage of the evil beans, but any of us survivors wouldn't dream of going anywhere near 
such treacherous locations.""", 1),
        ("Is the Jelly Monster on the other side of the gateway?", 0),
        ("There are many gates before you reach the Jelly Monster. Why do you ask?", 1),
        ("We're on a quest to destroy the Jelly Monster.", 0),
        ("You're either brave or foolish, but I suspect probably both.", 1),
        ("Why are you attempting such a daring adventure?", 1),
        ("The Elder Villager from the nearby village set me on it. Dan tagged along when I liberated his village", 0),
        ("The Elder Villager? Ahh. He is wise, wiser than me. He was always the better wizard.", 1),
        ("He's a wizard?", 0),
        ("""Oh, yes. So is Dermot. There are a lot of wizards hiding around these days. We can't show ourselves any more, 
not since the Jelly Monster took over.""", 1),
        ("Well, will you help us with where to go next?", 0),
        ("I can do better. I can show you where to go next.", 1),
        ("Far too long have I sat on this beach. I shall join you on your quest.", 1),
        ("Thank you, welcome to the team Mr. Wizard!", 0)
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
    "dan": "Talk to Dan.",
    "hermit": "Find Dermot the Hermit.",
    "hidden_lake": "Find the hidden lake.",
    "defend_wizard": "Defend the wizard!",
    "wizard": "Talk to the wizard.",
    "thanks": "Thank you for playing!"
}


completion_criteria = {
    "talk_villagers": ["scene/villager3", "scene/villager4", "scene/villager7"],
    "old_man": ["scene/old_man"],
    "heading_north": ["scene/north_bean"],
    "help_village": ["scene/help_village_bean"],
    "liberate_village": ("duel/6", "duel/7", "duel/8", "duel/9", "duel/10", "duel/11"),
    "fisherman": ["scene/fisherman2", "scene/fisherman_duel1"],
    "learn_fight": ["duel/14"],
    "old_man2": ["scene/old_man2"],
    "dan": ["scene/dan"],
    "hermit": ["scene/hermit"],
    "hidden_lake": ["scene/lake_warning"],
    "defend_wizard": ("duel/22", "duel/23", "duel/24", "duel/25"),
    "wizard": ["scene/wizard"],
    "thanks": []
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
    "dan": ["hermit"],
    "hermit": ["hidden_lake"],
    "hidden_lake": ["defend_wizard"],
    "defend_wizard": ["wizard"],
    "wizard": ["thanks"],
    "thanks": []
}
