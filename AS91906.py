#imports 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

#Allows for computer to convert binary for comic name into the actual name value eg. Super Dude
item_name_list = {}
item_names = []

root = Tk()
root.title("Mead Magazine & Comics")
#Auto sizing
root.resizable(False,False)


######### Class Code #########    
#create class that holds comic stock levels 
class Comic:
    
    def __init__(self, name, stock, sold):
        self.name = name
        self.stock = stock
        self.sold = sold
        global item_name_list
        item_name_list[self.name] = self

    
superdude = Comic("Super Dude", 8, 0)
lizardman = Comic("Lizardman", 12, 0)
waterwoman = Comic("WaterWoman", 3, 0)
stock_display_string = StringVar()
sold_display_string = StringVar()


#dislpays class in tandem with drop
for item in item_name_list.keys():
    item_names.append(item)
    
############ Functions #######################################################
    
#Adds Comics to stock level within parameters
def restock():
    if comic_box_right.get() == "":
        messagebox.showerror("No comic selected!","Please select a comic and try again!")
        return
    restock_success_message.grid_forget()
    selected_comic = comic_box_right.get()
    global item_name_list
    int_stock=0
    item = item_name_list[selected_comic]
    stock = restock_amount_entry.get()
    try:
        int_stock = int(stock)
    except:
        messagebox.showerror("Error", "Your restock was unsuccessful. \n   Please enter an integer")
        restock_amount.set("")
    if int_stock > 0:
        item.stock += int_stock
        restock_amount.set("")
        restock_success_message.grid(row=5, column=2, padx=5, pady=5)
    else:
        restock_amount.set("")
        return False
    update_stock_display()
    ("")

#Subtract Comics from stock level
def sell():
    if comic_box.get() == "":
        messagebox.showerror("No comic selected!","Please select a comic and try again!")
        return
    sale_success_message.grid_forget()
    selected_comic = comic_box.get()
    global item_name_list
    item = item_name_list[selected_comic]
    if 1 <= item.stock:
        item.stock -= 1
        item.sold += 1
        sale_success_message.grid(row=5, column=2, padx=5, pady=5)
    elif item.stock == 0:                                                           
        messagebox.showerror("Out of Stock!","You don't have enough in stock to perform this action.")
    else:
        return False
    update_stock_display()
    
            
# Adds complexity by keeping a receipt                
def get_data():
  account_file = open("accounts.txt","r")
  line_list = account_file.readlines()

  for line in line_list:
    account_data = line.strip().split(",")
    Comic(*account_data)

  account_file.close()

#updates stock display level
def update_stock_display():
    account_file = open("accounts.txt", "w")
    tempstring = ""
    tempstring2 = ""
    for v in item_name_list.values():
        tempstring += "{}:  {}\n".format(v.name, v.stock)
        tempstring2 += "{}:  {}\n".format(v.name, v.sold)
    stock_display_string.set(tempstring)
    sold_display_string.set(tempstring2)
    account_file.write("{}: {}\n{}: {}\n{}: {}\n".format(superdude.name, superdude.stock, lizardman.name, lizardman.stock, waterwoman.name, waterwoman.stock))
    account_file.close()
update_stock_display()

########### GUI CODE ##########################################################################################################


#### Top Frame ####

#topframe with welcome message
top_frame = ttk.LabelFrame(root, text="MM&C")
top_frame.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="NSEW")

#Label for welcome message
store_name = ttk.Label(top_frame, text="Welcome to Mead Magazines & Comics")
store_name.grid(row=0, column=0, padx=5, pady=5)

#### End Top Frame ####



##### Left frame Items ####

#left frame with sell button
left_frame = ttk.LabelFrame(root, text="Sell Comics")
left_frame.grid(row=1,column=0, padx=10, pady=10, sticky="NSEW")

#Drop down menu with comic selection in left frame 
comic_box = ttk.Combobox(left_frame, state="readonly", values=item_names)
comic_box.grid(row=2, column=2, padx=10, pady=10)


#button that removes x number of comics from stock 
sell_button = ttk.Button(left_frame, text="Sell", command=sell)
sell_button.grid(row=4, column=2, padx=10, pady=10)

sale_success_message = ttk.Label(left_frame, text="Your sale was successful!\n     Enjoy your comic")

##### End Left frame Items #####



#### Center Frame Items #####

#center left frame with stock display
center_frame = ttk.LabelFrame(root, text="Stock Display")
center_frame.grid(row=1,column=1, padx=10, pady=10, sticky="NSEW")

#display of stock
stock_display = ttk.Label(center_frame, textvariable=stock_display_string)
stock_display.grid(row=0, column=0, padx=10, pady=10)

#### End Center Frame Items #####



#### Sold Comics Frame #####

#center right frame with amt sold comics
sold_comics_frame = ttk.LabelFrame(root, text="Sales History")
sold_comics_frame.grid(row=1,column=2, padx=10, pady=10, sticky="NSEW")

#display sold comic count
sold_stock_display = ttk.Label(sold_comics_frame, textvariable=sold_display_string)
sold_stock_display.grid(row=0, column=0, padx=10, pady=10)

#### End Sold Comics Frame #####




#### Right Frame Items ####

#right frame
right_frame = ttk.LabelFrame(root, text="Restock Comics")
right_frame.grid(row=1,column=3, padx=10, pady=10, sticky="NSEW")

#Drop down menu with comic selection in right frame  linked to class values
comic_box_right = ttk.Combobox(right_frame, state="readonly", values=item_names)
comic_box_right.grid(row=2, column=2,  padx=10, pady=10)

#variable to store the amount
restock_amount = DoubleVar()
restock_amount.set("")

#entry to type amount that restocks
restock_amount_entry = ttk.Entry(right_frame, textvariable=restock_amount)
restock_amount_entry.grid(row=3, column=2, padx=10, pady=3, sticky="WE")

#comic restock message
restock_success_message = ttk.Label(right_frame, text="Your restock was successful!")

#button that adds x number of comics to stock 
restock_button = ttk.Button(right_frame, text="Restock", command=restock)
restock_button.grid(row=4, column=2, padx=10, pady=10)

#### End Right Frame Items ####



########### END GUI CODE ###################################################


root.mainloop()

