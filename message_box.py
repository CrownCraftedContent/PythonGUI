from tkinter import *
from tkinter import messagebox  # imports the messagebox library

def click():
    # v display a simple message
    #messagebox.showinfo(title='Message Box',message='Here is the message')
    # v can be put in a while True to make non-ending
    #messagebox.showwarning(title='WARNING', message='You have a virus!')
    #messagebox.showerror(title='ERROR!',message='Something went wrong')
    # v this returns True/False
    #if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing?'):
        #print("You did a thing")
    #else:
        #print("You canceled the thing")
    #if messagebox.askretrycancel(title='retry cancel',message='Do you want to retry the thing?'):
        #print("You retried a thing")
    #else:
        #print("You canceled instead of retrying")
    #if messagebox.askyesno(title='ask yes or no',message='Do you like dogs?'):
        #print("I also like dogs.")
    #else:
        #print("That's just weird.")
    #answer = messagebox.askquestion(title='Ask Question',message='Do you like pie?')
    #if answer == 'yes':
        #print('I like pie too')
    #else:
        #print("Why do you not like pie?")
    answer = messagebox.askyesnocancel(title='Yes No or Cancel',message='Do you like to code?',icon='info')  # also icon = 'warning','error'
    if answer==True:
        print("You like to code!")
    elif answer==False:
        print("Then why are you viewing this?")
    else:
        print("You have dodged the question!")

window = Tk()

button = Button(window, command=click, text="Click me")
button.pack()

window.mainloop()
