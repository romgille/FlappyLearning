import random

class Neuron:
    def __init__(self, value = 0, nbWeight = 0):
        self.value = value
        self.weight = []
        self.populate(nbWeight)

    def populate(self, nbWeight):
        for i in range(nbWeight):
            self.weight[i] = random.random() * 2 - 1
