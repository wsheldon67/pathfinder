from tkinter import *
from tkinter import ttk
import skills
import createCharacter

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

# character manager
characterManagerFrame = ttk.Frame(n)
characterManagerFrame.grid()
n.add(characterManagerFrame, text='Manage Characters')
characterManagerNotebook = ttk.Notebook(characterManagerFrame)
characterManagerNotebook.grid(row=0, column=0)
# character create
createCharacterFrame = ttk.Frame(characterManagerNotebook)
createCharacterFrame.grid()
characterManagerNotebook.add(createCharacterFrame, text='Create')
createCharacter.post(createCharacterFrame)

root.mainloop()