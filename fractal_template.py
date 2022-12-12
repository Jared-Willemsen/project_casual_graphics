from tkinter import *

class FractalTemplate:
    def __init__(self, name, canvas, xpos, ypos, size, depth, color):
        self.name = name
        self.canvas = canvas
        self.xpos = xpos
        self.ypos = ypos
        self.size = size
        self.depth = depth
        self.color = color
        self.menu_item = Frame()
    
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
        