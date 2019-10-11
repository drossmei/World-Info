import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from weatherCity import weatherCity
import json

#-------- Weather Info ----------------

input_file = open('cityLoc.json')
cities = json.load(input_file)
input_file.close()

def validCity(city) -> bool:
    if (city in cities):
        return True
    return False

#------- Initialize Window -------------
root = Tk()
root.title("Weather Info")
# root.geometry('700x400')

# To fullscreen use this
root.attributes('-fullscreen', True);
  
#------- GUI Contents ---------------------

def clicked():
    city = weatherCombo.get()
    if (validCity(city)):
        wc = weatherCity(city, cities)
        message = wc.__str__()
        messagebox.showinfo('Weather Status', message)
    else:
        messagebox.showinfo('Weather Status', "Please Enter a Valid City")


# Intialize Title Label
titleLabel = Label(root, text="Weather Info", font=("Courier", 44))
# titleLabel.grid(column=0, row=0)
titleLabel.pack()


#Initialize Weather Label
weatherLabel = Label(root, text="Enter City: ", font=("Courier", 20))
# weatherLabel.grid(column=0, row=1)
weatherLabel.pack(pady=10)


#Initialize Drop Down Menu
weatherCombo = Combobox(root)
weatherCombo['values'] = sorted(c for c in cities.keys())
weatherCombo.current(0)
# weatherCombo.grid(column=1, row=1)
weatherCombo.pack(pady=10)


#Initialize Weather Button 
weatherBtn = Button(root, text="Get Weather", width=20, command=clicked)
# weatherBtn.grid(column=2, row=1)
weatherBtn.pack(pady=10)


#Initialize Exit Button
exitBtn = Button(root, text='Exit', width=20, command=root.destroy)
# exitBtn.grid(column=5, row=10)
exitBtn.pack(side=BOTTOM, pady=50)


root.mainloop()