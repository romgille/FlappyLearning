import random

import Background
import Bird
import config
import Pipe

class Game:
    def __init__(self):
        self.background = Background.Background()
        self.pipes = []
        self.birds = []
        self.score = 0
        self.width = 500
        self.height = 512
        self.spawnInterval = 90
        self.interval = 0
        self.gen = []
        self.alives = 0
        self.generation = 0
        self.maxScore = 0

    def start(self):
        self.birds = [Bird.Bird()]
        # self.interval = 0
        # self.score = 0
        # self.pipes = []
        # self.birds = []
        # self.gen = [] # need Nerovol implementaion #Neuvol.nextGeneration()
        #
        # for generation in self.gen:
        #     b = Bird.Bird()
        #     self.birds.append(b)
        #
        # self.generation += 1
        # self.alives = len(self.birds)

    def update(self, deltaTime):
        # nothing to do if all birds are dead
        if len(self.birds) == 0:
            return

        # move the background
        self.background.update(deltaTime)

        # find next holl
        # nextHoll = 0
        # for i in range(0, len(self.pipes), 2):
        #     pipe = self.pipes[i]
        #     if pipe.x + pipe.width > self.birds[0].x:
        #         nextHoll = pipe.height/self.height
        #         break

        # update birds
        for b in self.birds:
            b.update(deltaTime)
        # for i in range(0, len(self.birds)):
        #     bird = self.birds[i]
        #     network = self.gen[i]
        #     if bird.alive:
        #         inputs = [bird.y / self.height, nextHoll]
        #
        #         output = network.compute(inputs)
        #         if len(output) <= 1 and output[0] > 0.5:
        #             bird.flap()
        #
        #         bird.update()
        #
        #         if bird.isDead(self.height, self.pipes):
        #             bird.alive = False
        #             self.alives -= 1
        #
        #             Neuvol.networkScore(network, self.score)
        #             if self.isItEnd():
        #                 self.start()

        # update pipes
        # for pipe in self.pipes:
        #     pipe.update()
        #     if pipe.isOut():
        #         self.pipes.remove(pipe)

        # not sure what it does ¯\_(ツ)_/¯
        # if self.interval == 0:
        #     deltaBord = 50
        #     pipeHoll = 120
        #     hollPosition = round(random.random() * \
        #             (self.height - deltaBord * 2 - pipeHoll)) + deltaBord
        #
        #     self.pipes.append(Pipe(x=self.width, y=0, height=hollPosition))
        #     self.pipes.append(Pipe(x=self.width, y=hollPosition+pipeHoll, height=self.height))
        #
        # self.interval += 1
        # if self.interval == self.spawnInterval:
        #     self.interval = 0

        # update score
        self.score += 1
        self.maxScore = self.score if self.score > self.maxScore else self.maxScore

    def isItEnd(self):
        for bird in self.birds:
            if not bird.isDead(config.cfg["window"]["height"], self.pipes):
                return False
        return True

    def drawScene(self):
        drawables = [self.background]

        for b in self.birds:
            drawables.append(b)

        for p in self.pipes:
            drawables.append(p)

        return drawables



    #Game.prototype.display = function(){
    #    self.ctx.clearRect(0, 0, self.width, self.height)
    #    for(var i = 0 i < Math.ceil(self.width / images.background.width) + 1 i++){
    #        self.ctx.drawImage(
    #            images.background,
    #            i * images.background.width - Math.floor(self.backgroundx%images.background.width),
    #            0)
    #    }
    #
    #    for(var i in self.pipes){
    #        if(i%2 == 0){
    #            self.ctx.drawImage(
    #                images.pipetop,
    #                self.pipes[i].x,
    #                self.pipes[i].y + self.pipes[i].height - images.pipetop.height,
    #                self.pipes[i].width, images.pipetop.height)
    #        }else{
    #            self.ctx.drawImage(
    #                images.pipebottom,
    #                self.pipes[i].x,
    #                self.pipes[i].y,
    #                self.pipes[i].width,
    #                images.pipetop.height)
    #        }
    #    }
    #
    #    self.ctx.fillStyle = "#FFC600"
    #    self.ctx.strokeStyle = "#CE9E00"
    #    for(var i in self.birds){
    #        if(self.birds[i].alive){
    #            self.ctx.save()
    #
    #            self.ctx.translate(
    #                self.birds[i].x + self.birds[i].width/2,
    #                self.birds[i].y + self.birds[i].height/2)
    #
    #            self.ctx.rotate(Math.PI/2 * self.birds[i].gravity/20)
    #
    #            self.ctx.drawImage(
    #                images.bird,
    #                -self.birds[i].width/2,
    #                -self.birds[i].height/2,
    #                self.birds[i].width,
    #                self.birds[i].height)
    #
    #            self.ctx.restore()
    #        }
    #    }
    #
    #    self.ctx.fillStyle = "white"
    #    self.ctx.font="20px Oswald, sans-serif"
    #    self.ctx.fillText("Score : "+ self.score, 10, 25)
    #    self.ctx.fillText("Max Score : "+self.maxScore, 10, 50)
    #    self.ctx.fillText("Generation : "+self.generation, 10, 75)
    #    self.ctx.fillText("Alive : "+self.alives+" / "+Neuvol.options.population, 10, 100)
    #
    #    var self = self
    #    requestAnimationFrame(function(){
    #        self.display()
    #    })
    #}
