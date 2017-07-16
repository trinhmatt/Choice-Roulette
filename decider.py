import random
from Tkinter import *

choices = []

def add_choice():
    if entry.get() != '':
        choices.append(entry.get())
        choices_display.insert(END,entry.get()+', ')
        entry.delete(0, END)


def choose():
    if choices[0] != '':
        decision = random.randint(0,len(choices)-1)
        final_display.delete(1.0,END)
        final_display.insert(END, 'The decider has chosen ' + choices[decision] + '!')

def clear_choices():
    global choices
    choices = []
    choices_display.delete(1.0,END)
    final_display.delete(1.0,END)


root = Tk()

entry = Entry(root)
add_button = Button(root, text = 'Add choice', command = add_choice)
chooser_button = Button(root, text = 'Choose!', command = choose)
clear_button = Button(root, text = 'Clear choices', command = clear_choices)
choices_label = Label(root, text = "Choices")
choices_display = Text(root, height = 10, width = 40)
final_display = Text(root, height = 5, width = 30)

choices_label.grid(row = 0)
choices_display.grid(row = 1)
final_display.grid(row = 2)
entry.grid(row = 3)
add_button.grid(row = 3,column = 1)
chooser_button.grid(row = 3,column = 2)
clear_button.grid(row = 4)

root.title("Choice Lottery")
root.mainloop()
