from math import sqrt  
from tkinter import * 

from fractal_template import *

class Sierpinski(FractalTemplate):
    def __init__(self, canvas, xpos, ypos, size, depth, color, name = 'sierpinski triangle'):
        super().__init__(name, canvas, xpos, ypos, size, depth, color)
    
    def start_sierpinski(self): 
        self.draw_sierpinski(self.size, self.xpos, self.ypos, self.depth)
    
    def draw_sierpinski(self, new_size, new_xpos, new_ypos, depth):
        if depth < 1:   
            self.draw_triangle(new_size, new_xpos, new_ypos)
            self.draw_triangle(new_size, (new_xpos + new_size), new_ypos)
            self.draw_triangle(new_size, (new_xpos + new_size/2), (new_ypos - sqrt(pow(new_size, 2) - pow((new_size/2), 2))))
        else:
            self.draw_sierpinski((new_size/2), new_xpos, new_ypos, (depth - 1))
            self.draw_sierpinski((new_size/2), (new_xpos + new_size), new_ypos, (depth - 1))
            self.draw_sierpinski((new_size/2), (new_xpos + new_size/2), (new_ypos - sqrt(pow(new_size, 2) - pow((new_size/2),2))), (depth - 1))

    def draw_triangle(self, size, x1, y1):
        x2, y2 = (x1 + size), y1
        x3, y3 = (x1 + size/2), (y1 - sqrt((pow(size, 2) - pow((size/2), 2))))
        self.canvas.create_line(x1, y1, x2, y2, fill=self.color)
        self.canvas.create_line(x1, y1, x3, y3, fill=self.color)
        self.canvas.create_line(x2, y2, x3, y3, fill=self.color)