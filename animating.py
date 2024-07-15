from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
x_velocity = 1
y_velocity = 1

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

background_photo = PhotoImage(file='Screenshot.png')
bg_image = canvas.create_image(0,0,image=background_photo,anchor=NW)

photo_image = PhotoImage(file='python-logo.png')
my_image = canvas.create_image(250, 250, image=photo_image, anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if (coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0):
        x_velocity = x_velocity * (-1)
    if (coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0):
        y_velocity = y_velocity * (-1)
    canvas.move(my_image, x_velocity, y_velocity)
    window.update()  # for any changes
    time.sleep(0.01)

window.mainloop()  # this code will somehow be reached
