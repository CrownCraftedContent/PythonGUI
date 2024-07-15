from tkinter import *

def doSomething(event):
    # print("You pressed " + event.keysym)  # keysym = key symbol
    label.config(text=event.keysym)

window = Tk()

# widget.bind(event,function)
window.bind("<Key>",doSomething)  # Return == Enter, Key == All keys

label = Label(window, font=("Helvetica", 100))
label.pack()

window.mainloop()
