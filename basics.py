from tkinter import *  # <-- imports everything from that module, all it has to offer

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain widgets

# WINDOW
window = Tk()  # instantiate a window instance
window.geometry("420x420")
window.title("Prince's Window")

# icon = PhotoImage(file='')  # must create a PhotoImage for proper window icon format
# window.iconphoto(True, icon)

# config for making changes to the window
window.config(background="black")  # color name or hexadecimal (search hex color picker)
window.config(background="#5cfcff")  # #hexadecimal is the format

photo = PhotoImage(file='Screenshot.png')  # jpg doesn't seem to work

# LABEL
# label = Label(window, text = "Hello world", font=('Arial',40,'bold'), fg='green', bg='black')  # window == container
# ^ for simplicity
label = Label(window,
              text="Hello world",
              font=('Arial',40,'bold'),
              fg='green',  # foreground (font color)
              bg='black',  # background
              relief=RAISED,  # border relief options (also SUNKEN, etc.)
              bd=10,  # border width
              padx=20,  # padding between text and border (x axis, 20 pixels)
              pady=20,    # "" except for y axis
              image=photo,   # places photo over text
              compound='bottom')  # positions image according to text
# fg == foreground (font) color, pass in color name or hex value
# bg == background color

label.pack()  # adds it to the window by default
# label.place(x=0,y=0)  # set to a specific location
# there are more options...

window.mainloop()  # display our window, listen for events
