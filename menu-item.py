from tkinter import *

root = Tk()
root.geometry('500x500')
root.resizable(False, False)
fractal = Label(root, text='Siepinski triagle', font=('Arial', 50)).grid(row=0, column=0, columnspan=2)

size_label = Label(root, text='size', font=('Arial',25)).grid(row=1, column=0, sticky=W)
size_value = Label(root, text='100', font=('Arial', 25)).grid(row=1, column=1, sticky=E)

generation_label = Label(root, text='generation', font=('Arial', 25)).grid(row=2, column=0, sticky=W)
generation_value = Label(root, text='3', font=('Arial', 25)).grid(row=2, column=1, sticky=E)

color_label = Label(root, text='color', font=('Arial', 25)).grid(row=3, column=0, sticky=W)
color_valie = Label(root, text='black', font=('Arial', 25)).grid(row=3, column=1, sticky=E)

position_label = Label(root, text='position', font=('Arial', 25)).grid(row=4, column=0, sticky=W)
position_value = Label(root, text='(300, 300)', font=('Arial', 25)).grid(row=4, column=1, sticky=E)


root.mainloop()