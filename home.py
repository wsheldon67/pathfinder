from tkinter import *
from tkinter import ttk
import skills
import character

# tk window
root = Tk()
mainframe = ttk.Frame(root)
mainframe.grid()

# tk notebook
n = ttk.Notebook(mainframe)
n.grid(row=0, column=0)

# skills
skillFrame = ttk.Frame(n)
skillFrame.grid()
n.add(skillFrame, text='Skills')
skills.post(skillFrame)

# character
characterFrame = ttk.Frame(n)
characterFrame.grid()
n.add(characterFrame, text='Character')
character.post(characterFrame)

root.mainloop()