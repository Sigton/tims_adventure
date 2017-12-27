"""
brain.py

A simple neural network
that is used to make decisions
such as the opponents next move
in the duelling.
"""


class Brain:

    def __init__(self, inputs, outputs):

        self.network = [{n: [1 for x in range(outputs)]} for n in range(inputs)]


if __name__ == "__main__":
    test_brain = Brain(8, 4)
