from tkinter import *
from tkinter import ttk
import create

def createCharacter():
    createWindow = Toplevel(root)
    create.post(createWindow)

root = Tk()
root.option_add("*tearOff", FALSE)

menubar = Menu(root)
root['menu'] = menubar
menu_file = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
menu_file.add_command(label='Create a Character', command=createCharacter)

root.mainloop()