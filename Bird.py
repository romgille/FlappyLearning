from math import pi as PI

import Drawable

class Bird(Drawable.Drawable):
    def __init__(self, x = 80, y = 250, width = 40, height = 30, alive = True,
            gravity = 0, velocity = 7, jump = -6):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.alive = alive
        self.gravity = gravity
        self.velocity = velocity
        self.jump = jump
        super().__init__(self.x, self.y, "img/bird.png")

    def flap(self):
        self.gravity = self.jump

    def update(self, deltaTime):
        self.gravity += self.velocity * deltaTime
        self.y += self.gravity

    def draw(self, ctx):
        # fix rotation computation
        # original : Math.PI/2 * self.gravity/20
        # + optional translate arg to recenter the image
        img = self.image.rotate(-PI * self.gravity * 2, expand=True)
        ctx.paste(img, (int(self.x), int(self.y)), img)

    # why never return false ?
    def isDead(self, height, pipes):
        if (self.y >= height) or (self.y <= - self.height):
            return true

        for pipe in pipes:
            if (self.x > pipe.x + pipe.width or self.x + self.width < pipe.x or
                self.y > pipe.y + pipe.height or self.y + self.height < pipe.y):
                    return true
