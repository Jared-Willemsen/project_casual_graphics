# TODO Improvements: Colors of the fractal, DONE
# highlighting selected fractal in controller view (up and down buttons), DONE
# UI labels for clarity about use, ALMOST DONE
# Save canvas picture as jpg
# Save canvas animation as gyf
# Structure Code
# Splash Screen
# Settings Frane

from tkinter import *
from tkinter import colorchooser
from os import listdir
from controller import Controller
from gallery import Gallery

#Splash Screen
splash_screen = Tk()
splash_screen.title("Fractal Art")
splash_screen.attributes("-fullscreen", True)
splash_screen.configure(background="#FFD700")
#removes title bar
splash_screen.overrideredirect(True)

background_img = PhotoImage(file="background_imgs/mural.png")
background_lbl = Label(splash_screen, image=background_img).pack()

splash_frame = Frame(splash_screen, highlightbackground="#FFD700", 
                        highlightthickness=10, height=1000, width=1000, bg="#ab0513")
splash_frame.place(relwidth=0.90,relheight=0.90, rely=0.05, relx=0.05)

figma_img = PhotoImage(file="splash_screen/Fractal.png")
background_l = Label(splash_frame, image=figma_img, highlightbackground="#ab0513", highlightthickness=0, borderwidth=0).pack()

def main():
    splash_screen.destroy()
    #initialization of the window/GUI
    mainwindow = Tk()
    mainwindow.title("Fractal Art")
    mainwindow.attributes("-fullscreen", True)
    mainwindow.configure(background="#FFD700")

    #initialization of the Gallery window
    gallery_window = Toplevel(mainwindow)
    # gallery_window.attributes("-fullscreen", True)
    gallery_window.configure(background="#ab0513")

    #background image for mainwindow and gallery
    background_img_canv = PhotoImage(file="background_imgs/mural.png")
    background_lbl1 = Label(mainwindow, image=background_img_canv).pack()
    background_gallery = Label(gallery_window, image=background_img_canv).pack()

    #Frame Canvas and Label
    gallery_frame = Frame(gallery_window, highlightbackground="#FFD700", highlightthickness=10, height=1000, width=1000, bg="#ab0513")
    gallery_frame.place(relwidth=0.90,relheight=0.90, rely=0.05, relx=0.05)
    gallery_canvas = Canvas(gallery_frame, bg="white", highlightbackground="#FFD700", highlightthickness="10", height=400, width=500)
    gallery_label = Label(gallery_frame, text="FRACTAL GALLERY", 
                font=("Verdana italic",50), bg="#ab0513", fg="white")
    painting_name = Label(gallery_frame, text='placeholder', bg="#ab0513", fg="white", font=("Verdana",50))
    gallery_label.place(relx=0.5, rely=0.07, anchor=CENTER)
    gallery_canvas.place(relx=0.5, rely=0.45, anchor=CENTER)
    painting_name.place(relx=0.5, rely=0.9, anchor=CENTER)  

    #Edit frame that will include all the widgets/UI
    fractal_frame = Frame(mainwindow, highlightbackground="#FFD700", 
                        highlightthickness=10, height=1000, width=1000, bg="#ab0513")
    fractal_frame.place(relwidth=0.90,relheight=0.90, rely=0.05, relx=0.05)
    frac_label = Label(fractal_frame, text="FRACTAL MUSEUM", 
                font=("Verdana italic",50), bg="#ab0513", fg="white")
    frac_label.pack()

    # Settings/User Customization frames 
    settings2 = Frame(fractal_frame, highlightbackground="#FFD700", highlightthickness=5, height=300, width=200, bg="white")
    settings3 = Frame(fractal_frame, highlightbackground="#FFD700", highlightthickness=5, height=300, width=200, bg="white")
    settings4 = Frame(fractal_frame, highlightbackground="#FFD700", highlightthickness=5, height=300, width=200, bg="white")

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
    edit_button.place(relx=0.3, rely=0.75)

    delete_button_gallery = Button(gallery_frame, image=delete_image, command=gallery.delete_canvas)
    delete_button_gallery.place(relx=0.6, rely=0.75)

    #UI ELEMENTS EDITOR------------------------------------------------------------------------------------------------------------------
    #button pictures
    sierpinski_image = PhotoImage(file='fractal_pictures/sierpinski.png').subsample(3, 3)
    koch_image = PhotoImage(file='fractal_pictures/koch_snowflake.png').subsample(3, 3)
    box_image = PhotoImage(file='fractal_pictures/box_fractal.png').subsample(3, 3)
    up_image = PhotoImage(file='button_pictures/up_arrow.png').subsample(8,8)
    down_image = PhotoImage(file='button_pictures/down_arrow.png').subsample(8,8)
    quit_image = PhotoImage(file='button_pictures/quit.png').subsample(10, 10)

    #buttons and labels for making a new fractal
    sierpinski = Label(fractal_frame, text="Sierpinski", font=("Verdana",15), bg="#ab0513", fg="white")
    sierpinski.place(relx=0.01, rely=0.22)
    siepinski_label = Label(image=sierpinski_image)
    sierpinski_button = Button(fractal_frame, image=sierpinski_image, command=controller.create_sierpinski_triangle, highlightbackground="#FFD700")
    sierpinski_button.place(relx=0.1, rely=0.1)

    koch = Label(fractal_frame, text="Koch", font=("Verdana",15), bg="#ab0513", fg="white")
    koch.place(relx=0.01, rely=0.47)
    koch_label = Label(image=koch_image)
    koch_button = Button(fractal_frame, image=koch_image, command=controller.create_koch_snowflake, highlightbackground="#FFD700")
    koch_button.place(relx=0.1, rely=0.35)

    box = Label(fractal_frame, text="Vicsek/Box", font=("Verdana",15), bg="#ab0513", fg="white")
    box.place(relx=0.01, rely=0.72)
    box_label = Label(image=box_image)
    box_button = Button(fractal_frame, image=box_image, command=controller.create_box, highlightbackground="#FFD700")
    box_button.place(relx=0.1, rely=0.65)

    #step 1 label 
    step1_label = Label(fractal_frame, text="Step 1. Choose which fractal to display,\nYou can select any and even combine them!", font=("Verdana",12), bg="#ab0513", fg="white")
    step1_label.place(relx=0.05, rely=0.05)

    #step 2 labels and buttons: fractal customization
    step2_label = Label(settings2, text="Step 2. Customize the\nfractal and canvas", font=("Verdana", 12), bg="white")
    step2_label.pack(padx=3, pady=3)

    #step 3 labels and buttons: fractal customization
    step3_label = Label(settings3, text="Step 3. Save and view\nyour work!", font=("Verdana",12), bg="white", fg="black")
    step3_label.pack(padx=3, pady=3)

    #menu frame label
    menu_label = Label(fractal_frame, text="The fractals you have selected will show up here.\nGreen indicates you have selected that fractal", font=("Verdana",12), bg="#ab0513", fg="white").place(relx=0.74, rely=0.05)

    #buttons for changing selection
    selection_lbl = Label(settings4, text="Control which\nfractal to select", font=("Verdana",13), bg="white", fg="black").pack()

    up_label = Label(image=up_image)
    selection_button_up = Button(settings4, image=up_image, highlightbackground="white", command=controller.select_up).pack()

    down_label = Label(image=down_image)
    selection_button_down = Button(settings4, image=down_image, highlightbackground="white", command=controller.select_down).pack()
    
    #button for choosing canvas color
    color_button = Button(settings2, text="Canvas Background", highlightbackground="white", command=canvas_color)
    color_button.pack(padx=3, pady=3)

    #buttons for changing generation
    generation_increase = Button(settings2, text='Generation +', highlightbackground="white", command=controller.increase_depth).pack(padx=3, pady=3)
    generation_decrease = Button(settings2, text='Generation -', highlightbackground="white", command=controller.decrease_depth).pack(padx=3, pady=3)

    #fractal line color button
    fractal_color_button = Button(settings2, text='Line Color', highlightbackground="white", command=controller.change_color).pack(padx=3, pady=3)

    #save and load buttons
    save_button = Button(settings3, text='Save State', highlightbackground="white", command=controller.save_canvas).pack(padx=3, pady=3)
    load_button = Button(settings3, text='Gallery', highlightbackground="white", command=switch_to_gallery).pack(padx=3, pady=3)

    #delete button
    delete_button_editor = Button(settings2, text='Delete Fractal', highlightbackground="white", command=controller.delete_fractal).pack(padx=3, pady=3)

    quit_label = Label(image=quit_image)
    quit_button = Button(fractal_frame, image=quit_image, command=end_program).place(x=10, y=10)

    settings2.place(relx=0.3, rely=0.65)
    settings3.place(relx=0.6, rely=0.7)
    settings4.place(relx=0.8, rely=0.8)
    #---------------------------------------------------------------------------------------------------------------------------------
    mainwindow.mainloop()

#initialization of main program from splash screen
start_button = Button(splash_frame, text="Click to start", command=main, padx=5, pady=5, font=("Verdana", 25) )
start_button.pack(pady=10)
mainloop()