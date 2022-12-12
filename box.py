from tkinter import *

class Box:
    def __init__(self, canv, x, y, depth, color):
        self.canv = canv
        self.x = x
        self.y = y
        self.color = color
        self.depth = depth
    
    def start_box(self):
        self.draw_box()

    def draw_box(self, x0, y0, x1, y1):
        self.canv.create_rectangle(x0, y0, x1, y1, fill=self.color, outline="black")

    

    

    

    