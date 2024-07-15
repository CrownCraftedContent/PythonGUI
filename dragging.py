from tkinter import *

def dragStart(event):
    widget = event.widget  # grab widget that triggered event
    widget.start_x = event.x
    widget.start_y = event.y
def dragMotion(event):
    widget = event.widget  # grab widget that triggered event
    x = widget.winfo_x() - label.start_x + event.x  # topLeft corner - start X coord + draggingTo
    y = widget.winfo_y() - label.start_y + event.y
    label.place(x=x,y=y)

window = Tk()

label = Label(window,bg="red",width=10,height=5)
label.place(x=0,y=0)

label_2 = Label(window,bg="red",width=10,height=5)
label_2.place(x=100,y=100)

label.bind("<Button-1>", dragStart)
label.bind("<B1-Motion>", dragMotion)

label_2.bind("<Button-1>", dragStart)
label_2.bind("<B1-Motion>", dragMotion)

window.mainloop()
