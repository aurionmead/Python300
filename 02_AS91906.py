#imports 
from tkinter import *
from tkinter import ttk
import random

item_name_list = {}
item_names = []
######### Class Code #########    Each item in item_names has the same value as the key in item_name_list // value = comic_box.get()  // item_name_list[value].stock 
#create class that holds comic stock levels 
class Comic:
    
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
        global item_name_lis
        item_name_list[self.name] = self
        print(item_name_list)
    
superdude = Comic("Super Dude", 8)
lizardman = Comic("Lizardman", 12)
waterwoman = Comic("WaterWoman", 3)
            


# dislpays class in tandem with drop
for item in item_name_list.keys():
    item_names.append(item)
    
############ Functions ##########
       #Adds Comics to stock level
def restock(self, stock):
    success_sale_message.grid_forget()
    integer_sale_message.grid_forget()
    if stock > 0:
        self.stock += 1
        return True
    else:
        return False
       
        #Subtract Comics from stock level
def withdraw():
    success_sale_message.grid_forget()
    integer_sale_message.grid_forget()
    selected_comic = comic_box.get()
    global item_name_list
    int_stock=0
    item = item_name_list[selected_comic]
    stock = amount_entry.get()
    try:
        int_stock = int(stock)
    except:
        integer_sale_message.grid(row=5, column=2, padx=5, pady=5)
        amount.set("")
    if int_stock > 0 and int_stock <= item.stock:
        item.stock -= int_stock
        amount.set("")
        success_sale_message.grid(row=5, column=2, padx=5, pady=5)
    else:
        amount.set("")
        return False
    
    

########### GUI CODE #####################################################
root = Tk()
root.title("Mead Magazine & Comics")
#fix sizing
root.resizable(False,False)

store_name = ttk.Label(root, text="Welcome to mead Magazines & Comics")
store_name.grid(row=0, column=0, padx=5, pady=5)

##### Left frame Items #####
left_frame = ttk.LabelFrame(root, text="Sell Frame")
left_frame.grid(row=1,column=0, padx=10, pady=10, sticky="NSEW")

#Drop down menu with comic selection in left frame 
comic_box = ttk.Combobox(left_frame, state="readonly", values=item_names)
comic_box.grid(row=2, column=2,  padx=10, pady=10)

# variable to store the amount
amount = DoubleVar()
amount.set("")

#entry to type in amount
amount_entry = ttk.Entry(left_frame, textvariable=amount)
amount_entry.grid(row=3, column=2, padx=10, pady=3, sticky="WE")

#button that removes x number of comics from stock 
sell_button = ttk.Button(left_frame, text="Sell", command=withdraw)
sell_button.grid(row=4, column=2, padx=10, pady=10)

#Comic sale messages
success_sale_message = ttk.Label(left_frame, text="Your sale was sucessful!")


integer_sale_message = ttk.Label(left_frame, text="Your sale was unsucessful, \n   please enter an integer")


#right frame with restock button
right_frame = ttk.LabelFrame(root, text="Restock Frame")
right_frame.grid(row=1,column=1, padx=10, pady=10, sticky="NSEW")

#Drop down menu with comic selection in right frame 
comic_box_right = ttk.Combobox(right_frame, state="readonly", values=item_names)
comic_box_right.grid(row=2, column=2,  padx=10, pady=10)

#button that adds x number of comics to stock 
restock_button = ttk.Button(right_frame, text="Sell", command=restock)
restock_button.grid(row=3, column=2, padx=10, pady=10)

########### END GUI CODE ###################################################


root.mainloop()

