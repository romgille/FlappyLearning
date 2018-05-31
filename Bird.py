from math import pi as PI

import config
import Drawable
import Neuroevolution

class Bird(Drawable.Drawable):
    def __init__(self, x = 80, y = 250, width = 40, height = 30,
            gravity = 0, velocity = 10, jump = -4.5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.gravity = gravity
        self.velocity = velocity
        self.jump = jump
        self.brain = lambda: None
        self.neuron = Neuroevolution.Neuroevolution()
        self.neuron.generateNetwork()
        self.neuron.mutation()

        super().__init__(self.x, self.y, config.cfg["img"]["bird"])

    def flap(self):
        self.gravity = self.jump

    def update(self, deltaTime):
        self.gravity += self.velocity * deltaTime
        self.y += self.gravity

        # use your brain to survive !
        self.brain(self)

    def draw(self, ctx):
        # fix rotation computation
        # original : Math.PI/2 * self.gravity/20
        # + optional translate arg to recenter the image
        img = self.image.rotate(-PI * self.gravity * 2, expand=True)
        ctx.paste(img, (int(self.x), int(self.y)), img)

    # move this to Game ?
    def isDead(self, height, pipes):
        # out of the screen
        if (self.y >= height) or (self.y <= - self.height):
            return True

        # Collided with pipes
        for pipe in pipes:
            if not (self.x + self.image_width() > pipe.x and self.x < pipe.x + pipe.image_width()):
                continue
            if self.y < pipe.hole_y or self.y + self.image_height() > pipe.hole_y + pipe.hole_size:
                return True

        return False
