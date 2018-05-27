from PIL import Image

import Drawable
import config

class Pipe(Drawable.Drawable):
    def __init__(self, hole_position=(config.cfg["window"]["height"] / 2),
        hole_height=(config.cfg["game"]["pipe"]["hole-height"])):
        self.x = config.cfg["window"]["width"]
        self.y = 0
        self.speed = config.cfg["game"]["pipe"]["speed"]
        self.hole_y = hole_position
        self.hole_height = hole_height
        self.passed = False
        super().__init__(self.x, self.y, config.cfg["img"]["pipe-top"])
        self.image2 = Image.open(config.cfg["img"]["pipe-bottom"]).convert("RGBA")

        # Position pipes on the image
        self.top_sprite = self.image.crop((0, int(self.image_height() - self.hole_y), self.image_width(), self.image_height()))
        self.bottom_sprite = self.image2.crop((0, 0, self.image_width(), int(config.cfg["window"]["height"] - self.hole_y - self.hole_height)))
        self.sprite = Image.new("RGBA", self.image_size())
        self.sprite.paste(self.top_sprite, (0, 0, self.image_width(), int(self.hole_y)), self.top_sprite)
        self.sprite.paste(self.bottom_sprite, (0, int(self.hole_y + self.hole_height), self.image_width(), config.cfg["window"]["height"]), self.bottom_sprite)

    def update(self, deltaTime):
        # move to the left
        self.x -= (self.speed * deltaTime)

    def draw(self, ctx):
        ctx.paste(self.sprite, (int(self.x), int(self.y)), self.sprite)

    def isOut(self):
        return self.x < -self.image_width()
