from tkinter import *
from tkinter import ttk
import skills
import character
import abilities

def post(parent):
    # tk window
    mainframe = ttk.Frame(parent)
    mainframe.grid()

    # tk notebook
    n = ttk.Notebook(mainframe)
    n.grid(row=0, column=0)

    def displayAbility():
        # abilities
        character.save()
        abilityFrame = ttk.Frame(n)
        abilityFrame.grid()
        n.add(abilityFrame, text='Abilities')
        abilities.post(abilityFrame)
        abilities.saveButton['command'] = displaySkill
        character.saveButton.state(['disabled'])

    def displaySkill():
        # skills
        abilities.save()
        skillFrame = ttk.Frame(n)
        skillFrame.grid()
        n.add(skillFrame, text='Skills')
        skills.post(skillFrame)
        ttk.Button(skillFrame, text='Save', command=skills.save)
        abilities.saveButton.state(['disabled'])

    # character
    characterFrame = ttk.Frame(n)
    characterFrame.grid()
    n.add(characterFrame, text='Character')
    character.post(characterFrame)
    character.saveButton['command'] = displayAbility

