import tkinter as tk
from tkinter import Tk, BOTTOM, messagebox
from tkinter.ttk import Label, Combobox, Button
from weatherLocation import weatherLocation
from geocode import Location

#-------- Weather Info ----------------

# input_file = open('cityLoc.json')
# cities = json.load(input_file)
# input_file.close()

# def validCity(city) -> bool:
#     if (city in cities):
#         return True
#     return False

majorCities = ["Los Angeles", "San Francisco", "Irvine", "Fresno", "San Diego", "San Juan Capistrano", "Santa Barbara", "Bakersfield"]

#------- Initialize Window -------------
root = Tk()
root.title("Weather Info")
# root.geometry('700x400')

# To fullscreen use this
# root.attributes('-fullscreen', True)
  
#------- GUI Contents ---------------------

def clicked():
    city = weatherCombo.get()
    try:
        l = Location(city)
        wl = weatherLocation(l.getLatitude(), l.getLatitude())
        wl.getTemperature()
        message = wl.__str__()
        messagebox.showinfo('Weather Status', message)
    except:
        messagebox.showinfo('Weather Status', "Sorry, city not recognized.")


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
weatherCombo['values'] = sorted(c for c in majorCities)
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