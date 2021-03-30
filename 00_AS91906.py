#imports 
from tkinter import *
import random

# Create a variable to store number of stock

######### Class Code #########
#create
class Comic:
    def __init__(self, stock):
        self.stock = stock
        pass
superdude = Comic(root, 8)
lizardman = Comic(root, 12)
waterwoman = Comic(root, 3)

# Functions #


########### GUI CODE #####################################################
root = Tk()
root.title("Mead Magazine & Comics")

#left frame with sell button
left_frame = ttkLabelFrame(root, textvariable="Sell Comic Frame")
left_frame.grid(row=0, coloumn=0, padx=5, pady=5 sticky="NSEW")



########### END GUI CODE #####################################################



root.mainloop()

