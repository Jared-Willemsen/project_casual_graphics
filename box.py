from tkinter import *
from fractal_template import *

class Box(FractalTemplate):

    def __init__(self, canvas, xpos, ypos, size, depth, color, name="box"):
        super().__init__(name, canvas, xpos, ypos, size, depth, color)

    def start_box(self):
        self.draw_box(self.xpos, self.ypos, 350, 350, self.depth)

    def draw_box(self, x_1,y_1,x_2,y_2,depth):
        #base case
        if depth==0:
            self.draw_rect(x_1, y_1, x_2, y_2)
            return
        #recursive case finds the coordinates of the intermediate points (one third and two thirds of the line)
        else:
            l_x1=x_1 + (x_2-x_1)/3
            l_x2=x_1 + 2 * (x_2-x_1)/3
            l_y1=y_1 + (y_2-y_1)/3
            l_y2=y_1 + 2 * (y_2-y_1)/3

            self.draw_rect(x_1,y_1,l_x1,l_y1)
            self.draw_rect(l_x2,y_1,x_2,l_y1)
            self.draw_rect(x_1,l_y2,l_x1,y_2)
            self.draw_rect(l_x2,l_y2,x_2,y_2)

            self.draw_box(l_x1,y_1,l_x2,l_y1,depth-1)
            self.draw_box(x_1,l_y1,l_x1,l_y2,depth-1)
            self.draw_box(l_x1,l_y1,l_x2,l_y2,depth-1)
            self.draw_box(l_x2,l_y1,x_2,l_y2,depth-1)
            self.draw_box(l_x1,l_y2,l_x2,y_2,depth-1)

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

            

    

    

    

    