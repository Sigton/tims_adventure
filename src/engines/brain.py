"""
brain.py

A simple neural network
that is used to make decisions
such as the opponents next move
in the duelling.
"""


class Brain:

    def __init__(self, inputs, outputs):

        self.inputs = inputs
        self.outputs = outputs

        self.weights = [[1 for n in range(inputs)] for m in range(outputs)]

    def get_output(self, in_data):

        pass


if __name__ == "__main__":
    test_brain = Brain(8, 4)
