from tkinter import *
from tkinter import ttk
import sqlite3
# table headers
headers = ['Skills', 'Ranks']

# get records from db
conn = sqlite3.connect('pathfinder.db')
c = conn.cursor()
# skills
c.execute('SELECT skill, rank FROM skills')
skills = c.fetchall()
print(skills)

skillElements = {}

# thing to do on button click
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
        skillElements[i[0]] = StringVar()
        skillElements[i[0]].set(i[1])
        ttk.Entry(parent, textvariable=skillElements[i[0]]).grid(row=counter, column=1)
        counter += 1

    ttk.Button(parent, text="Save", command=submitSkills).grid(row=counter, column=0)