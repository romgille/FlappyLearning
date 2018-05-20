from PIL import Image

import config
import Drawable

# More fucking const
WIDTH = 500
HEIGHT = 512

class Background(Drawable.Drawable):
    def __init__(self, x = 0, y = 0, width = 50, height = 40, speed = 3):
        self.x = 0
        self.y = 0
        self.width = config.cfg["window"]["width"]
        self.height = config.cfg["window"]["height"]
        self.speed = 4
        super().__init__(self.x, self.y, config.cfg["img"]["background"])

        # Make background wider than screen size
        # here, background is 1/2 the width of the screen
        # so we use 3 image side by side to create an infinite scrolling effet
        xBg, yBg = self.image_size()
        self.background = Image.new("RGBA", (xBg*3, config.cfg["window"]["height"]))
        self.background.paste(self.image, (xBg*2, 0, xBg*3, yBg), self.image)
        self.background.paste(self.image, (xBg, 0, xBg*2, yBg), self.image)
        self.background.paste(self.image, (0, 0, xBg, yBg), self.image)

    def update(self):
        self.x = (self.x + self.speed) % self.image_width()

    def draw(self, ctx):
        ctx.paste(self.background, (-self.x, self.y), self.background)
