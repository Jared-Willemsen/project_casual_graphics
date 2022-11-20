#ttk is a submodule allowing for newer widgets in Tk version 8.5
from tkinter import *
from tkinter import ttk
import os
from os import listdir

#initialization of the window/GUI
mainwindow = Tk()
mainwindow.title("Fractal Art")
mainwindow.attributes("-fullscreen", True)

#Goes through all the fractal pictures and puts them as images on the buttons
folder = "fractal_pictures"
for picture_path in os.listdir(folder):
    fractal_button = Button(mainwindow)
    img = PhotoImage(file=f"fractal_pictures/{picture_path}")
    resized = img.subsample(7, 7)
    fractal_button.config(image=resized)
    fractal_button.pack()

mainwindow.mainloop()


