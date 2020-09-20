# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 23:41:41 2018
ML with interface
@author: Turnphy
"""

import tkinter as tk
from PIL import Image

canvas_width=600
canvas_height=450

def paint(event):
    color='red'
    x1,y1=(event.x-1), (event.y-1)
    x2,y2=(event.x+1), (event.y+1)
    c.create_oval(x1,y1,x2,y2, fill=color, outline=color)


root = tk.Tk()
root.title('Tkpainter')
c=tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
c.pack(expand='YES', fill='both' )
c.bind('<B1-Motion>', paint)


message=tk.Label(root, text='Press and drag to draw')
message.pack(side='bottom')
# save canvas to .eps (postscript) file
c.postscript(file="tmp_canvas.eps", colormode="color",\
                  width=canvas_width,height=canvas_height,\
                  pagewidth=canvas_width-1,\
                  pageheight=canvas_height-1)
pic = Image.open("tmp_canvas.eps")
pic.show()
# mpimg.imsave("canvas_image.png", data)
root.mainloop()