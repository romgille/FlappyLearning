import Drawable

class Pipe(Drawable.Drawable):
    def __init__(self, x = None, y = None, width = None, height = None, speed = None):
        self.x = x or 0
        self.y = y or 0
        self.width = width or 50
        self.height = height or 40
        self.speed = height or 3
        super().__init__(self.x, self.y, "img/pipetop.png")

    def update(self):
        self.x -= self.speed

    def isOut(self):
        return self.x < - self.width
