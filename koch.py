from tkinter import *
from math import *

from fractal_template import *

# useful links: https://www.adrian.idv.hk/2017-12-20-koch/
#               https://www.youtube.com/watch?v=CjdxjepQYCU
# https://craftofcoding.wordpress.com/2019/11/19/recursive-patterns-the-koch-curve-i/
# https://craftofcoding.wordpress.com/2019/11/26/recursive-patterns-the-koch-curve-ii/

class Koch_Snowflake(FractalTemplate):

    def draw_line(self, x_0, y_0, x_1, y_1):
        self.lines.append(self.canvas.create_line(x_0, y_0, x_1, y_1, fill=self.color))
    
    def distance(self, s_x, s_y, e_x, e_y):
        #calculates distance between the starting and end points
        return sqrt(pow(e_x-s_x, 2) + pow(e_y-s_y, 2))

    def start_koch(self):
        self.clear_fractal_from_canvas()
        self.draw_koch(self.xpos, self.ypos, 500, 200, 0, self.depth)

    def draw_koch(self, s_x, s_y, e_x, e_y, ang, depth):
        p_x, p_y, q_x, q_y, r_x, r_y = 0, 0, 0, 0, 0, 0
        length = self.distance(s_x, s_y, e_x, e_y)/3
        
        #base case
        if depth == 0:
            self.draw_line(s_x, s_y, e_x, e_y)
            return
        #recursive case
        else:
            #calculates coordinates using formula
            p_x = s_x + length * cos(radians(ang))
            p_y = s_y + length * sin(radians(ang+180))
            q_x = p_x + length * cos(radians(ang+60))
            q_y = p_y + length * sin(radians(ang+60+180))
            r_x = q_x + length * cos(radians(ang-60))
            r_y = q_y + length * sin(radians(ang-60+180))
            #recursive calls that will 
            self.draw_koch(s_x, s_y, p_x, p_y, ang, depth-1)
            self.draw_koch(p_x, p_y, q_x, q_y, ang+60, depth-1)
            self.draw_koch(q_x, q_y, r_x, r_y, ang-60, depth-1)
            self.draw_koch(r_x, r_y, e_x, e_y, ang, depth-1)    

# for debugging
#if __name__ == "__main__":
    #koch = test_koch2(0, 0, 200, 500, 400, 0, "blue")
    #print(koch.draw_base())
