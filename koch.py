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
        self.width = width

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
