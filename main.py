#ttk is a submodule allowing for newer widgets in Tk version 8.5
from tkinter import *
import os
from sierpinski import *
from koch import *

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

#sierpinski = sierpinski(fractal_canvas, 150, 275, 100, 3, "blue")
#command = sierpinski.start_sierpinski()

koch = test_koch2(fractal_canvas, 0, 200, 500, 400, 2, "black")
koch.draw_base()

#UI interaction underneath canvas
num_gen = Entry(fractal_frame, width=10)
gen_label = Label(fractal_frame, text="Generation", width=10)
gen_label.place(x=500,y=500)
num_gen.place(x=500,y=525)

#background image
#background_img = PhotoImage(file="17495.png")
#background_lbl = Label(mainwindow, image=background_img)
#background_lbl.pack()

#Goes through all the fractal pictures and puts them as images on the buttons
fractal_folder = "fractal_pictures"
i = 100
for picture_path in os.listdir(fractal_folder):
    if picture_path != ".DS_Store":
        img = PhotoImage(file=f"fractal_pictures/{picture_path}").subsample(4, 4)

        #keeps a reference of the image so that it can be displayed and is not deleted
        label = Label(image=img)
        label.image = img

        fractal_button = Button(fractal_frame, image=img)
        fractal_button.place(x=900, y=i)
        i+=200
    else:
        continue



#goes through the picture frames and puts them as images on the buttons
frame_folder = "picture_frames"
t = 100
for picture_path in os.listdir(frame_folder):
    if picture_path != ".DS_Store":
        img = PhotoImage(file=f"picture_frames/{picture_path}").subsample(4, 4)

        #keeps a reference of the label image so that it can be displayed
        label = Label(image=img)
        label.image = img
        fractal_button = Button(fractal_frame, image=img)
        fractal_button.place(x=100, y=t)
        t+=200
    else:
        continue

mainwindow.mainloop()

# def color_the_canvas(color):
#     r = ("0"+hex(int(scale_red.get()))[2:])[-2:]
#     g = ("0"+hex(int(scale_green.get()))[2:])[-2:]
#     b = ("0"+hex(int(scale_blue.get()))[2:])[-2:]
#     canvas.configure(bg="#"+r+g+b)

#Elements take the space the children need, unless they are empty.
#When the children are empty width and height can be set.
# canvas = tk.Canvas(root,bg="#FFFFFF",height=200)
# canvas.pack(fill = tk.X, padx = 20, pady = 5)
# scale_red = tk.Scale(root,from_=0,to=255, troughcolor = "#FF0000", orient=tk.HORIZONTAL, command=color_the_canvas)
# scale_red.set(255)
# scale_red.pack(fill = tk.X, padx = 20, pady = 5)
# scale_green = tk.Scale(root,from_=0,to=255, troughcolor = "#00FF00", orient=tk.HORIZONTAL, command=color_the_canvas)
# scale_green.set(255)
# scale_green.pack(fill = tk.X, padx = 20, pady = 5)
# scale_blue = tk.Scale(root,from_=0,to=255, troughcolor = "#0000FF", orient=tk.HORIZONTAL, command=color_the_canvas)
# scale_blue.set(255)
# scale_blue.pack(fill = tk.X, padx = 20, pady = 5)
