from tkinter import *
from tkinter import ttk
import skills
import characterManager

# tk window
root = Tk()
mainframe = ttk.Frame(root)
mainframe.grid()

# tk notebook
n = ttk.Notebook(mainframe)
n.grid(row=0, column=0)
skillFrame = ttk.Frame(n)
skillFrame.grid()
characterManagerFrame = ttk.Frame(n)
characterManagerFrame.grid()
n.add(skillFrame, text='Skills')
n.add(characterManagerFrame, text='Manage Characters')

skills.post(skillFrame)
characterManager.post(characterManagerFrame)

root.mainloop()