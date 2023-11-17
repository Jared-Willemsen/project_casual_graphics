from tkinter import *
from fractal_template import FractalTemplate

class Box(FractalTemplate):

    def start_box(self):
        self.clear_fractal_from_canvas()
        self.draw_box(self.xpos, self.ypos, self.depth, self.size)

    def draw_box(self, x_1, y_1, depth, size):
        if depth==0: #draw
            self.draw_rect(x_1 + size, y_1, x_1 + 2*size, y_1 + size) 
            self.draw_rect(x_1, y_1 + size, x_1 + size, y_1 + 2*size) 
            self.draw_rect(x_1 - size, y_1, x_1 + size, y_1 + size) 
            self.draw_rect(x_1, y_1 - size, x_1 + size, y_1 + size) 
            self.draw_rect(x_1, y_1, x_1 + size, y_1 + size) 
        else: #recursive case
            self.draw_box(x_1, y_1, depth-1, size/3)
            self.draw_box(x_1 + size, y_1, depth-1, size/3)
            self.draw_box(x_1, y_1 + size, depth-1, size/3)
            self.draw_box(x_1 - size, y_1, depth-1, size/3)
            self.draw_box(x_1, y_1 - size, depth-1, size/3)

    def draw_rect(self, x0, y0, x_1, y_1):
        self.lines.append(self.canvas.create_rectangle(x0, y0, x_1, y_1, fill=self.color, outline="black"))
    

 

            

    

    

    

    