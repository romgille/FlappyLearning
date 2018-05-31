import random

import Neuron

class Neuroevolution:
    def __init__(self, network_structure = [2, [2], 1]):
        self.network_structure = network_structure
        self.network = []
        self.mutation_rate = 0.1
        self.mutation_range = 0.5

    def compute(self, inputs):
        for i in range(len(self.network[0])):
            self.network[0][i].value = inputs[i]

        previous = self.network[0]

        for layer in self.network[1]:
            for neuron in layer:
                s = 0
                for p in previous:
                    for e in neuron.weights:
                        s += p.value * e
                print('s=' + str(s))
                neuron.value = 1 / (1 + s ** 2)
                print(neuron.value)
                print('---')
            previous = layer

        for neuron in self.network[2]:
            for p in previous:
                for e in neuron.weights:
                    s += p.value * e
            neuron.value = 1 / (1 + s ** 2)

        # no need to use output array
        # output = []
        # for neuron in self.network[2]:
        #     output.append(neuron.value)
        #
        # return output[0]

        return self.network[2][0].value

    def generateNetwork(self):
        if self.network == []:
            self.perceptron()
            return

        self.network = []
        inputs = []
        hiddens = []
        output = []

        for i in range(self.network_structure[0]):
            inputs[i] = Neuron.Neuron(nbWeight = 2)

        for i in range(len(self.network_structure[1])):
            for j in range(self.network_structure[1][i]):
                hiddens[i][j] = Neuron.Neuron(nbWeight = 2)

        for i in range(self.network_structure[2]):
            output[i] = Neuron.Neuron(nbWeight = 2)

        self.network.append(inputs)
        self.network.append(hiddens)
        self.network.append(output)

    def perceptron(self):
        self.network = []
        inputs = []
        hiddens = []
        output = []

        for i in range(self.network_structure[0]):
            inputs.append(Neuron.Neuron(nbWeight = 2))

        for i in range(len(self.network_structure[1])):
            hiddens.append([])
            for j in range(self.network_structure[1][i]):
                hiddens[i].append(Neuron.Neuron(nbWeight = 2))

        for i in range(self.network_structure[2]):
            output.append(Neuron.Neuron(nbWeight = 2))

        self.network.append(inputs)
        self.network.append(hiddens)
        self.network.append(output)

    def breed(self, oldNetwork):
        for i in range(len(self.network[1].layer)):
            for j in range(len(self.network[1][i].neuron)):
                for k in range(len(self.network[1][i].neuron[i].weights)):
                    if random.random() > 0.5:
                        self.network[1][i].neuron[i].weights[j] = oldNetwork[1][i].neuron[j].weights[k]

    def mutation(self):
        for layer in self.network[1]:
            for neuron in layer:
                for i in range(len(neuron.weights)):
                    if random.random() > self.mutation_rate:
                        neuron.weights[i] += random.random() * self.mutation_range * 2 - self.mutation_range

# class BestNetwork:
#     def __init__(self):
#         self.
