from tkinter import *

# button = click for functionality

count = 0
def click():
    global count
    count += 1
    print(count)

window = Tk()

photo = PhotoImage(file='Screenshot.png')

button = Button(window,
                text="Click me",
                command=click,  # callback instead of () for function call
                font=("Comic Sans",30),
                fg="#00FF00",  # font color
                bg="black",
                activeforeground="#00FF00",  # colors while clicking
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="bottom")
button.pack()

window.mainloop()
