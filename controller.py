from sierpinski import *
import tkinter

class Controller: 
    def __init__(self, canvas, frame, fractals, max_fractals):
        self.canvas = canvas
        self.frame = frame
        self.fractals = fractals
        self.max_fractals = max_fractals
        self.menu_container = Frame(self.frame, height=500, width=250, bg='white')
        self.menu_container.pack_propagate(False)
        self.menu_container.place(x=900, y=100)
        self.menu_item_list = [] 
        self.selected_fractal = 0

    # def select_fractal(self, selection):
    #     self.select_fractal = selection

    def select_next(self):
        if self.selected_fractal < (len(self.fractals) - 1):    
            self.selected_fractal += 1
    
    def select_previous(self):
        if self.selected_fractal > 0:
            self.selected_fractal -= 1

    def create_menu_item(self, fractal):
        menu_item = Frame(self.menu_container, height=100, width=250, bg='white', highlightbackground='black', highlightthickness=2)
        title = Label(menu_item, text=fractal.name, font=('Arial', 20), bg='white').grid(row=0, column=0, columnspan=2)

        size_label = Label(menu_item, text='size', font=('Arial', 10), bg='white').grid(row=1, column=0, sticky=W)
        size_value = Label(menu_item, text=fractal.size, font=('Arial', 10), bg='white').grid(row=1, column=1, sticky=E)

        generation_label = Label(menu_item, text='generation', font=('Arial', 10), bg='white').grid(row=2, column=0, sticky=W)
        generation_value = Label(menu_item, text=fractal.depth, font=('Arial', 10), bg='white').grid(row=2, column=1, sticky=E)

        color_label = Label(menu_item, text='color', font=('Arial', 10), bg='white').grid(row=3, column=0, sticky=W)
        color_valie = Label(menu_item, text=fractal.color, font=('Arial', 10), bg='white').grid(row=3, column=1, sticky=E)

        position_label = Label(menu_item, text='position', font=('Arial', 10), bg='white').grid(row=4, column=0, sticky=W)
        position_value = Label(menu_item, text=f'({fractal.xpos}, {fractal.ypos})', font=('Arial', 10), bg='white').grid(row=4, column=1, sticky=E)
        menu_item.pack()
        return menu_item


    def add_menu_item(self, fractal):
        self.menu_item_list.append(self.create_menu_item(fractal))
        
    def create_sierpinski(self):
        if len(self.fractals) < self.max_fractals:
            new_sierpinski = Sierpinski(self.canvas, 0, 400, 100, 0, 'black')
            self.fractals.append(new_sierpinski)
            self.draw_fractals()
            self.add_menu_item(new_sierpinski)

    def draw_fractals(self): # not sure if this will work yet (I think we might have to refresh the canvas anytime something is edited) 
        for fractal in self.fractals:
            if fractal.name == 'sierpinski triangle':
                 fractal.start_sierpinski()
