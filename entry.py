from tkinter import *

# entry widget = textbox that accepts a single line of user input

def submit():
    password = entry.get()
    print("Hello", password)
    entry.config(state=DISABLED)  # config function for post alterations
def delete():
    entry.delete(0,END)  # all characters from start to end
def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,
              font=("Impact", 50),
              fg="#00FF00",
              bg="black",
              show="*")  # display characters as something else, like for passwords

# entry.insert(0,"Enter text here")  # <-- starter text
entry.pack(side=LEFT)

submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()
