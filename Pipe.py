from PIL import Image

import Drawable
import config

class Pipe(Drawable.Drawable):
    def __init__(self, hole_y=(config.cfg["window"]["height"] / 2),
        hole_size=config.cfg["game"]["pipe"]["hole-size"],
        speed=config.cfg["game"]["pipe"]["speed"]):

        # init attributes
        self.x = config.cfg["window"]["width"]
        self.y = 0
        self.speed = speed
        self.hole_y = hole_y
        self.hole_size = hole_size
        self.passed = False

        if self.hole_y + self.hole_size >  config.cfg["window"]["height"]:
            raise ValueError("Hole isn't suitable")

        # Load images
        self.image_top = Image.open(config.cfg["img"]["pipe-top"]).convert("RGBA")
        self.image_bottom = Image.open(config.cfg["img"]["pipe-bottom"]).convert("RGBA")

        w, h = self.image_top.size

        # Crop them according to hole position and height
        self.top_sprite = self.image_top.crop((0, int(h - self.hole_y), w, h))
        self.bottom_sprite = self.image_bottom.crop((0, 0, w, int(config.cfg["window"]["height"] - self.hole_y - self.hole_size)))

        # Position pipes on the image
        # (call the attribute "image" to be compliant with Drawable definition)
        self.image = Image.new("RGBA", (w, h))
        self.image.paste(self.top_sprite, (0, 0, w, int(self.hole_y)), self.top_sprite)
        self.image.paste(self.bottom_sprite, (0, int(self.hole_y + self.hole_size), w, config.cfg["window"]["height"]), self.bottom_sprite)

    def update(self, deltaTime):
        # move to the left
        self.x -= (self.speed * deltaTime)

    def isOut(self):
        return self.x < -self.image_width()
