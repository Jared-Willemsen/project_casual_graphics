from sierpinski import *
import tkinter

class Controller: 
    def __init__(self, canvas, frame, fractals, max_fractals):
        self.canvas = canvas
        self.frame = frame
        self.fractals = fractals
        self.max_fractals = max_fractals
        self.selected_fractal = 0
        
        self.menu_container = Frame(self.frame, height=500, width=250, bg='white', 
        highlightthickness = 10, highlightbackground="#ef2f2f")
        self.menu_container.pack_propagate(False)
        self.menu_container.place(x=900, y=100)

    def select_next(self):
        if self.selected_fractal < (len(self.fractals) - 1):    
            self.selected_fractal += 1
            self.fractals[self.selected_fractal].update_menu_item()
    
    def select_previous(self):
        if self.selected_fractal > 0:
            self.selected_fractal -= 1
            self.fractals[self.selected_fractal].update_menu_item()
    
    def increase_size(self):
        self.fractals[self.selected_fractal].size += 10
        self.draw_fractals()
        self.fractals[self.selected_fractal].update_menu_item()

    def decrease_size(self):
        if self.fractals[self.selected_fractal].size > 10:
            self.fractals[self.selected_fractal].size -= 10
            self.draw_fractals()
            self.fractals[self.selected_fractal].update_menu_item()
        
    def create_sierpinski(self):
        if len(self.fractals) < self.max_fractals:
            new_sierpinski = Sierpinski(self.canvas, 0, 400, 100, 0, 'black')
            self.fractals.append(new_sierpinski)
            self.draw_fractals()
            new_sierpinski.create_menu_item(self.menu_container)

    def draw_fractals(self):
        self.canvas.delete('all')
        for fractal in self.fractals:
            if fractal.name == 'sierpinski triangle':
                 fractal.start_sierpinski()
    
        
