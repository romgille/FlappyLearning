import Drawable

class Bird(Drawable.Drawable):
    def __init__(self, x = None, y = None, width = None, height = None,
            alive = None, gravity = None, velocity = None, jump = None):
        self.x = x or 80;
        self.y = y or 250;
        self.width = width or 40;
        self.height = height or 30;
        self.alive = alive or True;
        self.gravity = gravity or 0;
        self.velocity = velocity or 0.3;
        self.jump = jump or -6;
        super().__init__(self.x, self.y, "img/bird.png")

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
