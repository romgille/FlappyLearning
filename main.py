#!/bin/env python3

import time

import Background
import Bird
import Display

display = Display.Display()
bg = Background.Background()
birds = []

birds.append(Bird.Bird())

# sync stuff
delta = 0
old_time = time.time()

while not display.keypress_event:

    # move the background
    bg.update(delta)

    # move all elements to a single array of Drawables
    drawables = [bg]
    for b in birds:
        drawables.append(b)

    # draw the scene
    display.drawthat(drawables)

    # synchronization at 60 fps
    t = time.time()
    delta = t - old_time
    old_time = t
    sync_time = 1./60 - delta
    if sync_time > 0:
       time.sleep(sync_time)

display.close()
