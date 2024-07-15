# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window, bg="pink", bd=5, relief=SUNKEN)  # bd = border width, relief = border type (SUNKEN, RAISED, ETC)
frame.pack(side=BOTTOM)  # or place
frame.place(x=0,y=0)  # for exact coordinates

Button(frame, text="W", font=("Consolas",25), width=3).pack(side=TOP)
Button(frame, text="A", font=("Consolas",25), width=3).pack(side=LEFT)
Button(frame, text="S", font=("Consolas",25), width=3).pack(side=LEFT)
Button(frame, text="D", font=("Consolas",25), width=3).pack(side=LEFT)

window.mainloop()
