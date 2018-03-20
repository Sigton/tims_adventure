import math
import json

"""
brain.py

A simple neural network
that is used to make decisions
such as the opponents next move
in the duelling.
"""


weights_preset = [
    [2, 3, 4, 0.25, 3, 1, 1, 3, 1, 0.25, 3, 0.5],
    [2, 3, 0.25, 4, 3, 1, 1, 3, 1, 3, 0.25, 0.5],
    [0.5, -1.5, 1, 1, -0.5, 3, 3, -1.5, 2, 1.5, 1.5, 3],
    [-1, -2, 1, 1, -0.5, 0.5, 0.5, -4, 3, 1, 1, 3]
]
with open("src/saves/training_data.json", 'r') as infile:
    scenarios = json.load(infile)["scenarios"]


class Brain:

    def __init__(self, inputs, outputs):

        self.inputs = inputs
        self.outputs = outputs

        self.weights = weights_preset

    def get_output(self, in_data):

        squished_data = squish(in_data)

        out_data = [sum([squished_data[i]*weights_preset[x][i]
                         for i in range(self.inputs)]) for x in range(self.outputs)]
        return squish(out_data)


def get_cost(out_data, expected_outcome):

    squashed_out_data = squish(out_data)
    formatted_outcome = [1.0 if expected_outcome == i else 0.0 for i in range(len(squashed_out_data))]

    cost = [math.pow(squashed_out_data[i]-formatted_outcome[i], 2) for i in range(len(squashed_out_data))]
    return sum(cost)


def get_max_idx(out_data):

    return out_data.index(max(out_data))


def squish(data):

    squished_data = [(x-min(data))/(max(data)-min(data)) for x in data]
    return squished_data


if __name__ == "__main__":
    test_brain = Brain(12, 4)

    print("Running test scenarios")
    n = 0
    c = 0
    costs = []
    for s in scenarios:
        n += 1

        raw_output = test_brain.get_output(s[0])

        output_idx = get_max_idx(raw_output)
        output_cost = get_cost(raw_output, int(s[1]))

        costs += [output_cost]

        if int(s[1]) == output_idx:
            c += 1

        print("Scenario {}: {}. Expected outcome: {}. Cost: {}".format(n, output_idx, s[1], output_cost))

    print("Success rate: {}. Average cost: {}".format(c/n*100, sum(costs)/len(costs)))


# New Brain design
'''

class Brain:
    def __init__(self):

        self.options = [
            "main_attack",
            "alt_attack",
            "item",
            "retreat"
        ]

        self.costs = {
            "main_attack": 15,
            "alt_attack": 15,
            "item": 30,
            "retreat": 40
        }

        self.damaging_moves = ["main_attack", "alt_attack"]

    def evaluate(self):

        for move in self.options:
            if move in self.damaging_moves:
                pass
            else:
                pass
'''
