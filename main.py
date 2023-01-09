# TODO Improvements: Colors of the fractal, DONE
# highlighting selected fractal in controller view (up and down buttons), DONE
# UI labels for clarity about use, ALMOST DONE
# Wow factor is the brain
# Save canvas picture as jpg
# Save canvas animation as gyf

from tkinter import *
from tkinter import colorchooser
from os import listdir

#Files for the Controller and Gallery Class 
from controller import Controller
from gallery import Gallery

#initialization of the window/GUI
mainwindow = Tk()
mainwindow.title("Fractal Art")
mainwindow.attributes("-fullscreen", True)
mainwindow.configure(background="#FFD700")

#initialization of the Gallery window
gallery_window = Toplevel(mainwindow)
# gallery_window.attributes("-fullscreen", True)
gallery_window.configure(background="#2E2252")

#background image for mainwindow and gallery
background_img_canv = PhotoImage(file="background_imgs/mural.png")
background_lbl1 = Label(mainwindow, image=background_img_canv).pack()
background_gallery = Label(gallery_window, image=background_img_canv).pack()

#Frame Canvas and Label
gallery_frame = Frame(gallery_window, highlightbackground="#FFD700", highlightthickness=10, height=1000, width=1000, bg="#2E2252")
gallery_frame.place(relwidth=0.90,relheight=0.90, rely=0.05, relx=0.05)
gallery_canvas = Canvas(gallery_frame, bg="white", highlightbackground="#FFD700", highlightthickness="10", height=400, width=500)
gallery_label = Label(gallery_frame, text="FRACTAL GALLERY", 
            font=("Verdana italic",60), bg="#2E2252", fg="white")
painting_name = Label(gallery_frame, text='placeholder', bg="#2E2252", fg="white", font=("Verdana",60))
gallery_label.place(relx=0.5, rely=0.07, anchor=CENTER)
gallery_canvas.place(relx=0.5, rely=0.41, anchor=CENTER)
painting_name.place(relx=0.5, rely=0.755, anchor=CENTER)  

#Edit frame that will include all the widgets/UI
fractal_frame = Frame(mainwindow, highlightbackground="#FFD700", 
                    highlightthickness=10, height=1000, width=1000, bg="#2E2252")
fractal_frame.place(relwidth=0.90,relheight=0.90, rely=0.05, relx=0.05)
frac_label = Label(fractal_frame, text="FRACTAL MUSEUM", 
            font=("Verdana italic",50), bg="#2E2252", fg="white")
frac_label.pack()

#canvas that will be inside the frame for the created image
fractal_canvas = Canvas(fractal_frame, bg="white", highlightbackground="#FFD700", highlightthickness="10", height=400, width=500)
fractal_canvas.pack()

#Functions---------------------------------------------------------------------------------------------------------------------------
def end_program():
    gallery_window.destroy()
    mainwindow.destroy()

#color picker function
def canvas_color():
    color = colorchooser.askcolor(title="Tkinter color chooser")
    fractal_canvas.configure(bg=color[1])

#repeatedly changes fractal museum label color 
# def color_switcher():
#     current = frac_label.cget('fg')
#     if current == 'red':
#         new = 'green'
#     elif current == 'green':
#         new = 'blue'
#     else:
#         new  = 'red'
#     frac_label.config(fg=new)
#     gallery_label.config(fg=new)
#     fractal_frame.after(500, color_switcher)
# color_switcher()

#switching functions
def switch_to_gallery():
    gallery.saved_files = listdir('save_states')
    if len(gallery.saved_files) == 0:
        return
    gallery.change_label()
    gallery.load_fractals()
    gallery_window.lift()

def switch_to_editor():
    path = listdir('save_states')
    file = path[gallery.current_file]
    controller.load_canvas(file)
    file_name = file.split('.')[0]
    controller.file_name_entry.delete(0, 'end')
    controller.file_name_entry.insert(END, file_name)
    mainwindow.lift()

#initializing controller and gallery class
controller = Controller(fractal_canvas, fractal_frame, [])  
gallery = Gallery(gallery_frame, gallery_canvas, painting_name, mainwindow)

#UI ELELMENTS GALLERY----------------------------------------------------------------------------------------------------------------
right_image = PhotoImage(file='button_pictures/right_arrow.png').subsample(3, 3)
left_image = PhotoImage(file='button_pictures/left_arrow.png').subsample(3, 3)
edit_image = PhotoImage(file='button_pictures/edit.png').subsample(3, 3)
delete_image = PhotoImage(file='button_pictures/delete.png').subsample(3, 3)

right_label = Label(image=right_image)
left_label = Label(image=left_image)
edit_label = Label(image=edit_image)
delete_label = Label(image=delete_image)

right_button = Button(gallery_frame, image=right_image, command=gallery.slide_left)
right_button.place(relx=0.85, rely=0.41)

left_button = Button(gallery_frame, image=left_image, command=gallery.slide_right)
left_button.place(relx=0.01, rely=0.41)

edit_button = Button(gallery_frame, image=edit_image, command=switch_to_editor)
edit_button.place(relx=0.01, rely=0.68)

delete_button_gallery = Button(gallery_frame, image=delete_image, command=gallery.delete_canvas)
delete_button_gallery.place(relx=0.8, rely=0.68)
#UI ELEMENTS EDITOR------------------------------------------------------------------------------------------------------------------
#button pictures
sierpinski_image = PhotoImage(file='fractal_pictures/sierpinski.png').subsample(3, 3)
koch_image = PhotoImage(file='fractal_pictures/koch_snowflake.png').subsample(3, 3)
box_image = PhotoImage(file='fractal_pictures/box_fractal.png').subsample(3, 3)
up_image = PhotoImage(file='button_pictures/up_arrow.png').subsample(8,8)
down_image = PhotoImage(file='button_pictures/down_arrow.png').subsample(8,8)
quit_image = PhotoImage(file='button_pictures/quit.png').subsample(10, 10)

#step 1 label
step1_label = Label(fractal_frame, text="Step 1. Choose which fractal to display,\nYou can select any and even combine them!", font=("Verdana",12), bg="#2E2252", fg="white")
step1_label.place(relx=0.05, rely=0.05)

#step 2 label
step2_label = Label(fractal_frame, text="Step 2. Customize how the\nfractal and canvas look", font=("Verdana",12), bg="#2E2252", fg="white")
step2_label.place(relx=0.3, rely=0.65)

#step 3 label
step3_label = Label(fractal_frame, text="Step 3. Save and view\nyour work!", font=("Verdana",12), bg="#2E2252", fg="white")
step3_label.place(relx=0.6, rely=0.65)

#menu frame label
menu_label = Label(fractal_frame, text="The fractals you have selected will show up here.\nGreen indicates you have selected that fractal", font=("Verdana",12), bg="#2E2252", fg="white").place(relx=0.74, rely=0.05)

#buttons and labels for making a new fractal
sierpinski = Label(fractal_frame, text="Sierpinski", font=("Verdana",15), bg="#2E2252", fg="white")
sierpinski.place(relx=0.01, rely=0.22)
siepinski_label = Label(image=sierpinski_image)
sierpinski_button = Button(fractal_frame, image=sierpinski_image, command=controller.create_sierpinski_triangle)
sierpinski_button.place(x=100, y=100)

koch = Label(fractal_frame, text="Koch", font=("Verdana",15), bg="#2E2252", fg="white")
koch.place(relx=0.01, rely=0.47)
koch_label = Label(image=koch_image)
koch_button = Button(fractal_frame, image=koch_image, command=controller.create_koch_snowflake)
koch_button.place(x=100, y=300)

box = Label(fractal_frame, text="Vicsek/Box", font=("Verdana",15), bg="#2E2252", fg="white")
box.place(relx=0.01, rely=0.72)
box_label = Label(image=box_image)
box_button = Button(fractal_frame, image=box_image, command=controller.create_box)
box_button.place(x=100, y=500)

#buttons for changing selection
up_label = Label(image=up_image)
selection_button_up = Button(fractal_frame, image=up_image, highlightbackground="#2E2252", command=controller.select_up).pack()

down_label = Label(image=down_image)
selection_button_down = Button(fractal_frame, image=down_image, highlightbackground="#2E2252", command=controller.select_down).pack()

selection_lbl = Label(fractal_frame, text="Control which\nfractal to select", font=("Verdana",13), bg="#2E2252", fg="white").pack()

#button for choosing canvas color
color_button = Button(fractal_frame, text="Canvas Background", highlightbackground="#2E2252", command=canvas_color)
color_button.place(relx=0.3, rely=0.7)

#buttons for changing generation
generation_increase = Button(fractal_frame, text='Generation +', highlightbackground="#2E2252", command=controller.increase_depth).place(relx=0.3, rely=0.75)
generation_decrease = Button(fractal_frame, text='Generation -', highlightbackground="#2E2252", command=controller.decrease_depth).place(relx=0.3, rely=0.8)

#fractal line color button
fractal_color_button = Button(fractal_frame, text='Line Color', highlightbackground="#2E2252", command=controller.change_color).place(relx=0.3, rely=0.85)

#save and load buttons
save_button = Button(fractal_frame, text='Save State', highlightbackground="#2E2252", command=controller.save_canvas).place(relx=0.6, rely=0.75)
load_button = Button(fractal_frame, text='Gallery', highlightbackground='#2E2252', command=switch_to_gallery).place(relx=0.6, rely=0.8)

#delete button
delete_button_editor = Button(fractal_frame, text='Delete Fractal', highlightbackground="#2E2252", command=controller.delete_fractal).place(relx=0.3, rely=0.9)

quit_label = Label(image=quit_image)
quit_button = Button(fractal_frame, image=quit_image, highlightbackground="#2E2252", command=end_program).place(x=10, y=10)
#---------------------------------------------------------------------------------------------------------------------------------
mainwindow.mainloop()

