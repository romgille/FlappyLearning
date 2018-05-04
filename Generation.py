class Generation:

    def __init__(self):
        self.genomes = []
        self.crossoverFactor = 0.5

    def addGenome(self, genome, genomes):
        for i in range(genomes):
            if Neuroevolution.scoreSort < 0:
                if genome.score > genomes[i].score:
                    break
            else:
                if genome.score < genomes[i].score:
                    break

        genomes.splice(i, 0, genome) # TODO trouver fonction pour splice

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
