import random

class Neuron:
    def __init__(self, value = 0, nbWeight = 0):
        self.value = value
        self.weights = []
        self.populate(nbWeight)

    def populate(self, nbWeight):
        self.weights = []
        for i in range(nbWeight):
            self.weights.append(random.random() * 2 - 1)
