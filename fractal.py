#ttk is a submodule allowing for newer widgets in Tk version 8.5
from tkinter import *
from tkinter import ttk
import os
from os import listdir

#initialization of the window/GUI
mainwindow = Tk()
mainwindow.title("Fractal Art")
mainwindow.attributes("-fullscreen", True)

frame = Frame(mainwindow, height=1000, width=1000, bg="#D3D3D3")
frame.place(relwidth=0.75,relheight=0.8, rely=0.1, relx=0.1)

#Goes through all the fractal pictures and puts them as images on the buttons
folder = "fractal_pictures"
for picture_path in os.listdir(folder):
    img = PhotoImage(file=f"fractal_pictures/{picture_path}").subsample(7, 7)
    label = Label(image=img)
    label.image = img
    fractal_button = Button(frame, image=img)
    fractal_button.pack()

# for picture_path in os.listdir(folder):
#     add = PhotoImage(file=f"fractal_pictures/{picture_path}")
#     label = Label(image=add)
#     label.image = add
#     fractal_button = Button(frame, image = add)
#     fractal_button.pack()


mainwindow.mainloop()


