import tkinter
import os, inspect
import time
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageTk
from PIL import ImageDraw

myfont = ImageFont.truetype(font='arial.ttf', size=30);

window = tkinter.Tk()
WIDTH, HEIGHT = 640, 480
buffer = Image.new('RGBA', (WIDTH,HEIGHT))
draw = ImageDraw.Draw(buffer)


canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
window.title('Mon Super Jeu')
img = tkinter.PhotoImage(width=WIDTH, height=HEIGHT)
ECRAN = canvas.create_image((WIDTH/2, HEIGHT/2), image = img, state="normal" )
canvas.pack()



xxx = 200
yyy = 0


while(True):
    timestart = time.time()

    ##################################################################

    #  zone a modifier

    draw.rectangle(((0,0),(500,500)), fill="black")
    draw.ellipse(((xxx, yyy), (xxx+20, yyy+20)), fill="blue")
    draw.text((30, 5),"Bonjour", font= myfont, fill=(255,0,0))
    yyy = (yyy+4)%500;


    ##################################################################
    #  gestion des FPS et de l'affiche écran | ne pas toucher

    # transfert de la zone de dessin vers l'ecran
    photo = PIL.ImageTk.PhotoImage(buffer)
    canvas.itemconfig(ECRAN, image = photo)

    # synchronisation a 20 fps
    timeend = time.time()
    delta = timeend-timestart - 1/20
    if ( delta > 0 ):
       time.sleep(delta)
    #affichage
    canvas.update()



window.destroy()
