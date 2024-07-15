from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir='C:\\Users\\thepm\\PycharmProjects\\PythonGUI',
                                    defaultextension='.txt',
                                    filetypes=[
                                        ('Text File', '.txt'),
                                        ('HTML File', '.html'),
                                        ('All Files', '*.*')
                                    ])
    if file is None:
        return
    file_text = str(text.get(1.0, END))
    # file_text = input("Enter text this way instead: ")
    file.write(file_text)
    file.close()

window = Tk()

button = Button(window, text='Save', command=saveFile)
button.pack()
text = Text(window)
text.pack()

window.mainloop()
