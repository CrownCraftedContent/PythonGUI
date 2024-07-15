from tkinter import *

def submit():
    print("The temperature is", scale.get(), "degrees C")  # or + str(scale.get()) +

window = Tk()

# create & pack a hot image here

scale = Scale(window,
              from_=100,  # needs underscore after from
              to=0,
              length=600,
              # orient=HORIZONTAL,  # orientation of scale (VERTICAL/HORIZONTAL)
              font=('Consolas',20),
              tickinterval=10,  # adds numeric indicators
              showvalue=0,  # hide current value
              resolution=5,  # increment amount of slider
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='#111111'
              )

# scale.set(50)  # set current value of slider
scale.set(((scale['from']-scale['to'])/2)+scale['to'])  # ((max - min) / 2) + min
scale.pack()

# create & pack a cold image here

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()
