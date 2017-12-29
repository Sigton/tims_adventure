import random
import math

"""
brain.py

A simple neural network
that is used to make decisions
such as the opponents next move
in the duelling.
"""

weights_preset = [
    [1, 1.5, 1.5, 0.5, 1.5, 1, 1, 1.5],
    [1, 1.5, 0.5, 1.5, 1.5, 1, 1, 1.5],
    [0.5, 0.5, 0.5, 0.5, 0.5, 1.5, 1.5, 0.5],
    [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
]


class Brain:

    def __init__(self, inputs, outputs):

        self.inputs = inputs
        self.outputs = outputs

        self.weights = weights_preset  # [[random.uniform(-1.0, 1.0) for n in range(inputs)] for m in range(outputs)]
        self.bias = [0 for n in range(outputs)]

    def get_output(self, in_data):

        out_data = [sum(x) for x in
                    [[sum(m) for m in zip(in_data, self.weights[n])] for n in range(self.outputs)]]
        print(out_data, [math.tanh(x) for x in out_data])
        return out_data.index(max(out_data))


if __name__ == "__main__":
    test_brain = Brain(8, 4)

    print(test_brain.get_output([1, 0, 1, 1, 0, 0, 1, 0]))
