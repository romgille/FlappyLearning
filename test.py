#! /bin/python3

import time

import Background
import Display

d = Display.Display()
b = Background.Background()

# sync stuff
delta = 0
old_time = time.time()

while not d.keypress_event:

    # move the background
    b.update()

    # draw the scene
    d.drawthat([b])

    # synchronization at 60 fps
    t = time.time()
    delta = t - old_time
    old_time = t
    sync_time = 1./60 - delta
    if sync_time > 0:
       time.sleep(sync_time)

d.close()
