import random

class Neuron:
    def __init__(self, value = 0, nbWeight = 0):
        self.value = value
        self.weights = []
        self.populate(nbWeight)

    def __str__( self ):
        return 'Value: ' + str(self.value) + ' ; Weights: ' + str(self.weights)

    def __repr__( self ):
        return 'Value: ' + str(self.value) + ' ; Weights: ' + str(self.weights)

    def populate(self, nbWeight):
        self.weights = []
        for i in range(nbWeight):
            self.weights.append(random.random() * 2 - 1)
