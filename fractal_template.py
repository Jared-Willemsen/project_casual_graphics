from tkinter import *

class FractalTemplate:
    def __init__(self, canvas, xpos, ypos, size, depth, color, is_selected, lines, name):
        self.canvas = canvas
        self.xpos = xpos
        self.ypos = ypos
        self.size = size
        self.depth = depth
        self.color = color
        self.is_selected = is_selected
        self.lines = lines
        self.name = name
        self.menu_item = Frame()
    
    def clear_menu_item(self): #deletes all lables in its menu-item
        for object in self.menu_item.winfo_children():
            object.destroy()

    def delete_menu_item(self):
        self.menu_item.destroy()
    
    def clear_fractal_from_canvas(self):
        for line in self.lines:
            self.canvas.delete(line) 
        self.lines.clear()

    def fill_menu_item(self): #fills the menu-item with information about the fractal
        Label(self.menu_item, text=self.name, font=('Arial', 20), bg='white').grid(row=0, column=0, columnspan=2)

        Label(self.menu_item, text='size', font=('Arial', 10), bg='white').grid(row=1, column=0, sticky=W)
        Label(self.menu_item, text=self.size, font=('Arial', 10), bg='white').grid(row=1, column=1, sticky=E)

        Label(self.menu_item, text='generation', font=('Arial', 10), bg='white').grid(row=2, column=0, sticky=W)
        Label(self.menu_item, text=self.depth, font=('Arial', 10), bg='white').grid(row=2, column=1, sticky=E)

        Label(self.menu_item, text='color', font=('Arial', 10), bg='white').grid(row=3, column=0, sticky=W)
        Label(self.menu_item, text=self.color, font=('Arial', 10), bg='white').grid(row=3, column=1, sticky=E)

        Label(self.menu_item, text='position', font=('Arial', 10), bg='white').grid(row=4, column=0, sticky=W)
        Label(self.menu_item, text=f'({self.xpos}, {self.ypos})', font=('Arial', 10), bg='white').grid(row=4, column=1, sticky=E)
    
    def switch_selection_status(self):
        if not self.is_selected:
            self.is_selected = True
            self.menu_item.config(highlightbackground='green')
        else:
            self.is_selected = False
            self.menu_item.config(highlightbackground='#333333')

    def update_menu_item(self): #clears the old menu-item and fills it with new values
        self.clear_menu_item()
        self.fill_menu_item()
    
    def create_menu_item(self, menu_container): #creates the frame for the menu-item fills it with current values and packs it to the menu
        self.menu_item = Frame(menu_container, height=100, width=250, bg='white', highlightbackground='#333333', highlightthickness=6)
        if self.is_selected:
            self.menu_item.config(highlightbackground='green')
        self.fill_menu_item()
        self.menu_item.pack()

    def get_save_data(self):
        saved_data = {}
        saved_data['name'] = self.name
        saved_data['position'] = (self.xpos, self.ypos)
        saved_data['size'] = self.size
        saved_data['depth'] = self.depth
        saved_data['color'] = self.color
        return saved_data
    

        