from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(title="Open File",  # can set initialdir="\\?"
                                          filetypes=(("Text Files", "*.txt"),
                                          ("All Files", "*.*")))
    file = open(filepath, 'r')  # rt (read text) is default but basically the same as 'r'
    print(file.read())
    file.close()

window = Tk()

button = Button(window, text="Open", command=openFile)
button.pack()

window.mainloop()