# TODO Improvements: Colors of the fractal, DONE
# highlighting selected fractal in controller view (up and down buttons), DONE
# UI labels for clarity about use, ALMOST DONE
# Wow factor is the brain
# Save canvas picture as jpg
# Save canvas animation as gyf

#ttk is a submodule allowing for newer widgets in Tk version 8.5
from tkinter import *
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
fractal_frame = Frame(mainwindow, highlightbackground="#FFD700", 
                    highlightthickness=10, height=1000, width=1000, bg="#2E2252")
fractal_frame.place(relwidth=0.90,relheight=0.90, rely=0.05, relx=0.05)
frac_label = Label(fractal_frame, text="FRACTAL MUSEUM", 
            font=("Verdana italic",60), bg="#2E2252", fg="white")
frac_label.pack()

#canvas that will be inside the frame for the created image
fractal_canvas = Canvas(fractal_frame, bg="white", highlightbackground="#FFD700", highlightthickness="10", height=400, width=500)
fractal_canvas.pack()

#color picker function
def canvas_color():
    color = colorchooser.askcolor(title="Tkinter color chooser")
    fractal_canvas.configure(bg=color[1])

#repeatedly changes fractal museum label color 
def color_switchr():
    current = frac_label.cget('fg')
    if current == 'red':
        new = 'green'
    elif current == 'green':
        new = 'blue'
    else:
        new  = 'red'
    frac_label.config(fg=new)
    fractal_frame.after(500, color_switchr)
color_switchr()

controller = Controller(fractal_canvas, fractal_frame, [])  

#UI ELEMENTS------------------------------------------------------------------------------------------------------------------
#button pictures
sierpinski_image = PhotoImage(file='fractal_pictures/sierpinski.png').subsample(3, 3)
koch_image = PhotoImage(file='fractal_pictures/koch_snowflake.png').subsample(3, 3)
box_image = PhotoImage(file='fractal_pictures/box_fractal.png').subsample(3, 3)
up_image = PhotoImage(file='button_pictures/up_arrow.png').subsample(8,8)
down_image = PhotoImage(file='button_pictures/down_arrow.png').subsample(8,8)

#step 1 label
step1_label = Label(fractal_frame, text="Step 1. Choose which fractal to display\nYou can select any and even combine them!", font=("Verdana",12), bg="#2E2252", fg="white")
step1_label.place(x=40, y=50)

#step 2 label
step2_label = Label(fractal_frame, text="Step 2. Customize how the\nfractal and canvas look", font=("Verdana",12), bg="#2E2252", fg="white")
step2_label.place(x=350, y=500)

#step 3 label
step3_label = Label(fractal_frame, text="Step 3. Save your work!", font=("Verdana",12), bg="#2E2252", fg="white")
step3_label.place(x=780, y=500)

#menu frame label
menu_label = Label(fractal_frame, text="The fractals you have selected will show up here.\nGreen indicates you have selected that fractal", font=("Verdana",12), bg="#2E2252", fg="white").place(x=940, y=50)

#buttons and labels for making a new fractal
sierpinski = Label(fractal_frame, text="Sierpinski", font=("Verdana",15), bg="#2E2252", fg="white")
sierpinski.place(x=15, y=180)
siepinski_label = Label(image=sierpinski_image)
sierpinski_button = Button(fractal_frame, image=sierpinski_image, command=controller.create_sierpinski_triangle)
sierpinski_button.place(x=100, y=100)

koch = Label(fractal_frame, text="Koch", font=("Verdana",15), bg="#2E2252", fg="white")
koch.place(x=15, y=380)
koch_label = Label(image=koch_image)
koch_button = Button(fractal_frame, image=koch_image, command=controller.create_koch_snowflake)
koch_button.place(x=100, y=300)

box = Label(fractal_frame, text="Vicsek/Box", font=("Verdana",15), bg="#2E2252", fg="white")
box.place(x=12, y=580)
box_label = Label(image=box_image)
box_button = Button(fractal_frame, image=box_image, command=controller.create_box)
box_button.place(x=100, y=500)

#buttons for changing selection
up_label = Label(image=up_image)
selection_button_up = Button(fractal_frame, image=up_image, highlightbackground="#2E2252", command=controller.select_previous).pack()

down_label = Label(image=down_image)
selection_button_down = Button(fractal_frame, image=down_image, highlightbackground="#2E2252", command=controller.select_next).pack()

selection_lbl = Label(fractal_frame, text="Control which\nfractal to select", font=("Verdana",13), bg="#2E2252", fg="white").pack()

#button for choosing canvas color
color_button = Button(fractal_frame, text="Canvas Background", highlightbackground="#2E2252", command=canvas_color)
color_button.place(x=375, y=550)

#buttons for changing generation
generation_increase = Button(fractal_frame, text='Generation +', highlightbackground="#2E2252", command=controller.increase_depth).place(x=375, y=600)
generation_decrease = Button(fractal_frame, text='Generation -', highlightbackground="#2E2252", command=controller.decrease_depth).place(x=375, y=650)

#fractal line color button
fractal_color_button = Button(fractal_frame, text='Line Color', highlightbackground="#2E2252", command=controller.change_color).place(x=375, y=700)

#save and load buttons
save_button = Button(fractal_frame, text='Save State', highlightbackground="#2E2252", command=controller.save_canvas).place(x=780, y=550)
load_button = Button(fractal_frame, text='Load Prev State', highlightbackground='#2E2252', command=controller.load_canvas).place(x=780, y=600)
#---------------------------------------------------------------------------------------------------------------------------------
mainwindow.mainloop()

