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
        self.canv.create_line(x0, y0, x1, y1, fill=self.colour)
    
    def distance(self, sx, sy, ex, ey):
        #uses distance formula
        return sqrt(pow(ex-sx, 2) + pow(ey-sy, 2))

    def draw_koch(self, sx, sy, ex, ey, angle, depth):
        px, py, qx, qy, rx, ry = 0, 0, 0, 0, 0, 0
        length = self.distance(sx, sy, ex, ey)/3
        
        if depth == 0:
            self.draw_line(sx, sy, ex, ey)
            return
        else:
            px = sx + length*cos(radians(angle))
            py = sy + length*sin(radians(angle+180))
            qx = px + length*cos(radians(angle+60))
            qy = py + length*sin(radians(angle+60+180))
            rx = qx + length*cos(radians(angle-60))
            ry = qy + length*sin(radians(angle-60+180))
            self.draw_koch(sx, sy, px, py, angle, depth-1)
            self.draw_koch(px, py, qx, qy, angle+60, depth-1)
            self.draw_koch(qx, qy, rx, ry, angle-60, depth-1)
            self.draw_koch(rx, ry, ex, ey, angle, depth-1)    

# for debugging
#if __name__ == "__main__":
    #koch = test_koch2(0, 0, 200, 500, 400, 0, "blue")
    #print(koch.draw_base())
