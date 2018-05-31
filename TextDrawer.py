from PIL import ImageDraw
from PIL import ImageFont

import config
import Drawable

class TextDrawer(Drawable.Drawable):
    def __init__(self, x, y, text=""):
        self.x = x
        self.y = y
        self.text = text
        self.font = ImageFont.truetype(font=config.cfg["default-font"]["path"],
            size=config.cfg["default-font"]["size"])
        self.color = config.cfg["color"]["white"]

    # dumps functions from Drawable
    def image_size(self):
        return (0,0)
    def image_width(self):
        return 0
    def image_height(self):
        return 0

    def draw(self, ctx):
        draw = ImageDraw.Draw(ctx)
        draw.text((self.x, self.y), self.text, font=self.font, fill=self.color)
