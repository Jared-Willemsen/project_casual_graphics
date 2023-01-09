from os import listdir, remove
from json import load
from time import sleep
from tkinter import *

from sierpinski import Sierpinski
from koch import Koch_Snowflake
from box import Box

class Gallery:
    def __init__(self, frame, canvas, painting_label, mainwindow):
        self.frame = frame
        self.canvas = canvas
        self.painting_label = painting_label
        self.mainwindow = mainwindow
        self.saved_files = listdir('save_states')
        self.current_file = 0
        self.canvas_xpos = 0.5
        self.canvas_ypos = 0.41

    def draw_fractal(self, fractal):
        if fractal.name == 'Sierpinski':
            fractal.start_sierpinski() #draws sierpinski
        if fractal.name == 'Koch':
            fractal.start_koch() #draws koch
        if fractal.name == 'Vicsek':
            fractal.start_box() #draws vicsek/box fractal

    def load_fractal(self, fractal):
        if fractal['name'] == 'Sierpinski':
            loaded_fractal = Sierpinski(self.canvas, fractal['position'][0], fractal['position'][1], fractal['size'], fractal['depth'], fractal['color'], False, [], fractal['name']) 
        elif fractal['name'] == 'Koch':
            loaded_fractal = Koch_Snowflake(self.canvas, fractal['position'][0], fractal['position'][1], fractal['size'], fractal['depth'], fractal['color'], False, [], fractal['name']) 
        elif fractal['name'] == 'Vicsek':
            loaded_fractal = Box(self.canvas, fractal['position'][0], fractal['position'][1], fractal['size'], fractal['depth'], fractal['color'], False, [], fractal['name']) 
        self.draw_fractal(loaded_fractal)

    def load_fractals(self):
        self.canvas.delete('all')
        file = self.saved_files[self.current_file] 
        with open(f'save_states/{file}', 'r') as json_file:
            loaded_data = load(json_file)
        for fractal in loaded_data:
            self.load_fractal(fractal)   

    def change_label(self): #changes the label below the painting to the name of the currently selected painting.
        file_name = self.saved_files[self.current_file]
        name = file_name.split('.')[0]
        self.painting_label.config(text=name) 

    def move_canvas_left(self): # moves the canvas to the left and switches the painting
        self.canvas_xpos -= 0.1
        self.canvas.place_configure(relx=self.canvas_xpos)
        self.painting_label.place_configure(relx=self.canvas_xpos)
        if self.canvas_xpos <= -0.2: # when the canvas is off-screen switch the painting and put the canvas to the right side of the screen
            self.current_file += 1
            self.canvas.delete('all')
            self.load_fractals()
            self.change_label()
            self.canvas_xpos = 1.2
        if self.canvas_xpos == 0.5: # when the canvas is back in the center stop
            return
        self.frame.after(100, self.move_canvas_left) # makes it so that the canvas is drawn while it loops 
    
    def move_canvas_right(self): # moves the canvas to the right and switches the painting
        self.canvas_xpos += 0.1
        self.canvas.place_configure(relx=self.canvas_xpos)
        self.painting_label.place_configure(relx=self.canvas_xpos)
        if self.canvas_xpos >= 1.2:# when the canvas is off-screen switch the painting and put the canvas to the left side of the screen
            self.current_file -= 1
            self.canvas.delete('all')
            self.load_fractals()
            self.change_label()
            self.canvas_xpos = -0.2
        if self.canvas_xpos == 0.5: # when the canvas is back in the center stop
            return
        self.frame.after(100, self.move_canvas_right) # makes it so that the canvas is drawn while it loops

    def slide_left(self): # goes to the next painting if possible
        if self.current_file >= len(self.saved_files) - 1:
            return
        self.move_canvas_left()

    def slide_right(self): #goes to the previous painting if possible
        if self.current_file <= 0:
            return
        self.move_canvas_right()
        
    def delete_canvas(self): # deletes a canvas
        remove(f'save_states/{self.saved_files[self.current_file]}')
        del self.saved_files[self.current_file]
        if len(self.saved_files) == 0: # if there are no paintings left, go back to the editor
            self.canvas.delete('all')
            self.painting_label.config(text='')
            self.mainwindow.lift()
        if len(self.saved_files) == self.current_file: # if you delete the last painting get the previous painting
            self.current_file -= 1
            self.canvas_xpos = -0.2
            self.canvas.delete('all')
            self.load_fractals()
            self.change_label()
            self.move_canvas_right()
        else: # in all other cases get the next painting
            self.canvas_xpos = 1.2
            self.canvas.delete('all')
            self.load_fractals()
            self.change_label()
            self.move_canvas_left()
