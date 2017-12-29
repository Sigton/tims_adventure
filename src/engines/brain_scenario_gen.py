import random
import json

with open("src/saves/training_data.json", 'r') as infile:

    scenarios = json.load(infile)["scenarios"]

for n in range(int(input("How many scenarios:"))):
    maxHP = random.randint(100, 250)
    HP = int(maxHP * random.uniform(0, 1))
    hp_lost = maxHP - HP

    playerHP = int(random.randint(100, 250)*random.uniform(0, 1))

    hp_diff = HP - playerHP

    m_attack_hp = random.randint(5, 30)
    a_attack_hp = random.randint(5, 30)

    max_energy = 100
    energy = int(max_energy*random.uniform(0, 1))
    energy_lost = max_energy-energy

    no_hp_items = random.choice([0, 0, 0, 0, 1, 1, 1, 2, 2, 3])
    no_en_items = random.choice([0, 0, 0, 0, 1, 1, 1, 2, 2, 3])

    level = random.randint(1, 5)
    player_level = random.randint(1, 5)

    level_diff = level-player_level

    m_attack_en = int(m_attack_hp*random.uniform(0.5, 1.5))
    a_attack_en = int(a_attack_hp*random.uniform(0.5, 1.5))

    s = [HP, hp_diff, m_attack_hp, a_attack_hp, energy, no_hp_items, no_en_items, level_diff,
         hp_lost, m_attack_en, a_attack_en, energy_lost]
    print(s)
    expected_outcome = input("Expected outcome:")
    if expected_outcome == "":
        continue

    scenarios += [[s, expected_outcome]]

with open("src/saves/training_data.json", 'w') as outfile:
    json.dump({"scenarios": scenarios}, outfile)

