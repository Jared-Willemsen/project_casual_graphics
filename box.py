from tkinter import *

class box:
    def __init__(self, canv, x, y, depth, color):
        self.canv = canv
        self.x = x
        self.y = y
        self.color = color
        self.depth = depth
    
    def draw_box(self, x0, y0, x1, y1):
        self.create_rectangle(x0, y0, x1, y1, fill=self.color)

    

    

    