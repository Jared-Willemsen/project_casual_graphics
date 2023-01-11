from json import dumps as dump
from json import load 
from tkinter import *
from tkinter import colorchooser

from sierpinski import *
from koch import *
from box import *


class Controller: 
    def __init__(self, canvas, frame, fractals, max_depth=5):
        self.canvas = canvas
        self.canvas_color = 'white'
        self.frame = frame
        self.fractals = fractals
        self.max_depth = max_depth
        self.selected_fractal = 0

        menu_frame = Frame(self.frame, bg='white', highlightthickness = 10, highlightbackground="#FFD700")
        sliders = Frame(self.frame, highlightbackground="#FFD700", highlightthickness=5, height=300, width=200, bg="white")
        menu_canvas = Canvas(menu_frame, bg="white", height=500, width=220)
        menu_scrollbar = Scrollbar(menu_frame, orient="vertical", command=menu_canvas.yview) 
        self.menu_container = Frame(menu_canvas, bg='White')
        #self.menu_container.pack_propagate(0)
        
        self.menu_container.bind("<Configure>",lambda e: menu_canvas.configure(scrollregion=menu_canvas.bbox("all")))
        menu_canvas.create_window((0, 0), window=self.menu_container, anchor="nw")
        menu_canvas.configure(yscrollcommand = menu_scrollbar.set)
        
        # for i in range(50):
        #     Label(self.menu_container, text="Sample scrolling label").pack()

        menu_frame.place(relx=0.75, rely=0.1)
        menu_canvas.pack(side="left", fill="both", expand=True)
        menu_scrollbar.pack(side="left", fill="y")
        # menu_scrollbar.config(command=self.menu_container.yview)

        self.size_slider = Scale(sliders, label="Size/Zoom", from_=10, to=3000, length=150, bg="white", 
        fg="black", orient=HORIZONTAL, command=self.change_size)
        self.size_slider.pack()

        self.position_slider_x = Scale(sliders, label="X Position", from_=0, to=500, length=150, bg="white", 
        fg="black", orient=HORIZONTAL, command=self.change_x_position)
        self.position_slider_x.pack()
        self.position_slider_y = Scale(sliders, label="Y Position", from_=0, to=500, length=150, bg="white", 
        fg="black", orient=HORIZONTAL, command=self.change_y_position)
        self.position_slider_y.pack()

        self.file_name_entry = Entry(highlightbackground="#FFD700")
        self.file_name_entry.insert(END, 'Name your work!')
        self.file_name_entry.place(width=110, relx=0.6, rely=0.62)

        sliders.place(relx=0.46, rely=0.65)

    def set_sliders(self):
        self.size_slider.set(self.fractals[self.selected_fractal].size)
        self.position_slider_x.set(self.fractals[self.selected_fractal].xpos)
        self.position_slider_y.set(self.fractals[self.selected_fractal].ypos)

    #fractal selection methods
    def select_up(self):
        self.fractals[self.selected_fractal].switch_selection_status()
        if self.selected_fractal > 0:
            self.selected_fractal -= 1
        else:
            self.selected_fractal = len(self.fractals) - 1
        self.fractals[self.selected_fractal].switch_selection_status()
        self.set_sliders()

    def select_down(self):
        self.fractals[self.selected_fractal].switch_selection_status()
        if self.selected_fractal < (len(self.fractals) - 1):    
            self.selected_fractal += 1
        else:
            self.selected_fractal = 0
        self.fractals[self.selected_fractal].switch_selection_status()
        self.set_sliders()

    #fractal edit methods
    def increase_depth(self):
        if self.fractals[self.selected_fractal].depth < self.max_depth:
            self.fractals[self.selected_fractal].depth += 1
            self.draw_fractal(self.fractals[self.selected_fractal])
            self.fractals[self.selected_fractal].update_menu_item()

    def decrease_depth(self):
        if self.fractals[self.selected_fractal].depth > 0:
            self.fractals[self.selected_fractal].depth -= 1
            self.draw_fractal(self.fractals[self.selected_fractal])
            self.fractals[self.selected_fractal].update_menu_item()

    def change_size(self, val):
        self.fractals[self.selected_fractal].size = self.size_slider.get()
        self.draw_fractal(self.fractals[self.selected_fractal])
        self.fractals[self.selected_fractal].update_menu_item()
    
    def change_x_position(self, val):
        self.fractals[self.selected_fractal].xpos = self.position_slider_x.get()
        self.draw_fractal(self.fractals[self.selected_fractal])
        self.fractals[self.selected_fractal].update_menu_item()

    def change_y_position(self, val):
        self.fractals[self.selected_fractal].ypos = self.position_slider_y.get()
        self.draw_fractal(self.fractals[self.selected_fractal])
        self.fractals[self.selected_fractal].update_menu_item()
    
    def change_color(self):
        line_color = colorchooser.askcolor(title="Tkinter color chooser")
        self.fractals[self.selected_fractal].color = line_color[1]
        self.draw_fractal(self.fractals[self.selected_fractal])
        self.fractals[self.selected_fractal].update_menu_item()
    
        #color picker function
    def change_canvas_color(self):
        self.canvas_color = colorchooser.askcolor(title="Tkinter color chooser")[1]
        self.canvas.configure(bg=self.canvas_color)

    #Fractal creation methods
    def create_sierpinski_triangle(self):
        if len(self.fractals) == 0:
            new_sierpinski = Sierpinski(self.canvas, 150, 400, 100, 0, '#000000', True, [], 'Sierpinski')
        else:
            new_sierpinski = Sierpinski(self.canvas, 150, 400, 100, 0, '#000000', False, [], 'Sierpinski')
        self.fractals.append(new_sierpinski)
        self.set_sliders()
        self.draw_fractal(new_sierpinski)
        new_sierpinski.create_menu_item(self.menu_container)

    def create_koch_snowflake(self):
        if len(self.fractals) == 0:
            new_koch = Koch_Snowflake(self.canvas, 0, 200, 500, 0, "#000000", True, [], 'Koch')
        else:
            new_koch = Koch_Snowflake(self.canvas, 0, 200, 500, 0, '#000000', False, [], 'Koch')
        self.fractals.append(new_koch)
        self.set_sliders()
        self.draw_fractal(new_koch)
        new_koch.create_menu_item(self.menu_container)

    def create_box(self):
        if len(self.fractals) == 0:
            new_box = Box(self.canvas, 225, 150, 50, 0, "#000000", True, [], 'Vicsek')
        else:
            new_box = Box(self.canvas, 225, 150, 50, 0, "#000000", False, [], 'Vicsek')
        self.fractals.append(new_box)
        self.set_sliders()
        self.draw_fractal(new_box)
        new_box.create_menu_item(self.menu_container)

    #draws all fractals to the canvas
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
        if len(self.fractals) == 0:
            loaded_fractal.is_selected = True
        self.fractals.append(loaded_fractal)
        self.set_sliders()
        self.draw_fractal(loaded_fractal)
        loaded_fractal.create_menu_item(self.menu_container)

    def clear_controller(self):
        self.fractals.clear()
        self.selected_fractal = 0
        self.canvas.delete('all')
        for item in self.menu_container.winfo_children():
            item.destroy()

    #saves fractal list
    def save_canvas(self):
        file_name = self.file_name_entry.get()
        fractal_data = []
        for fractal in self.fractals:
            fractal_data.append(fractal.get_save_data())
        saved_data = []
        saved_data.append(fractal_data)
        saved_data.append(self.canvas_color)    
        json_controller = dump(saved_data)
        with open(f'save_states/{file_name}.json', 'w') as json_file:
            json_file.write(json_controller)
    
    def load_canvas(self, file):
        self.clear_controller()
        with open(f'save_states/{file}', 'r') as json_file:
            loaded_data = load(json_file)
        for fractal in loaded_data[0]:
            self.load_fractal(fractal)
        self.canvas_color = loaded_data[1]
        self.canvas.configure(bg = self.canvas_color)
    
    def delete_fractal(self):
        self.fractals[self.selected_fractal].delete_menu_item()
        self.fractals[self.selected_fractal].clear_fractal_from_canvas()
        del self.fractals[self.selected_fractal]
        if self.selected_fractal > len(self.fractals) - 1:
            self.selected_fractal -= 1
        self.fractals[self.selected_fractal].switch_selection_status()
