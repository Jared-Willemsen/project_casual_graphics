from tkinter import * 

mainwindow = Tk()
mainwindow.title("Fractal Art")
mainwindow.attributes("-fullscreen", True)
mainwindow.update_idletasks()

window_frames = []

window_height = mainwindow.winfo_height()
window_width = mainwindow.winfo_width()

print(window_height, window_width)

row_amount = 10
column_amount = 20

for i in range(row_amount):
    window_frames.append([])
    for j in range(column_amount):
        if (i + j) % 2 == 0:
            window_frames[i].append(Frame(mainwindow, background="White", height=window_height/row_amount, width=window_width/column_amount))
        else:
            window_frames[i].append(Frame(mainwindow, background="Black", height=window_height/row_amount, width=window_width/column_amount))
        window_frames[i][j].grid(row=i, column=j)
    
mainwindow.mainloop()