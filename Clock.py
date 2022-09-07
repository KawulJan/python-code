from tkinter import*
from tkinter.ttk import*

from time import strftime


root =Tk()
root.title("Clock")
def time():
    string =strftime('%H:%M:%S %p')
    Label.config(Text=string)
    Label.after(1000, time)

Label =Label(root, font=("ds-digital", 80), background ="black", foreground ="cyan")
Label.pack(ANCHOR=CENTER)
time()

mainloop()
