from tkinter import *
from tkinter.ttk import *
import math
import random
# Create the main window
root = Tk()

# Create a canvas to draw on
canvas = Canvas(root, width=800, height=600)
canvas.pack()

class RecursiveTree:
    def __init__(self, canvas, trunk_length=100, branch_angle=30):
        self.canvas = canvas
        self.trunk_length = trunk_length
        self.branch_angle = branch_angle

    def draw(self, x1, y1, depth):
        if depth == 0:
            # Choose a random color for the neuron
            color = random.choice(["white", "blue"])

            # Draw a neuron at the end of the branch
            self.canvas.create_oval(x1 - 5, y1 - 5, x1 + 5, y1 + 5, fill=color)

            # Call the after method to make the neurons flicker
            self.canvas.after(100, self.draw, x1, y1, depth)
            return
        else:
            # Calculate the end points of the branches
            x2 = x1 + self.trunk_length * math.cos(math.radians(self.branch_angle))
            y2 = y1 + self.trunk_length * math.sin(math.radians(self.branch_angle))
            x3 = x1 + self.trunk_length * math.cos(math.radians(-self.branch_angle))
            y3 = y1 + self.trunk_length * math.sin(math.radians(-self.branch_angle))

            # Calculate the end points of the sub-branches
            x4 = x2 + self.trunk_length * math.cos(math.radians(self.branch_angle))
            y4 = y2 + self.trunk_length * math.sin(math.radians(self.branch_angle))
            x5 = x2 + self.trunk_length * math.cos(math.radians(-self.branch_angle))
            y5 = y2 + self.trunk_length * math.sin(math.radians(-self.branch_angle))

            # Calculate the end points of the upper branches
            x6 = x3 + self.trunk_length * math.cos(math.radians(self.branch_angle))
            y6 = y3 + self.trunk_length * math.sin(math.radians(self.branch_angle))
            x7 = x3 + self.trunk_length * math.cos(math.radians(-self.branch_angle))
            y7 = y3 + self.trunk_length * math.sin(math.radians(-self.branch_angle))

            # Draw the main branches
            self.canvas.create_line(x1, y1, x2, y2, fill="gray")
            self.canvas.create_line(x1, y1, x3, y3, fill="gray")

            # Draw the sub-branches
            self.canvas.create_line(x2, y2, x4, y4, fill="gray")
            self.canvas.create_line(x2, y2, x5, y5, fill="gray")

            #Draw the upper-branches
            self.canvas.create_line(x3, y3, x6, y6, fill="gray")
            self.canvas.create_line(x3, y3, x7, y7)

            # Recursively draw the sub-branches
            self.draw(x2, y2, depth - 1)
            self.draw(x3, y3, depth - 1)
            self.draw(x1, y1, depth - 1)

            # Recursively draw the sub-branches
            self.draw(x4, y4, depth - 1)
            self.draw(x5, y5, depth - 1)
            self.draw(x2, y2, depth - 1)

            #recursively draw upper branches
            self.draw(x6, y6, depth-1)
            self.draw(x7, y7, depth-1)
            self.draw(x3, y3, depth-1)

# Create a RecursiveTree instance
rt = RecursiveTree(canvas)

# Set the trunk length and branching angle
rt.trunk_length = 70
rt.branch_angle = 30

# Draw the fractal at the given position and depth
rt.draw(100, 300, 3)

# Run the main loop
root.mainloop()
