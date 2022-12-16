from sierpinski import *
from koch import *
from box import *
from json import dumps as dump
from tkinter import *

class Controller: 
    def __init__(self, canvas, frame, fractals, max_fractals = 5, max_depth=6):
        self.canvas = canvas
        self.frame = frame
        self.fractals = fractals
        self.max_fractals = max_fractals
        self.max_depth = max_depth
        self.selected_fractal = 0
        
        self.size_slider = Scale(self.frame, from_=10, to=500, length=250, bg="#2E2252", 
        fg="white", orient=HORIZONTAL, command=self.change_size)
        self.size_slider.pack()

        self.menu_container = Frame(self.frame, height=500, width=250, bg='white', 
        highlightthickness = 10, highlightbackground="#FFD700")
        self.menu_container.pack_propagate(False)
        self.menu_container.place(x=955, y=100)

    def select_next(self):
        if self.selected_fractal < (len(self.fractals) - 1):    
            self.selected_fractal += 1
            self.fractals[self.selected_fractal].update_menu_item()
            self.size_slider.set(self.fractals[self.selected_fractal].size)
    
    def select_previous(self):
        if self.selected_fractal > 0:
            self.selected_fractal -= 1
            self.fractals[self.selected_fractal].update_menu_item()
            self.size_slider.set(self.fractals[self.selected_fractal].size)
    
    def increase_depth(self):
        if self.fractals[self.selected_fractal].depth < self.max_depth:
            self.fractals[self.selected_fractal].depth += 1
            self.draw_fractals()
            self.fractals[self.selected_fractal].update_menu_item()

    def decrease_depth(self):
        if self.fractals[self.selected_fractal].depth > 0:
            self.fractals[self.selected_fractal].depth -= 1
            self.draw_fractals()
            self.fractals[self.selected_fractal].update_menu_item()

    def change_size(self, val):
        self.fractals[self.selected_fractal].size = self.size_slider.get()
        self.draw_fractals()
        self.fractals[self.selected_fractal].update_menu_item()

    def create_sierpinski_triangle(self):
        if len(self.fractals) < self.max_fractals:
            new_sierpinski = Sierpinski(self.canvas, 150, 400, 100, 0, 'black')
            self.fractals.append(new_sierpinski)
            self.draw_fractals()
            new_sierpinski.create_menu_item(self.menu_container)
    
    def create_koch_snowflake(self):
        if len(self.fractals) < self.max_fractals:
            new_koch = Koch_Snowflake(self.canvas, 0, 200, 5, 0, "black")
            self.fractals.append(new_koch)
            self.draw_fractals()
            new_koch.create_menu_item(self.menu_container)

    def create_box(self):
        if len(self.fractals) < self.max_fractals:
            new_box = Box(self.canvas, 150, 150, 5, 0, "white")
            self.fractals.append(new_box)
            self.draw_fractals()
            new_box.create_menu_item(self.menu_container)

    def draw_fractals(self):
        self.canvas.delete('all') #clears canvas for re-draw
        for fractal in self.fractals:# goes through list of all created fractals and chechs which one it is 
            if fractal.name == 'sierpinski triangle':
                 fractal.start_sierpinski() #draws sierpinski
            if fractal.name == 'koch snowflake':
                fractal.start_koch() #draws koch
            if fractal.name == 'box':
                fractal.start_box() #draws vicsek/box fractal
    
    def save_canvas(self):
        saved_data = []
        for fractal in self.fractals:
            saved_data.append(fractal.get_save_data())    
        json_controller = dump(saved_data)
        with open('save_states/save_file.json', 'w') as json_file:
            json_file.write(json_controller)
    
    
        
