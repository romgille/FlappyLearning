import config
import Drawable

class Bird(Drawable.Drawable):
    def __init__(self, x = 80, y = 250, width = 40, height = 30, alive = True,
            gravity = 0, velocity = 0.3, jump = -6):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.alive = alive
        self.gravity = gravity
        self.velocity = velocity
        self.jump = jump
        super().__init__(self.x, self.y, config.cfg["img"]["bird"])

    def flap(self):
        self.gravity = self.jump

    def update(self):
        self.gravity += self.velocity
        self.y += self.gravity

    # why never return false ?
    def isDead(self, height, pipes):
        if (self.y >= height) or (self.y <= - self.height):
            return true

        for pipe in pipes:
            if (self.x > pipe.x + pipe.width or self.x + self.width < pipe.x or
                self.y > pipe.y + pipe.height or self.y + self.height < pipe.y):
                    return true
