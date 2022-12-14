#ttk is a submodule allowing for newer widgets in Tk version 8.5
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

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
fractal_frame = Frame(mainwindow, highlightbackground="#a8b8d0", 
                    highlightthickness=10, height=1000, width=1000, bg="#333333")
fractal_frame.place(relwidth=0.90,relheight=0.90, rely=0.05, relx=0.05)
frac_label = Label(fractal_frame, text="FRACTAL MUSEUM", 
            font=("Verdana italic",60), bg="#333333", fg="#a8b8d0")
frac_label.pack()

#canvas that will be inside the frame for the created image
fractal_canvas = Canvas(fractal_frame, bg="white", highlightbackground="#a8b8d0", highlightthickness="10", height=400, width=500)
fractal_canvas.pack()

#color picker function
def canvas_color():
    color = tkinter.colorchooser.askcolor(title="Tkinter color chooser")
    fractal_canvas.configure(bg=color[1])

#fractal color picker
#def fractal_color():
    #color = tkinter.colorchooser.askcolor(title="Tkinter color chooser")
    #return color[1]

#button for choosing fractal color
#frac_color = Button(fractal_frame, text="Fractal Color", command=fractal_color)
#frac_color.place(x=500, y=550)

controller = Controller(fractal_canvas, fractal_frame, [], 5)
controller.draw_fractals()

# koch = Koch_Snowflake(fractal_canvas, 0, 200, 5, 5, "blue")
# koch.start_koch()

# box = Box(fractal_canvas, 0, 200, 5, "blue")
# box.draw_box(0, 200, 500, 400)

#UI ELEMENTS------------------------------------------------------------------------------------------------------------------
#button pictures
sierpinski_image = PhotoImage(file='fractal_pictures/sierpinski.png').subsample(3, 3)
koch_image = PhotoImage(file='fractal_pictures/koch_snowflake.png').subsample(3, 3)
box_image = PhotoImage(file='fractal_pictures/box_fractal.png').subsample(3, 3)
up_image = PhotoImage(file='button_pictures/up_arrow.png').subsample(7,7)
down_image = PhotoImage(file='button_pictures/down_arrow.png').subsample(7,7)

#buttons for making a new fractal
siepinski_label = Label(image=sierpinski_image)
sierpinski_button = Button(fractal_frame, image=sierpinski_image, command=controller.create_sierpinski_triangle)
sierpinski_button.place(x=100, y=100)

koch_label = Label(image=koch_image)
koch_button = Button(fractal_frame, image=koch_image, command=controller.create_koch_snowflake)
koch_button.place(x=100, y=300)

box_label = Label(image=box_image)
box_button = Button(fractal_frame, image=box_image)
box_button.place(x=100, y=500)

#buttons for changing selection
up_label = Label(image=up_image)
selection_button_up = Button(fractal_frame, image=up_image, highlightbackground="#333333", command=controller.select_previous).pack()

down_lable = Label(image=down_image)
selection_button_down = Button(fractal_frame, image=down_image, highlightbackground="#333333", command=controller.select_next).pack()

#buttons for changing generation
generation_increase = Button(fractal_frame, text='Generation +', highlightbackground="#333333", command=controller.increase_depth).place(x=375, y=500)
generation_decrease = Button(fractal_frame, text='Generation -', highlightbackground="#333333", command=controller.decrease_depth).place(x=375, y=550)

#button for choosing canvas color
color_button = Button(fractal_frame, text="Canvas Background", highlightbackground="#333333", command=canvas_color)
color_button.place(x=375, y=600)

save_button = Button(fractal_frame, text='Save', highlightbackground="#333333", command=controller.save_canvas).pack()
#---------------------------------------------------------------------------------------------------------------------------------
mainwindow.mainloop()

