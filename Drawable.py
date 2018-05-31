from PIL import Image

class Drawable(object):
    def __init__(self, x, y, path):
        self.x = x
        self.y = y
        self.path = path
        self.image = Image.open(self.path).convert("RGBA")

    def image_size(self):
        return self.image.size

    def image_width(self):
        return self.image_size()[0]

    def image_height(self):
        return self.image_size()[1]

    def draw(self, ctx):
        ctx.paste(self.image, (int(self.x), int(self.y)), self.image)
