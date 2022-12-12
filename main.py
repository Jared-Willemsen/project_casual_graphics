#ttk is a submodule allowing for newer widgets in Tk version 8.5
from tkinter import *
from tkinter import colorchooser
import os

#Files we created for each of the different fractals
from sierpinski import *
from koch import *
from box import *
from controller import * 

#initialization of the window/GUI
mainwindow = Tk()
mainwindow.title("Fractal Art")
mainwindow.attributes("-fullscreen", True)
mainwindow.configure(background="#FFD700")

#background image for mainwindow
background_img_canv = PhotoImage(file="background_imgs/mural.png")
background_lbl1 = Label(mainwindow, image=background_img_canv)
background_lbl1.pack()

#frame that will include all the widgets/UI
fractal_frame = Frame(mainwindow, highlightbackground="#ef2f2f", 
                    highlightthickness=20, height=1000, width=1000, bg="#333333")
fractal_frame.place(relwidth=0.90,relheight=0.90, rely=0.05, relx=0.05)
frac_label = Label(fractal_frame, text="FRACTAL MUSEUM", 
            font=("Verdana italic",60), bg="#333333", fg="#f00")
frac_label.pack()

#canvas that will be inside the frame for the created image
fractal_canvas = Canvas(fractal_frame, bg="white", height=400, width=500)
fractal_canvas.pack()

#color picker function
def canvas_color():
    color = tkinter.colorchooser.askcolor(title="Tkinter color chooser")
    fractal_canvas.configure(bg=color[1])

#fractal color picker
#def fractal_color():
    #color = tkinter.colorchooser.askcolor(title="Tkinter color chooser")
    #return color[1]

#button for choosing canvas color
color_button = Button(fractal_frame, text="Canvas Background", command=canvas_color)
color_button.place(x=500, y=600)

#button for choosing fractal color
#frac_color = Button(fractal_frame, text="Fractal Color", command=fractal_color)
#frac_color.place(x=500, y=550)

#background image for frame
# background_img_frame = PhotoImage(file="museum.png")
# background_lbl2 = Label(fractal_frame, image=background_img_frame)
# background_lbl2.pack()

controller = Controller(fractal_canvas, fractal_frame, [], 5)
controller.draw_fractals()

#UI interaction underneath canvas
num_gen = Entry(fractal_frame, width=10)
gen_label = Label(fractal_frame, text="Generation", width=10)
gen_label.place(x=500,y=500)
num_gen.place(x=500,y=525)

#Buttons for the fractals and the picture frames
sierpinski_image = PhotoImage(file='fractal_pictures/sierpinski.png').subsample(4, 4)
koch_image = PhotoImage(file='fractal_pictures/koch_snowflake.png').subsample(4, 4)
box_image = PhotoImage(file='fractal_pictures/box_fractal.png').subsample(4, 4)

siepinski_label = Label(image=sierpinski_image)
sierpinski_button = Button(fractal_frame, image=sierpinski_image, command=controller.create_sierpinski)
sierpinski_button.place(x=200, y=100)

koch_label = Label(image=koch_image)
koch_button = Button(fractal_frame, image=koch_image)
koch_button.place(x=200, y=300)

box_label = Label(image=box_image)
box_button = Button(fractal_frame, image=box_image)
box_button.place(x=200, y=500)



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
        fractal_button.place(x=30, y=t)
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
