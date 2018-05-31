#!/bin/env python3

import time

import Game
import Display

display = Display.Display()
game = Game.Game()
game.start()

# sync stuff
delta = 0
old_time = time.time()

while not display.keypress_event:

    if game.isItEnd():
        game.start()

    game.update(delta)

    # draw the scene
    drawables = game.drawScene()
    display.drawthat(drawables)

    # synchronization at 60 fps
    t = time.time()
    delta = t - old_time
    old_time = t
    sync_time = 1./60 - delta
    if sync_time > 0:
       time.sleep(sync_time)

display.close()
