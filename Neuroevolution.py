import random


class Neuroevolution:
    def __init__(self, networkStructure = [2, [2], 1], population = 50,
            elitism = 0.25):
        self.networkStructure = networkStructure
        self.network = []
        self.savedNeuron = []
        self.population = population
        self.elitism = elitism

    def compute(self, inputs):


        return output


    def perceptron(self):
        self.network = []
        inputs = []
        hiddens = []
        output = []

        for i in range(networkStructure[0]):
            inputs[i] = Neuron()

        for i in range(len(networkStructure[1])):
            for j in range(networkStructure[1][i]):
                hiddens[i][j] = Neuron()
        # check neuron construction
