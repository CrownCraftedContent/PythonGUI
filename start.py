from tkinter import *  # <-- imports everything from that module, all it has to offer

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain widgets

window = Tk()  # instantiate an instance of a window
window.geometry("420x420")
window.title("Prince's Window")

# icon = PhotoImage(file='')  # must create a PhotoImage for proper window icon format
# window.iconphoto(True, icon)

# config for making changes to the window
window.config(background="black")  # color name or hexadecimal (search hex color picker)
window.config(background="#5cfcff")  # #hexadecimal is the format
window.mainloop()  # display our window, listen for events