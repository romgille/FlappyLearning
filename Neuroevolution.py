import random


class Neuroevolution:
    def __init__(self, networkStructure = [2, [2], 1], elitism = 0.25):
        self.networkStructure = networkStructure
        self.network = []
        self.savedNeuron = []
        self.elitism = elitism

    def compute(self, inputs):
        #self.generateNetwork(inputs)
        previous = self.network[0]

        for layer in self.network[1]:
            s = 0
            for neuron in layer:
                for p in previous:
                    s += p.value * [e for e in neuron.weight]
                neuron.value = 1/(1 + s**2)
            previous = layer

        for neuron in self.network[2]:
            for p in previous:
                s += p.value * [e for e in neuron.weight]
            neuron.value = 1/(1 + s**2)

        output = []
        for neuron in self.network[2]:
            output.append(neuron.value)

        return output

    def generateNetwork(self, old_inputs):
        if network == []:
            self.perceptron(old_inputs)
            return

        self.network = []
        inputs = []
        hiddens = []
        output = []

        for i in range(networkStructure[0]):
            inputs[i] = Neuron(value = old_inputs[i], nbWeight = 2)

        for i in range(len(networkStructure[1])):
            for j in range(networkStructure[1][i]):
                hiddens[i][j] = Neuron(nbWeight = 2)

        for i in range(networkStructure[2]):
            output[i] = Neuron(nbWeight = 2)

        self.network.append(inputs)
        self.network.append(hiddens)
        self.network.append(output)

        self.breed()


    def perceptron(self, old_inputs):
        self.network = []
        inputs = []
        hiddens = []
        output = []

        for i in range(networkStructure[0]):
            inputs[i] = Neuron(value = old_inputs[i], nbWeight = 2)

        for i in range(len(networkStructure[1])):
            for j in range(networkStructure[1][i]):
                hiddens[i][j] = Neuron(nbWeight = 2)

        for i in range(networkStructure[2]):
            output[i] = Neuron(nbWeight = 2)

        self.network.append(inputs)
        self.network.append(hiddens)
        self.network.append(output)


    def getBestNetworks


    def breed(self, oldNetwork):
                    




    def mutation(self):
        for layer in self.network[1]:
            for neuron in layer:
                for i in range(neuron.weight):
                    if random.rand() > self.mutation_rate:
                        neuron.weight[i] += random.rand() * self.mutation_range * 2 - self.mutation_range

    
