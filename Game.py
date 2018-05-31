import random

import Background
import Bird
import config
import Pipe
import TextDrawer

class Game:
    def __init__(self):
        # game elements
        self.background = Background.Background()
        self.birds = []
        self.pipes = []
        self.pipe_cooldown = config.cfg['game']['pipe']['spawn-cooldown']

        # scoring
        self.score = 0
        self.score_max = 0
        self.score_text = TextDrawer.TextDrawer(30, 5)

        # Neurovol stuff
        self.gen = []
        self.generation = 0

    def start(self):
        # init birds
        self.birds = []
        for i in range(100):
            bird = Bird.Bird()
            bird.brain = lambda b: b.flap() if b.y > random.randint(350, 380) else None
            self.birds.append(bird)

        # init pipes
        self.pipes = []
        self.pipe_cooldown = config.cfg['game']['pipe']['spawn-cooldown']
        self.spawn_pipe()

        # init scoring
        self.score = 0

        # TODO: init Neurovol
        # self.gen = [] # need Nerovol implementaion #Neuvol.nextGeneration()
        #
        # for generation in self.gen:
        #     b = Bird.Bird()
        #     self.birds.append(b)
        #
        # self.generation += 1
        # self.alives = len(self.birds)
        for bird in self.birds:
            
    def spawn_pipe(self):
        hole_y = random.randint(config.cfg['game']['pipe']['hole-min'],
            config.cfg['game']['pipe']['hole-max'])
        self.pipes.append(Pipe.Pipe(hole_y))

    def increase_score(self):
        self.score += 1
        if self.score_max < self.score:
            self.score_max = self.score

    def isItEnd(self):
        return len(self.birds) == 0

    def update(self, deltaTime):
        # Nothing to do if all birds are dead
        if len(self.birds) == 0:
            return

        # Move the background
        self.background.update(deltaTime)

        # Find next holl
        nextHoll = 0
        for pipe in self.pipes:
            # find the first non-passed pipe
            if pipe.x + pipe.image_width() > self.birds[0].x:
                # compute the hole ratio
                nextHoll = pipe.hole_y / config.cfg["window"]["height"]
                break

        # Update birds
        for b in self.birds:
            b.update(deltaTime)
        # TODO: Neurovol Stuff should be moved to the Bird brain
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

        # Update pipes
        for pipe in self.pipes:
            pipe.update(deltaTime)

            # increase score
            if pipe.x + pipe.image_width() < self.birds[0].x and not pipe.passed:
                pipe.passed = True
                self.increase_score()

            # remove out of screen pipes
            if pipe.isOut():
                self.pipes.remove(pipe)

        # Spawn new pipes
        if self.pipe_cooldown <= 0:
            self.spawn_pipe()
            self.pipe_cooldown = config.cfg['game']['pipe']['spawn-cooldown']
        else:
            self.pipe_cooldown -= deltaTime

        # Check collisions between pipes and birds
        for bird in self.birds:
            if b.isDead(config.cfg["window"]["height"], self.pipes):
                self.birds.remove(bird)

        # Update text
        self.score_text.text = "Score: " + str(self.score) \
            + "\nMax: " + str(self.score_max) \
            + "\nAlive: " + str(len(self.birds))

    def drawScene(self):
        drawables = [self.background]

        for p in self.pipes:
            drawables.append(p)

        for b in self.birds:
            drawables.append(b)

        drawables.append(self.score_text)

        return drawables
