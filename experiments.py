from tkinter import *
from koch import *

mainwindow = Tk()
mainwindow.title("Fractal Art")
mainwindow.attributes("-fullscreen", True)
mainwindow.configure(background="#FFD700")

fractal_canvas = Canvas(mainwindow, bg="white", height=400, width=500)
fractal_canvas.pack()

koch = test_koch2(fractal_canvas, 0, 200, 500, 400, 2, "black")
koch.draw_base()

#link https://mathworld.wolfram.com/LindenmayerSystem.html

#koch l system
#axiom  = F
#rules = F -> F+F-F+F

#class koch:
   # def __init__(self, canvas, size, x, y, depth, colour):
        #self.canvas = canvas
        #self.size = size
        # self.x = x
        # self.y = y
        # self.depth = depth
        # self.colour = colour
   #def start_koch(self):
        #self.canvas.create_line(x, y, y)
    
    #def draw_koch(self):
        

    #def draw_line(self):





mainwindow.mainloop()