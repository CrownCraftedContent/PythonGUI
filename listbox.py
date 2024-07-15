# listbox = A listing of selectable text items within its own container
from tkinter import *

def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    # print("You have ordered", listbox.get(listbox.curselection()))
    print("You have ordered:")
    for index in food:
        print(index)
def add():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())

def delete():
    # listbox.delete(listbox.curselection())
    for index in reversed(listbox.curselection()):  # reversed because indices change after each deletion
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Constantia',35),
                  width=12,
                  selectmode=MULTIPLE
                  )
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

# print("Setting listbox height to", listbox.size())

listbox.config(height=listbox.size())

entry_box = Entry(window)
entry_box.pack()

submit_button = Button(window, text="Submit",command=submit)
submit_button.pack()

add_button = Button(window, text="Add",command=add)
add_button.pack()

delete_button = Button(window, text="Delete",command=delete)
delete_button.pack()

window.mainloop()
