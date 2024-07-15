from tkinter import *
from tkinter.ttk import *
import time

def start():
    tasks = 87  # in GB
    tmp = 0
    speed = 3
    wait_time = 1
    while tmp < tasks:
        time.sleep(1)
        bar['value'] += ((speed * wait_time) / tasks) * 100  # out of 100
        tmp += (speed * wait_time)
        text.set(str(tmp) + "/" + str(tasks) + " GB completed")
        percent.set(str(round((tmp/tasks)*100, 2))+"%")
        window.update_idletasks()  # updates progress bar during each iteration

window = Tk()

percent = StringVar()  # allows us to update it with new text
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)  # length is about 100 by default
bar.pack(pady=10)

percent_label = Label(window, textvariable=percent).pack()
task_label = Label(window, textvariable=text).pack()

button = Button(window, text="Download", command=start).pack()

window.mainloop()
