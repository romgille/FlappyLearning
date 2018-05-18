#!/bin/python
import tkinter
import os, inspect
import time
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageTk
from PIL import ImageDraw

import Bird
import Pipe

class Display:
    WIDTH = 500
    HEIGHT = 512
    BLACK_COLOR = "#000000"
    WHITE_COLOR = "#FFFFFF"
    FONT = ImageFont.truetype(font="fonts/Roboto-Regular.ttf", size=30)
    XXX = 50
    YYY = 200

    def __init__(self):
        # Window
        self.window = tkinter.Tk()
        self.window.title("Flappy Learning")
        # Image
        self.buffer = Image.new("RGBA", (WIDTH, HEIGHT))

        # Background
        backgroundImage = Image.open("img/background.png").convert("RGBA")
        xBg, yBg = myBackgroundImage.size
        self.background = Image.new("RGBA", (WIDTH, HEIGHT))
        self.background.paste(backgroundImage, (xBg, 0, xBg*2, yBg), backgroundImage)
        self.background.paste(backgroundImage, (0, 0, xBg, yBg), backgroundImage)

    def draw(birds, pipes):
        # Draw the background
        draw = ImageDraw.Draw(buffer)
        # Canvas to draw
        canvas = tkinter.Canvas(self.window, width=WIDTH-1, height=HEIGHT-1, bg=BLACK_COLOR)
        img = tkinter.PhotoImage(width=WIDTH, height=HEIGHT)
        ECRAN = canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
        canvas.pack()

        draw.rectangle(((0,0), (WIDTH,HEIGHT)), fill=myBlackColor)
        buffer.paste(myBackground, (-yyy,0))
        buffer.paste(myBackground, (-yyy+WIDTH,0))

        # Draw birds
        for bird in birds:
            bird.draw(buffer)
        # Draw pipes
        for pipe in pipes:
            pipe.draw(buffer)

        # Draw text delta
        draw.text((30, 5),"delta: " + str(delta), font=FONT, fill=WHITE_COLOR)
        yyy = (yyy+4) % WIDTH

        # Transfert de la zone de dessin vers l'ecran
        photo = PIL.ImageTk.PhotoImage(buffer)
        canvas.itemconfig(ECRAN, image=photo)

        # Affichage
        canvas.update()

"""
# Window
window = tkinter.Tk()

# Image
WIDTH, HEIGHT = 500, 512
buffer = Image.new("RGBA", (WIDTH,HEIGHT))

# stuff
myfont = ImageFont.truetype(font="fonts/Roboto-Regular.ttf", size=30);
myBlackColor = "#000000"
myWhiteColor = "#FFFFFF"

# Background
myBackgroundImage = Image.open("img/background.png").convert("RGBA")
xBg, yBg = myBackgroundImage.size
myBackground = Image.new("RGBA", (WIDTH,HEIGHT))
myBackground.paste(myBackgroundImage, (xBg,0,xBg*2,yBg), myBackgroundImage)
myBackground.paste(myBackgroundImage, (0,0,xBg,yBg), myBackgroundImage)

# Draw the background
draw = ImageDraw.Draw(buffer)

# Bird
myBird = Bird.Bird()

# Pipe
myPipe = Pipe.Pipe()

# Canvas to draw
canvas = tkinter.Canvas(window, width=WIDTH-1, height=HEIGHT-1, bg=myBlackColor)
window.title("Flappy Learning")
img = tkinter.PhotoImage(width=WIDTH, height=HEIGHT)
ECRAN = canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
canvas.pack()
xxx = 50
yyy = 200

delta = 0
old_time = time.time()

while(True):
    draw.rectangle(((0,0), (WIDTH,HEIGHT)), fill=myBlackColor)
    buffer.paste(myBackground, (-yyy,0))
    buffer.paste(myBackground, (-yyy+WIDTH,0))
    myBird.draw(buffer)
    myPipe.draw(buffer)
    draw.text((30, 5),"delta: " + str(delta), font= myfont, fill=myWhiteColor)
    # draw.ellipse(((xxx,yyy), (xxx+20, yyy+20)), fill="blue")
    yyy = (yyy+4) % WIDTH

    # transfert de la zone de dessin vers l"ecran
    photo = PIL.ImageTk.PhotoImage(buffer)
    canvas.itemconfig(ECRAN, image=photo)

    # TODO: faire la synchronization dans game
    # synchronization at 60 fps
    t = time.time()
    delta = t - old_time
    old_time = t
    sync_time = 1./60 - delta
    if sync_time > 0:
       time.sleep(sync_time)

    # affichage
    canvas.update()

window.destroy()
"""