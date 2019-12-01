from tkinter import *
from tkinter import ttk
import sqlite3

# get info from db
conn = sqlite3.connect('pathfinder.db')
c = conn.cursor()
# get races
c.execute('SELECT race FROM races')
races = []
for i in c.fetchall():
    races.append(i[0])

# get classes
c.execute('SELECT class FROM classes')
classes = []
for i in c.fetchall():
    classes.append(i[0])

def save():
    global raceSelect
    print(raceSelect.curselection())
    selectedRace = races[raceSelect.curselection()[0]]
    global classSelect
    print(classSelect.curselection())
    selectedClass = classes[classSelect.curselection()[0]]
    global characterName
    selectedName = characterName.get()
    print(selectedName)


def post(parent):
    # name
    ttk.Label(parent, text="Name").grid(row=1, column=0)
    global characterName
    characterName = StringVar()
    ttk.Entry(parent, textvariable=characterName).grid(row=2, column=0, sticky='N')
    # race
    ttk.Label(parent, text="Race").grid(row=1, column=1)
    raceList = StringVar(value=races)
    global raceSelect
    raceSelect = Listbox(parent, listvariable=raceList, height=15)
    raceSelect.grid(row=2, column=1)
    # class
    ttk.Label(parent, text="Class").grid(row=1, column=2)
    classList = StringVar(value=classes)
    global classSelect
    classSelect = Listbox(parent, listvariable=classList, height=15)
    classSelect.grid(row=2, column=2)
    # submit
    ttk.Button(parent, text="Save", command=save).grid(row=3, column=0, sticky='N')