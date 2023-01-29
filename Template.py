from tkinter import *
from tkinter import ttk

root = Tk()


def DoSomething(number):
    print(number)

Radiobutton(root,text = 'Click Me', indicatoron= 0, command=lambda: DoSomething('Clicked')).pack(fill = BOTH)


root.mainloop()
