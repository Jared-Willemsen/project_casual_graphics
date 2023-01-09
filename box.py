from tkinter import *
from fractal_template import FractalTemplate

class Box(FractalTemplate):

    def start_box(self):
        self.clear_fractal_from_canvas()
        self.draw_box(self.xpos, self.ypos, self.depth, self.size)

    def draw_box(self, x_1, y_1, depth, size):
        #base case
        if depth==0:
            self.draw_rect(x_1 + size, y_1, x_1 + 2*size, y_1 + size) # right rectangle
            self.draw_rect(x_1, y_1 + size, x_1 + size, y_1 + 2*size) # buttom rectangle
            self.draw_rect(x_1 - size, y_1, x_1 + size, y_1 + size) # left rectangle
            self.draw_rect(x_1, y_1 - size, x_1 + size, y_1 + size) # top rectangle
            self.draw_rect(x_1, y_1, x_1 + size, y_1 + size) # center rectangle
        #recursive case finds the coordinates of the intermediate points (one third and two thirds of the line)
        else:
            self.draw_box(x_1, y_1, depth-1, size/3)
            self.draw_box(x_1 + size, y_1, depth-1, size/3)
            self.draw_box(x_1, y_1 + size, depth-1, size/3)
            self.draw_box(x_1 - size, y_1, depth-1, size/3)
            self.draw_box(x_1, y_1 - size, depth-1, size/3)

    def draw_rect(self, x0, y0, x_1, y_1):
        self.lines.append(self.canvas.create_rectangle(x0, y0, x_1, y_1, fill=self.color, outline="black"))
    

 

            

    

    

    

    