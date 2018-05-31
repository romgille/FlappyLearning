#!/bin/python

import tkinter
import PIL
from PIL import Image
from PIL import ImageTk
from PIL import ImageDraw

import config

class Display:
    def __init__(self):
        # Open a Window
        self.window = tkinter.Tk()
        self.window.title(config.cfg["window"]["title"])

        # Listening to keypress event
        self.keypress_event = False
        self.window.bind("<KeyPress>", self.keydown)

        # Prepare the Image Buffer
        self.buffer = Image.new("RGBA",
            (config.cfg["window"]["width"],config.cfg["window"]["height"]))

        # Prepare the Drawing Object
        self.draw = ImageDraw.Draw(self.buffer)

        # Prepare the Canvas
        self.canvas = tkinter.Canvas(self.window,
            width=config.cfg["window"]["width"] - 1,
            height=config.cfg["window"]["height"] - 1,
            bg=config.cfg["color"]["black"])
        self.img = tkinter.PhotoImage(width=config.cfg["window"]["width"],
            height=config.cfg["window"]["height"])
        self.screen = self.canvas.create_image(
            (config.cfg["window"]["width"]/2, config.cfg["window"]["height"]/2),
            image=self.img, state="normal")
        self.canvas.pack()

    def close(self):
        self.window.destroy()

    def drawthat(self, drawables):
        # Wipe the current image
        self.draw.rectangle(((0,0),
            (config.cfg["window"]["width"],config.cfg["window"]["height"])),
            fill=config.cfg["color"]["black"])

        # Draw
        for d in drawables:
            d.draw(self.buffer)

        # Update canvas with buffer
        photo = PIL.ImageTk.PhotoImage(self.buffer)
        self.canvas.itemconfig(self.screen, image=photo)
        self.canvas.update()

    # Handler for key press event
    def keydown(self, event):
        self.keypress_event = True
