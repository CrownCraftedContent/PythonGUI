from tkinter import *

def createWindow():
    new_window = Tk()           # Toplevel() =  new window 'on top' of other windows. Usually linked to a 'bottom' window
                                                # closes with the bottom level, but bottom doesn't close with top levels
                                # Tk() =        new independent window, not linked to old window
    start_window.destroy()      # close out of old window

start_window = Tk()

Button(start_window, text="Create new window", command=createWindow).pack()

start_window.mainloop()
