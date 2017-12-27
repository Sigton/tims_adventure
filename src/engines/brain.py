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

        self.weights = [[0 for n in range(inputs)] for m in range(outputs)]
        self.bias = [0 for n in range(outputs)]

    def get_output(self, in_data):

        out_data = [[sum(m) for m in zip(in_data, self.weights[n])] for n in range(self.outputs)]
        print(out_data)
        return out_data.index(max(out_data))


if __name__ == "__main__":
    test_brain = Brain(8, 4)

    print(test_brain.get_output([1, 0, 1, 1, 0, 0, 1, 0]))
