from tkinter import *
from math import *
# useful links: https://www.adrian.idv.hk/2017-12-20-koch/
#               https://www.youtube.com/watch?v=CjdxjepQYCU

class koch_snowflake:
    def __init__(self, canv, x, y, canv_width, canv_length, depth, colour):
        self.canv = canv
        self.x = x
        self.y = y
        self.canv_width = canv_width
        self.canv_length = canv_length
        self.colour = colour
        self.depth = depth

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



# # paraphrase this
    # def rotate_points_60(self, xa, ya, xb, yb, angle):
    #     # uses the rotation matrix to calculate the coordinates of the apex of the triangle which is xc, yc
    #     sine, cosine = sin(radians(angle)), cos(radians(angle))
    #     x_c = cosine*(xb-xa)-sine*(yb-ya) + xa
    #     y_c = sine*(xb-xa)+cosine*(yb-ya) + ya
    #     return x_c, y_c

    # def trisection(self, x_0, y_0, x_1, y_1):
    #     # calculating one third and 2 thirds of the line segment (x_a, y_a) and (x_b, y_b)
    #     x_a = (2*x_0)/3 + x_1/3
    #     y_a = (2*y_0)/3 + y_1/3
    #     x_b = x_0/3 + (2*x_1)/3
    #     y_b = y_0/3 + (2*y_1)/3
    #     return x_a, y_a, x_b, y_b

    # def draw_base(self):
    #     xa, ya, xb, yb = self.trisection(0, self.canv_length/2, 500, self.canv_length/2)
    #     xc, yc = self.rotate_points(xa, ya, xb, yb, 60)
    #     self.draw_line(0, 200, xa, ya)
    #     self.draw_line(xa, ya, xc, yc)
    #     self.draw_line(xc, yc, xb, yb)
    #     self.draw_line(xb, yb, 500, 200)
    #     self.draw_line(xb, yb, self.canv_width, self.y)
