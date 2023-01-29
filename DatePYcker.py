from tkinter import *
from tkcalendar import *

    
ws = Tk()
ws.title("Python Guides")
ws.config(bg="lightblue")


def display_msg():
    date = cal.get_date()
    ws.quit()
    return date 
    

fone = Frame(ws,background='lightblue')
fone.pack(pady=10)

cal = Calendar(
    fone, 
    selectmode="day",
    )

cal.pack(padx=10,pady=10)

actionBtn =Button(
    fone,
    text="Select Date",
    command=display_msg
)
actionBtn.pack()

ws.mainloop()