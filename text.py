# text widget = functions like a text pad/area, you can enter MULTIPLE lines of text
from tkinter import *

def submit():
    input = text.get("1.0",END)  # 1.0 = first line
    print(input)

window = Tk()

text = Text(window, bg='light yellow',
            font=('Ink Free',25),  # text size corresponds directly with font size
            height=8,  # amount of characters tall
            width=20,  # amount of characters wide
            padx=20,
            pady=20,
            fg='purple')
text.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()