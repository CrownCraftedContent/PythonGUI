from tkinter import *

def doSomething(event):
    print("You clicked at: " + str(event.x) + ", " + str(event.y))  # event.x and event.y work for each mouse event

window = Tk()

window.bind("<Button-1>", doSomething)  # Button-1: Left Click, Button-2: Scroll Wheel Click, Button-3: Right Click
window.bind("<ButtonRelease>", doSomething)  # when a mouse button is released
window.bind("<Enter>", doSomething)  # when mouse enters the window
window.bind("<Leave>", doSomething)  # leave the window
window.bind("<Motion>", doSomething)  # when the mouse moves
window.mainloop()
