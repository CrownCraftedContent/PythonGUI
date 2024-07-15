from tkinter import *

def openFile():
    print("File has been opened!")
def saveFile():
    print("File has been saved!")

def cut():
    print("You cut some text")
def copy():
    print("You copied some text")
def paste():
    print("You pasted some text")

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0, font=("MV Boli",15))  # tearoff gets rid of first default listing
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=openFile)  # clickable option, image=?, compound=left
file_menu.add_command(label="Save", command=saveFile)  # clickable option
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)  # clickable option

edit_menu = Menu(title="Edit", tearoff=0, font=("MV Boli",15))
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)  # image=?, compound=left
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

window.mainloop()
