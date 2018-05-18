import Drawable

class Pipe(Drawable.Drawable):
    def __init__(self, x = 0, y = 0, width = 50, height = 40, speed = 3):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = height
        super().__init__(self.x, self.y, "img/pipetop.png")

    def update(self):
        self.x -= self.speed

    def isOut(self):
        return self.x < - self.width
