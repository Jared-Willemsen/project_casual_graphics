from tkinter import *
import matplotlib as plt
import numpy as np

mainwindow = Tk()
mainwindow.mainloop()

# def fractal(n, c):

#     #mandelbrot set 

#     #base case
#     if n == 0:
#         return 0
#     else:
#         #recursive case
#         return fractal(n-1, c) ** 2 + c

#for i in range(11):
   #print(f"z ({i}) = {fractal(i, 1)}")

# memory efficient
def fractal2(c):
    z = 0
    while True:
        yield z
        z = z ** 2 + c
for n, z in enumerate(fractal2(-1)):
    if n < 11:
        print(f"z({n}) = {z}")
