from tkinter import *
import math
import numpy

# useful links: https://www.adrian.idv.hk/2017-12-20-koch/
#              https://www.youtube.com/watch?v=CjdxjepQYCU


class test_koch1:
    def __init__(self, fractal_canvas, x, y, size, colour, depth):
        # initializating all the variables
        self.fractal_canvas = fractal_canvas
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
        self.depth = depth

    def draw_line(self, x0, y0, x1, y1):
        self.fractal_canvas.create_line(x0, y0, x1, y1, fill=self.colour)

    def turn_by_deg(self, angle):
        a += angle

    def draw(self, size):
        # calculating the coordinates of the apex of the triangle (x_c, y_c)
        radian = 60*math.pi/180
        nx = self.x + size*math.cos(radian)
        ny = self.y + size*math.sin(radian)
        self.draw_line(self.x, self.y, nx, ny)
        nx, ny = self.x, self.y

    # def koch(self):
        # base case
        # if self.depth == 0:

        # recursive case
        # else:

    def trisection(self, x_0, y_0, x_1, y_1):
        # calculating one third and 2 thirds of the line segment (x_a, y_a) and (x_b, y_b)
        x_a = (2*x_0)/3 + x_1/3
        y_a = (2*y_0)/3 + y_1/3
        x_b = x_0/3 + (2*x_1)/3
        y_b = y_0/3 + (2*y_1)/3
        return x_a, y_a, x_b, y_b


# <------------------------------------------------------>

    
class test_koch2:
    def __init__(self, canv, x, y, canv_width, canv_length):
        self.canv = canv
        self.x = x
        self.y = y
        self.a = 0
        self.canv_width = canv_width
        self.canv_length = canv_length

    def draw_line(self, x0, y0, x1, y1):
        self.fractal_canvas.create_line(x0, y0, x1, y1, fill=self.colour)

    def turn(self, angle):
        # turns the angle passed in
        self.a += angle
        return self.a

    def rotate_(self, angle, size):
        # https://danceswithcode.net/engineeringnotes/rotations_in_2d/rotations_in_2d.html
        nx = self.x + size*math.cos(math.radians(angle))
        ny = self.y + size*math.sin(math.radians(angle))
        self.canv.create_line(self.x, self.y, nx, ny)
        self.x = nx
        self.y = ny

    def rotate(self, ox, oy, point, angle):
        px, py = point
        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        self.canv.create_line(ox, oy, qx, qy)

    def trisection(self, x_0, y_0, x_1, y_1):
        # calculating one third and 2 thirds of the line segment (x_a, y_a) and (x_b, y_b)
        x_a = (2*x_0)/3 + x_1/3
        y_a = (2*y_0)/3 + y_1/3
        x_b = x_0/3 + (2*x_1)/3
        y_b = y_0/3 + (2*y_1)/3
        return x_a, y_a, x_b, y_b

    # def koch(self, n, size):
        # if n == 0:
        #self.draw_line(0, (self.canv_width))
        # return
        # else:
        #a, b = self.trisection(0, self.canv_length/2, self.canv_width, self.canv_length/2)
        #rotate = rotate(a, b, 60)
        #self.koch(n-1, size/3)

    def draw_base(self):
        xa, ya, xb, yb = self.trisection(0, self.canv_length/2, 0, self.canv_length/2)
        self.draw_line(0, self.canv_length/2, xa, ya)
        self.draw_line(xa, ya, xb, yb)

# for debugging
if "__name__" == "__main__":
    koch = test_koch2
    koch.draw_base()
