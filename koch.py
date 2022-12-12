from tkinter import *
from math import *

# useful links: https://www.adrian.idv.hk/2017-12-20-koch/
#               https://www.youtube.com/watch?v=CjdxjepQYCU
# https://craftofcoding.wordpress.com/2019/11/19/recursive-patterns-the-koch-curve-i/
# https://craftofcoding.wordpress.com/2019/11/26/recursive-patterns-the-koch-curve-ii/

class koch_snowflake:
    def __init__(self, canv, x, y, depth, color):
        self.canv = canv
        self.x = x
        self.y = y
        self.color = color
        self.depth = depth

    def draw_line(self, x0, y0, x1, y1):
        self.canv.create_line(x0, y0, x1, y1, fill=self.color)
    
    def distance(self, s_x, s_y, e_x, e_y):
        #uses distance formula
        return sqrt(pow(e_x-s_x, 2) + pow(e_y-s_y, 2))

    def draw_koch(self, s_x, s_y, e_x, e_y, angle, depth):

        p_x, p_y, q_x, q_y, r_x, r_y = 0, 0, 0, 0, 0, 0
        length = self.distance(s_x, s_y, e_x, e_y)/3
        
        if depth == 0:
            self.draw_line(s_x, s_y, e_x, e_y)
            return
        else:
            p_x = s_x + length*cos(radians(angle))
            p_y = s_y + length*sin(radians(angle+180))
            q_x = p_x + length*cos(radians(angle+60))
            q_y = p_y + length*sin(radians(angle+60+180))
            r_x = q_x + length*cos(radians(angle-60))
            r_y = q_y + length*sin(radians(angle-60+180))
            self.draw_koch(s_x, s_y, p_x, p_y, angle, depth-1)
            self.draw_koch(p_x, p_y, q_x, q_y, angle+60, depth-1)
            self.draw_koch(q_x, q_y, r_x, r_y, angle-60, depth-1)
            self.draw_koch(r_x, r_y, e_x, e_y, angle, depth-1)    

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
