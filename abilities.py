from tkinter import *
from tkinter import ttk
import sqlite3
# table headers
headers = ['Skills', 'Ranks', 'Class Bonus']

# get records from db
conn = sqlite3.connect('pathfinder.db')
c = conn.cursor()
# character info
c.execute('SELECT value FROM keyValue WHERE key="race"')
race = c.fetchone()[0]
# abilities
c.execute(f'SELECT ability, score FROM abilities')
skills = c.fetchall()

skillElements = {}

# save skills
def submitSkills():
    concatQ = []
    for i in skills:
        q = (skillElements[i[0]].get(), i[0])
        concatQ.append(q)
    with conn:
        c.executemany('UPDATE skills SET rank=? WHERE skill=?', concatQ)

def post(parent):
    '''Adds skills page to "parent"'''

    # post headers
    headerCounter = 0
    for i in headers:
        ttk.Label(parent, text=i).grid(row=0, column=headerCounter)
        headerCounter += 1

    # post skills as rows, add textvariables to skillElements for use l8r
    counter = 1
    for i in skills:
        ttk.Label(parent, text=i[0]).grid(row=counter, column=0)
        # entry
        skillElements[i[0]] = StringVar()
        skillElements[i[0]].set(i[1])
        ttk.Entry(parent, textvariable=skillElements[i[0]]).grid(row=counter, column=1)
        # class bonuses
        ttk.Label(parent, text=int(i[2])*3).grid(row=counter, column=2)
        counter += 1

    ttk.Button(parent, text="Save", command=submitSkills).grid(row=counter, column=0)

def update():
    print("weo")