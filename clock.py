from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")  # Hour:Minute:Second AM/PM appears to use current time as default
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)  # recursive call every 1 second (1000 ms)

window = Tk()

time_label = Label(window, font=("Arial",50), fg="#00FF00", bg="black")
time_label.pack()

day_label = Label(window, font=("Ink Free",25), fg="#00FF00", bg="black")
day_label.pack()

date_label = Label(window, font=("Ink Free",30), fg="#00FF00", bg="black")
date_label.pack()

update()

window.mainloop()
