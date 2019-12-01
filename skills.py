from tkinter import *
from tkinter import ttk
import sqlite3
# table headers
headers = ['Skills', 'Ranks']

# get records from db
conn = sqlite3.connect('pathfinder.db')
c = conn.cursor()
c.execute('SELECT skill FROM skills')
skills = c.fetchall()

skillElements = {}

# thing to do on button click
def submitSkills():
    concatQ = []
    for i in skills:
        q = (0, i[0], skillElements[i[0]].get())
        concatQ.append(q)
    with conn:
        c.executemany('INSERT OR REPLACE INTO cSkills VALUES (?, ?, ?)', concatQ)

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
        ttk.Label(parent, text=i).grid(row=counter, column=0)
        skillElements[i[0]] = StringVar()
        skillElements[i[0]].set(0)
        ttk.Entry(parent, textvariable=skillElements[i[0]]).grid(row=counter, column=1)
        counter += 1

    ttk.Button(parent, text="Button", command=submitSkills).grid(row=counter, column=0)