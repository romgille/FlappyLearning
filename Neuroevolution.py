class Neuroevolution:

    def __init__(self, network = [1,[1],1], population = 50, elitism = 0.2,
            randomBehavior = 0.2, mutationRate = 0.1, mutationRange = 0.5,
            historic = 0, lowHistoric = False, scoreSort = -1, nbChild = 1):

        self.network = network
        self.population = population
        self.elitism = elitism
        self.randomBehaviour = randomBehavior
        self.mutationRate = mutationRate
        self.mutationRange = mutationRange
        self.historic = historic
        self.lowHistoric = lowHistoric
        self.scoreSort = scoreSort
        self.nbChild = nbChild
        self.neurons = [[]] #first element is value, second is weight

    @staticmethod
    def activation(a):
        return (1 / (1 + math.exp((-a)/1)))

    @staticmethod
    def randomClamped(a):
        return random.random() * 2 - 1

    def populateNeuron(self, nbNeurons):
        neuron = []
        for i in range(0, nbNeurons):
            neuron.append(0, self.randomClamped())
        return neuron

    def populate(self, nbNeurons, nbInputs):
        layer = []
        for i in range(0, nbNeurons):
            n = self.populateNeuron(nbInputs)
            layer.append(n)
        return layer

    def network(self, input, hiddens, output):
        layers = []
        index = 0
        previousNeurons = 0
        layer = populate(input, previousNeurons)
        previousNeurons = input
        layers.append(layer)
        index += 1

        for hidden in hiddens:
            layer = populate(hidden, previousNeurons)
            previousNeurons = hidden
            layers.append(layer)
            index += 1

        layer = populate(output, previousNeurons)
        layers.append(layer)

        for i in range(0, len(inputs)):
            if layers[0] and layers[0][i]:
                layers[0][i][0] = inputs[i]

        prevLayer = layers[0]
        for i in range(0, len(layers)):
            for j in range(0, len(layers[i])):
                sum = 0
                for k in range(0, len(prevLayer)):
                    sum += prevLayer[k].value * layers[i][j][1][k]

                layers[i][j][0] = activation(sum)

            prevLayer = layers[i]

        out = []
        lastLayers = layers[len(layers) - 1]
        for lastLayer in lastLayers:
            out.append(lastLayer[0])

        return out

    def getNetworkSave(self, layers):
        neurons = []
        weights = []

        for layer in layers:
            neurons.append(len(layer))
            for j in range(0, len(layer)):
                for k in range(0, len(layer[j][1])):
                    weights.append(layer[j][1][k])

        return [neurons, weights]

    def setNetworkSave(self, save):
        previousNeurons = 0
        index = 0
        indexWeights = 0
        layers = 0

        for i in range(0, len(save[0])):
            layer = populate(save[0][i], previousNeurons)

            for j in range(0, len(layer)):
                for k in range(0, len(layer[j][1])):
                    layer[j][1][k] = save[1][indexWeights]
                    indexWeights += 1

            previousNeurons = save[0][i]
            index += 1
            layers.append(layer)

        return layers


    /*GENERATION******************************************************************/
    /**
     * Generation class.
     *
     * Composed of a set of Genomes.
     *
     * @constructor
     */
    var Generation = function () {
        this.genomes = [];
        this.crossoverFactor = 0.5;
    }

    /**
     * Add a genome to the generation.
     *
     * @param {genome} Genome to add.
     * @return void.
     */
    Generation.prototype.addGenome = function (genome) {
        // Locate position to insert Genome into.
        // The gnomes should remain sorted.
        for (var i = 0; i < this.genomes.length; i++) {
            // Sort in descending order.
            if (self.options.scoreSort < 0) {
                if (genome.score > this.genomes[i].score) {
                    break;
                }
                // Sort in ascending order.
            } else {
                if (genome.score < this.genomes[i].score) {
                    break;
                }
            }

        }

        // Insert genome into correct position.
        this.genomes.splice(i, 0, genome);
    }

    /**
     * Breed to genomes to produce offspring(s).
     *
     * @param {g1} Genome 1.
     * @param {g2} Genome 2.
     * @param {nbChilds} Number of offspring (children).
     */
    Generation.prototype.breed = function (g1, g2, nbChilds) {
        var datas = [];
        for (var nb = 0; nb < nbChilds; nb++) {
            // Deep clone of genome 1.
            var data = JSON.parse(JSON.stringify(g1));
            for (var i in g2.network.weights) {
                // Genetic crossover
                if (Math.random() <= this.crossoverFactor) {
                    data.network.weights[i] = g2.network.weights[i];
                }
            }

            // Perform mutation on some weights.
            for (var i in data.network.weights) {
                if (Math.random() <= self.options.mutationRate) {
                    data.network.weights[i] += Math.random() *
                        self.options.mutationRange *
                        2 -
                        self.options.mutationRange;
                }
            }
            datas.push(data);
        }

        return datas;
    }

    /**
     * Generate the next generation.
     *
     * @return Next generation data array.
     */
    Generation.prototype.generateNextGeneration = function () {
        var nexts = [];

        for (var i = 0; i < Math.round(self.options.elitism *
            self.options.population); i++) {
            if (nexts.length < self.options.population) {
                // Push a deep copy of ith Genomes Nethwork.
                nexts.push(JSON.parse(JSON.stringify(this.genomes[i].network)));
            }
        }

        for (var i = 0; i < Math.round(self.options.randomBehaviour *
            self.options.population); i++) {
            var n = JSON.parse(JSON.stringify(this.genomes[0].network));
            for (var k in n.weights) {
                n.weights[k] = self.options.randomClamped();
            }
            if (nexts.length < self.options.population) {
                nexts.push(n);
            }
        }

        var max = 0;
        while (true) {
            for (var i = 0; i < max; i++) {
                // Create the children and push them to the nexts array.
                var childs = this.breed(this.genomes[i], this.genomes[max],
                    (self.options.nbChild > 0 ? self.options.nbChild : 1));
                for (var c in childs) {
                    nexts.push(childs[c].network);
                    if (nexts.length >= self.options.population) {
                        // Return once number of children is equal to the
                        // population by generatino value.
                        return nexts;
                    }
                }
            }
            max++;
            if (max >= this.genomes.length - 1) {
                max = 0;
            }
        }
    }


    /*GENERATIONS*****************************************************************/
    /**
     * Generations class.
     *
     * Holds previous Generations and current Generation.
     *
     * @constructor
     */
    var Generations = function () {
        this.generations = [];
        var currentGeneration = new Generation();
    }

    /**
     * Create the first generation.
     *
     * @param {input} Input layer.
     * @param {input} Hidden layer(s).
     * @param {output} Output layer.
     * @return First Generation.
     */
    Generations.prototype.firstGeneration = function (input, hiddens, output) {
        console.log(input);
        console.log(hiddens);
        console.log(output);
        var out = [];
        for (var i = 0; i < self.options.population; i++) {
            // Generate the Network and save it.
            var nn = new Network();
            nn.perceptronGeneration(input, hiddens, output);
            out.push(nn.getSave());
        }

        this.generations.push(new Generation());
        return out;
    }

    /**
     * Create the next Generation.
     *
     * @return Next Generation.
     */
    Generations.prototype.nextGeneration = function () {
        if (this.generations.length == 0) {
            // Need to create first generation.
            return false;
        }

        var gen = this.generations[this.generations.length - 1].generateNextGeneration();
        this.generations.push(new Generation());
        return gen;
    }

    /**
     * Add a genome to the Generations.
     *
     * @param {genome}
     * @return False if no Generations to add to.
     */
    Generations.prototype.addGenome = function (genome) {
        // Can't add to a Generation if there are no Generations.
        if (this.generations.length == 0) return false;

        // FIXME addGenome returns void.
        return this.generations[this.generations.length - 1].addGenome(genome);
    }


    /*SELF************************************************************************/
    self.generations = new Generations();

    /**
     * Reset and create a new Generations object.
     *
     * @return void.
     */
    self.restart = function () {
        self.generations = new Generations();
    }

    /**
     * Create the next generation.
     *
     * @return Neural Network array for next Generation.
     */
    self.nextGeneration = function () {
        var networks = [];

        if (self.generations.generations.length == 0) {
            // If no Generations, create first.
            networks = self.generations.firstGeneration(
                self.options.network[0],
                self.options.network[1],
                self.options.network[2]
            );
        } else {
            // Otherwise, create next one.
            networks = self.generations.nextGeneration();
        }

        // Create Networks from the current Generation.
        var nns = [];
        for (var i in networks) {
            var nn = new Network();
            nn.setSave(networks[i]);
            nns.push(nn);
        }

        if (self.options.lowHistoric) {
            // Remove old Networks.
            if (self.generations.generations.length >= 2) {
                var genomes =
                    self.generations
                    .generations[self.generations.generations.length - 2]
                    .genomes;
                for (var i in genomes) {
                    delete genomes[i].network;
                }
            }
        }

        if (self.options.historic != -1) {
            // Remove older generations.
            if (self.generations.generations.length > self.options.historic + 1) {
                self.generations.generations.splice(0,
                    self.generations.generations.length - (self.options.historic + 1));
            }
        }

        return nns;
    }

    /**
     * Adds a new Genome with specified Neural Network and score.
     *
     * @param {network} Neural Network.
     * @param {score} Score value.
     * @return void.
     */
    self.networkScore = function (network, score) {
        self.generations.addGenome(new Genome(score, network.getSave()));
    }
}
