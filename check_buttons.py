from tkinter import *

def display():
    if (x.get()==1):
        print("You agree")
    else:
        print("You don't agree")

window = Tk()

x = IntVar()  # or BooleanVar or StringVar etc., Int 1 and 0 is the default

photo = PhotoImage(file='python-logo.png')

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,  # value stored in variable when toggled on (by default is 1)
                           offvalue=0,
                           command=display,
                           font=('Impact', 20),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound='right')  # where the photo gets added relative to text

check_button.pack()

window.mainloop()