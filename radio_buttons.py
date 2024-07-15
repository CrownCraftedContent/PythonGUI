# radio button = similar to checkbox, but you can only select one from a group
from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    if (x.get() == 0):
        print("You ordered pizza!")
    elif (x.get() == 1):
        print("You ordered a hamburger!")
    elif (x.get() == 2):
        print("You ordered a hotdog!")
    else:
        print("What happened here?")

window = Tk()

# Create images after window for some reason


x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x,  # groups radiobuttons together if they share the same variable
                              value=index,  # assigns each radiobutton a different value
                              padx=25,
                              #  image=food_images[index], adds image to radiobutton
                              #  compound='left'
                              # indicatoron=0,  # eliminate circle indicators
                              # width=375,  # set width of radio buttons manually
                              font=('Impact', 50),
                              command=order)
    radiobutton.pack(anchor=W)  # or 'w'  <-- means align to West

window.mainloop()