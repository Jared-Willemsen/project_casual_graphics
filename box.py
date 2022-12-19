from tkinter import *
from fractal_template import *

class Box(FractalTemplate):

    def __init__(self, canvas, xpos, ypos, size, depth, color, is_selected, name="Vicsek"):
        super().__init__(name, canvas, xpos, ypos, size, depth, color, is_selected)

    def start_box(self):
        self.draw_box(self.xpos, self.ypos, self.depth, self.size)

    def draw_box(self, x_1, y_1, depth, size):
        #base case
        if depth==0:
            self.draw_rect(x_1 + size, y_1, x_1 + 2*size, y_1 + size) # right rectangle
            self.draw_rect(x_1, y_1 + size, x_1 + size, y_1 + 2*size) # buttom rectangle
            self.draw_rect(x_1 - size, y_1, x_1 + size, y_1 + size) # left rectangle
            self.draw_rect(x_1, y_1 - size, x_1 + size, y_1 + size) # top rectangle
            self.draw_rect(x_1, y_1, x_1 + size, y_1 + size) # center rectangle
            return
        #recursive case finds the coordinates of the intermediate points (one third and two thirds of the line)
        else:
            self.draw_box(x_1, y_1, depth-1, size/3)
            self.draw_box(x_1 + size, y_1, depth-1, size/3)
            self.draw_box(x_1, y_1 + size, depth-1, size/3)
            self.draw_box(x_1 - size, y_1, depth-1, size/3)
            self.draw_box(x_1, y_1 - size, depth-1, size/3)

    def draw_rect(self, x0, y0, x_1, y_1):
        self.canvas.create_rectangle(x0, y0, x_1, y_1, fill=self.color, outline="black")
    

    # def draw_fractal(self, x, y, width, height):
    #     if width < 5 or height < 5:
    #         return
        
    #     # Calculate the coordinates of the four smaller boxes
    #     x1 = x + width / 3
    #     y1 = y + height / 3
    #     x_2 = x + (width / 3) * 2
    #     y_2 = y + (height / 3) * 2
        
    #     # Draw the four smaller boxes
    #     self.draw_rectangle(x1, y, x_2, y1)
    #     self.draw_rectangle(x1, y_2, x_2, y)
    #     self.draw_rectangle(x, y1, x1, y_2)
    #     self.draw_rectangle(x_2, y1, x, y_2)
        
    #     # Recursively draw the smaller boxes
    #     self.draw_fractal(x1, y1, width / 3, height / 3)
    #     self.draw_fractal(x1, y_2, width / 3, height / 3)
    #     self.draw_fractal(x_2, y1, width / 3, height / 3)
    #     self.draw_fractal(x_2, y_2, width / 3, height / 3)

            

    

    

    

    