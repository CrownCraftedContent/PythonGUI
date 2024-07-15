from tkinter import *

# grid() = geometry manager that organizes widgets in a table-like structure

# column widths expand to accommodate largest widget size

window = Tk()

title_label = Label(window, text="Enter your info", font=("Arial", 25)).grid(row=0, column=0, columnspan=2)

first_name_label = Label(window, text="First Name: ").grid(row=1, column=0)
first_name_entry = Entry(window).grid(row=1, column=1)

last_name_label = Label(window, text="Last Name: ").grid(row=2, column=0)
last_name_entry = Entry(window).grid(row=2, column=1)

email_label = Label(window, text="Email: ").grid(row=3, column=0)
email_entry = Entry(window).grid(row=3, column=1)

submit_button = Button(window, text="Submit").grid(row=4, column=0, columnspan=2)  # take up two spaces, is placed btw.



window.mainloop()
