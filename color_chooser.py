from tkinter import *
from tkinter import colorchooser  #submodule

def click():
    # color = colorchooser.askcolor()  # RGB, Hexadecimal
    # print("You have chosen", color)
    # colorHex = color[1]  # <-- hex value
    # window.config(bg=colorHex)  # change background color to what we've chosen
    #  ^ aka v
    window.config(bg=colorchooser.askcolor()[1])

window = Tk()
window.geometry("420x420")

button = Button(window, text='click me', command=click)
button.pack()

window.mainloop()
