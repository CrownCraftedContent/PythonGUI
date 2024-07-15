from tkinter import *
from tkinter import ttk  # several extra widgets

window = Tk()

notebook = ttk.Notebook(window)  # widget that manages a collection windows/displays

tab1 = Frame(notebook)  # new frame for tab 1
tab2 = Frame(notebook)  # new frame for tab 2

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both")     # expand = expand to fill any space not otherwise used
                                            # fill = fill space on x and y axes
Label(tab1, text="Hello this is Tab #1.",width=50,height=25).pack()  # height = width/2 for double-spacing?
Label(tab2, text="Goodbye, this is Tab #2", width=50, height=25).pack()

window.mainloop()