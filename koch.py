from tkinter import *
from math import *

# useful links: https://www.adrian.idv.hk/2017-12-20-koch/
#               https://www.youtube.com/watch?v=CjdxjepQYCU

#     def draw(self, size):
#         # calculating the coordinates of the apex of the triangle (x_c, y_c)
#         radian = 60*math.pi/180
#         nx = self.x + size*math.cos(radian)
#         ny = self.y + size*math.sin(radian)
#         self.draw_line(self.x, self.y, nx, ny)
#         nx, ny = self.x, self.y

# <------------------------------------------------------>

class koch_snowflake:
    def __init__(self, canv, x, y, canv_width, canv_length, depth, colour, width):
        self.canv = canv
        self.x = x
        self.y = y
        self.canv_width = canv_width
        self.canv_length = canv_length
        self.colour = colour
        self.depth = depth
        self.width = width

    def draw_line(self, x0, y0, x1, y1):
        self.canv.create_line(x0, y0, x1, y1, fill=self.colour, width=self.width)

    # paraphrase this
    def rotate_points_60(self, xa, ya, xb, yb, angle):
        # uses the rotation matrix to calculate the coordinates of the apex of the triangle which is xc, yc
        sin, cos = sin(radians(angle)), cos(radians(angle))
        x_c = cos*(xb-xa)-sin*(yb-ya) + xa
        y_c = sin*(xb-xa)+cos*(yb-ya) + ya
        return x_c, y_c

    def trisection(self, x_0, y_0, x_1, y_1):
        # calculating one third and 2 thirds of the line segment (x_a, y_a) and (x_b, y_b)
        x_a = (2*x_0)/3 + x_1/3
        y_a = (2*y_0)/3 + y_1/3
        x_b = x_0/3 + (2*x_1)/3
        y_b = y_0/3 + (2*y_1)/3
        return x_a, y_a, x_b, y_b

    def first_iter(self):
        xa, ya, xb, yb = self.trisection(self.x, self.canv_length/2, 500, self.canv_length/2)     
        xc, yc = self.rotate_points_60(xa, ya, xb, yb, -60)
        self.draw_line(self.x, self.y, xa, ya)
        self.draw_line(xa, ya, xc, yc)
        self.draw_line(xc, yc, xb, yb)
        self.draw_line(xb, yb, self.canv_width, self.y)

    def distance(self, sx, sy, ex, ey):
        #uses distance formula
        return sqrt(pow(ex-sx, 2) + pow(ey-sy, 2))

    def draw_koch(self, sx, sy, ex, ey, angle):
        px, py, qx, qy, rx, ry = 0, 0, 0, 0, 0, 0
        ncalls = 0
        ncalls += 1
        length = self.distance(sx, sy, ex, ey)/3
        if length < 1:
            self.draw_line(sx, sy, ex, ey)
            return
        else:
            px = sx + length*cos(radians(angle))
            py = sy + length*sin(radians(angle+180))
            qx = px + length*cos(radians(angle+60))
            qy = py + length*sin(radians(angle+60+180))
            rx = qx + length*cos(radians(angle-60))
            ry = qy + length*sin(radians(angle-60+180))
            self.draw_koch(sx, sy, px, py, angle)
            self.draw_koch(px, py, qx, qy, angle+60)
            self.draw_koch(qx, qy, rx, ry, angle-60)
            self.draw_koch(rx, ry, ex, ey, angle)
            
        

    #def koch(self, size):
        # base case
        #if self.depth == 0:
            #self.first_iter()
        # recursive case
        #else:

            

# for debugging
#if __name__ == "__main__":
    #koch = koch_snowflake(0, 0, 200, 500, 400, 0, "blue", 2)
    #koch.draw_koch(0, 200, 500, 200, 60)