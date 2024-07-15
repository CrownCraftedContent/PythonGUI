from tkinter import *
import time

class Ball:
    def __init__(self, canvas, x, y, diameter, x_velocity, y_velocity, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y, diameter, diameter, fill=color)
        self.velocity_x = x_velocity
        self.velocity_y = y_velocity

    def move(self):
        coordinates = self.canvas.coords(self.image)
        print(coordinates)  # shows [topLeftX, topLeftY, bottomRightX, bottomRightY]
        if coordinates[2] >= self.canvas.winfo_width() or coordinates[0] < 0:
            self.velocity_x = self.velocity_x * (-1)
        if coordinates[3] >= self.canvas.winfo_height() or coordinates[1] < 0:
            self.velocity_y = self.velocity_y * (-1)
        self.canvas.move(self.image, self.velocity_x, self.velocity_y)


window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0,0,100,3,1,"white")
tennis_ball = Ball(canvas, 0,0,25,5,3,"yellow")
basket_ball = Ball(canvas, 0, 0, 115, 2, 3, "orange")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
