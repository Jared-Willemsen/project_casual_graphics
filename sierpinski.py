from math import sqrt  
from tkinter import * 

class Sierpinski:
    def __init__(self, canvas, xpos, ypos, size, depth, color):
        self.name = 'sierpinski triangle'
        self.canvas = canvas
        self.xpos = xpos
        self.ypos = ypos
        self.size = size
        self.depth = depth
        self.color = color
        self.menu_item = Frame()
    
    def start_sierpinski(self): 
        self.draw_sierpinski(self.size, self.xpos, self.ypos, self.depth)
    
    def draw_sierpinski(self, new_size, new_xpos, new_ypos, depth):
        if depth < 1:   
            self.draw_triangle(new_size, new_xpos, new_ypos)
            self.draw_triangle(new_size, (new_xpos + new_size), new_ypos)
            self.draw_triangle(new_size, (new_xpos + new_size/2), (new_ypos - sqrt(pow(new_size, 2) - pow((new_size/2), 2))))
        else:
            self.draw_sierpinski((new_size/2), new_xpos, new_ypos, (depth - 1))
            self.draw_sierpinski((new_size/2), (new_xpos + new_size), new_ypos, (depth - 1))
            self.draw_sierpinski((new_size/2), (new_xpos + new_size/2), (new_ypos - sqrt(pow(new_size, 2) - pow((new_size/2),2))), (depth - 1))

    def draw_triangle(self, size, x1, y1):
        x2, y2 = (x1 + size), y1
        x3, y3 = (x1 + size/2), (y1 - sqrt((pow(size, 2) - pow((size/2), 2))))
        self.canvas.create_line(x1, y1, x2, y2, fill=self.color)
        self.canvas.create_line(x1, y1, x3, y3, fill=self.color)
        self.canvas.create_line(x2, y2, x3, y3, fill=self.color)
    
    def clear_menu_item(self):
        for object in self.menu_item.winfo_children():
            object.destroy()

    def fill_menu_item(self):
        Label(self.menu_item, text=self.name, font=('Arial', 20), bg='white').grid(row=0, column=0, columnspan=2)

        Label(self.menu_item, text='size', font=('Arial', 10), bg='white').grid(row=1, column=0, sticky=W)
        Label(self.menu_item, text=self.size, font=('Arial', 10), bg='white').grid(row=1, column=1, sticky=E)

        Label(self.menu_item, text='generation', font=('Arial', 10), bg='white').grid(row=2, column=0, sticky=W)
        Label(self.menu_item, text=self.depth, font=('Arial', 10), bg='white').grid(row=2, column=1, sticky=E)

        Label(self.menu_item, text='color', font=('Arial', 10), bg='white').grid(row=3, column=0, sticky=W)
        Label(self.menu_item, text=self.color, font=('Arial', 10), bg='white').grid(row=3, column=1, sticky=E)

        Label(self.menu_item, text='position', font=('Arial', 10), bg='white').grid(row=4, column=0, sticky=W)
        Label(self.menu_item, text=f'({self.xpos}, {self.ypos})', font=('Arial', 10), bg='white').grid(row=4, column=1, sticky=E)
    
    def update_menu_item(self):
        self.clear_menu_item()
        self.fill_menu_item()
    
    def create_menu_item(self, menu_container):
        self.menu_item = Frame(menu_container, height=100, width=250, bg='white', highlightbackground='black', highlightthickness=2)
        self.fill_menu_item()
        self.menu_item.pack()

        