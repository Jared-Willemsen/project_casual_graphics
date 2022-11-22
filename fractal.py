#ttk is a submodule allowing for newer widgets in Tk version 8.5
from tkinter import *
import os

#initialization of the window/GUI
mainwindow = Tk()
mainwindow.title("Fractal Art")
mainwindow.attributes("-fullscreen", True)
mainwindow.configure(background="#FFD700")

#frame that will include all the widgets/UI
fractal_frame = Frame(mainwindow, highlightbackground="#ADD8E6", 
                    highlightthickness=20, height=1000, width=1000, bg="#333333")
fractal_frame.place(relwidth=0.8,relheight=0.8, rely=0.1, relx=0.1)
frac_label = Label(fractal_frame, text="FRACTAL MUSEUM", 
            font=("Verdana italic",60), bg="#333333", fg="#f00")
frac_label.pack()

#canvas that will be inside the frame for the created image
fractal_canvas = Canvas(fractal_frame, bg="white", height=400, width=500)
fractal_canvas.pack()

#Goes through all the fractal pictures and puts them as images on the buttons
fractal_folder = "fractal_pictures"
i = 100
for picture_path in os.listdir(fractal_folder):
    if picture_path != ".DS_Store":
        img = PhotoImage(file=f"fractal_pictures/{picture_path}").subsample(4, 4)
        label = Label(image=img)
        label.image = img
        fractal_button = Button(fractal_frame, image=img)
        fractal_button.place(x=900, y=i)
        i+=200
    else:
        continue

#goes for the 
frame_folder = "picture_frames"
t = 100
for picture_path in os.listdir(frame_folder):
    if picture_path != ".DS_Store":
        img = PhotoImage(file=f"picture_frames/{picture_path}").subsample(4, 4)
        label = Label(image=img)
        label.image = img
        fractal_button = Button(fractal_frame, image=img)
        fractal_button.place(x=100, y=t)
        t+=200
    else:
        continue

mainwindow.mainloop()


