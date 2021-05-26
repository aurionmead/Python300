#imports 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

item_name_list = {}
item_names = []

root = Tk()
root.title("Mead Magazine & Comics")
#Auto sizing
root.resizable(False,False)


######### Class Code #########    Each item in item_names has the same value as the key in item_name_list // value = comic_box.get()  // item_name_list[value].stock 
#create class that holds comic stock levels 
class Comic:
    
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
        global item_name_list
        item_name_list[self.name] = self
        print(item_name_list)
    
superdude = Comic("Super Dude", 8)
lizardman = Comic("Lizardman", 12)
waterwoman = Comic("WaterWoman", 3)
stock_display_string = StringVar()            


# dislpays class in tandem with drop
for item in item_name_list.keys():
    item_names.append(item)
    
############ Functions #######################################################
       #Adds Comics to stock level
def restock():
    restock_success_message.grid_forget()
    restock_integer_message.grid_forget()
    selected_comic = comic_box_right.get()
    global item_name_list
    int_stock=0
    item = item_name_list[selected_comic]
    stock = restock_amount_entry.get()
    try:
        int_stock = int(stock)
    except:
        restock_integer_message.grid(row=5, column=2, padx=5, pady=5)
        restock_amount.set("")
    if int_stock > 0:
        item.stock += int_stock
        restock_amount.set("")
        restock_success_message.grid(row=5, column=2, padx=5, pady=5)
    else:
        restock_amount.set("")
        return False
    update_stock_display()

       
        #Subtract Comics from stock level
def sell():
    selected_comic = comic_box.get()
    global item_name_list
    item = item_name_list[selected_comic]
    if 1 <= item.stock:
        item.stock -= 1
        messagebox.showinfo("Comic Sold", "Enjoy your comic")
    elif item.stock == 0:                                                           
        messagebox.showerror("Out of Stock!","You don't have enough in stock to perform this action.")
    else:
        return False
    update_stock_display()
    
def update_stock_display():
    tempstring = ""
    for v in item_name_list.values():
        tempstring += "{}:  {}\n".format(v.name, v.stock)
    stock_display_string.set(tempstring)
update_stock_display()
########### GUI CODE #####################################################


store_name = ttk.Label(root, text="Welcome to Mead Magazines & Comics")
store_name.grid(row=0, column=1, padx=5, pady=5)

##### Left frame Items #####
#left frame with sell button
left_frame = ttk.LabelFrame(root, text="Sell Frame")
left_frame.grid(row=1,column=0, padx=10, pady=10, sticky="NSEW")

#Drop down menu with comic selection in left frame 
comic_box = ttk.Combobox(left_frame, state="readonly", values=item_names)
comic_box.grid(row=2, column=2,  padx=10, pady=10)


#button that removes x number of comics from stock 
sell_button = ttk.Button(left_frame, text="Sell", command=sell)
sell_button.grid(row=4, column=2, padx=10, pady=10)

#### Center Frame ####
center_frame = ttk.LabelFrame(root, text="Stock Display Frame")
center_frame.grid(row=1,column=1, padx=10, pady=10, sticky="NSEW")

#display of stock
stock_display = ttk.Label(center_frame, textvariable=stock_display_string)
stock_display.grid(row=0, column=0)

sold_stock_display = ttk.Label(center_frame, textvariable=stock_display_string)
sold_stock_display.grid(row=0, column=0)

#### Right Frame Items #### 
#right frame with restock button
right_frame = ttk.LabelFrame(root, text="Restock Frame")
right_frame.grid(row=1,column=2, padx=10, pady=10, sticky="NSEW")

#Drop down menu with comic selection in right frame 
comic_box_right = ttk.Combobox(right_frame, state="readonly", values=item_names)
comic_box_right.grid(row=2, column=2,  padx=10, pady=10)

# variable to store the amount
restock_amount = DoubleVar()
restock_amount.set("")

#entry to type amount that restocks
restock_amount_entry = ttk.Entry(right_frame, textvariable=restock_amount)
restock_amount_entry.grid(row=3, column=2, padx=10, pady=3, sticky="WE")

#comic restock message
restock_success_message = ttk.Label(right_frame, text="Your restock was sucessful!")

restock_integer_message = ttk.Label(right_frame, text="Your restock was unsucessful. \n   Please enter an integer")

#button that adds x number of comics to stock 
restock_button = ttk.Button(right_frame, text="Restock", command=restock)
restock_button.grid(row=4, column=2, padx=10, pady=10)

########### END GUI CODE ###################################################


root.mainloop()

