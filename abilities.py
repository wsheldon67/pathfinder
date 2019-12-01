from tkinter import *
from tkinter import ttk
import sqlite3
import config
import myMod
import math
# configs
headers = ['Ability', 'Points', 'Cost', 'Racial', 'Score', 'Mod']
# get records from db
conn = sqlite3.connect('pathfinder.db')
c = conn.cursor()
# character info
c.execute('SELECT value FROM keyValue WHERE key="race"')
race = c.fetchone()[0]
# abilities
c.execute('SELECT ability, score FROM abilities')
abilities = c.fetchall()
# race info
c.execute('SELECT con, wis, cha, dex, str, int FROM races WHERE Race=?', [race])
racialModifiers = myMod.sqlParseOne(c.fetchone(), config.abilities)

abilityElements = {}


def save():
    
    concatQ = []
    for i in abilities:
        q = (abilityElements[i[0]].get(), i[0])
        concatQ.append(q)
    with conn:
        c.executemany('UPDATE abilities SET score=? WHERE ability=?', concatQ)

def post(parent):
    '''Adds ability page to "parent"'''
    # total points
    ttk.Label(parent, text="Remaining Points:").grid(row=0, column=0)
    global pointsRemaining
    pointsRemaining = StringVar()
    pointsRemaining.set(config.abilityPoints)
    ttk.Label(parent, textvariable=pointsRemaining).grid(row=0, column=1)
    # headers
    headerCounter = 0
    for i in headers:
        ttk.Label(parent, text=i).grid(row=1, column=headerCounter)
        headerCounter += 1

    # post abilities as rows, add textvariables to abilityElements for use l8r
    counter = 2
    for i in abilities:
        ttk.Label(parent, text=i[0]).grid(row=counter, column=0)
        # entry
        abilityElements[i[0]] = StringVar()
        abilityElements[i[0]].set(10)
        ttk.Entry(parent, textvariable=abilityElements[i[0]], validate='focusout', validatecommand=update).grid(row=counter, column=1)
        # row labels - no data
        abilityElements[i[0]+'cost'] = StringVar()
        abilityElements[i[0]+'mod'] = StringVar()
        abilityElements[i[0]+'race'] = StringVar()
        abilityElements[i[0]+'score'] = StringVar()
        ttk.Label(parent, textvariable=abilityElements[i[0]+'cost']).grid(row=counter, column=2)
        ttk.Label(parent, textvariable=abilityElements[i[0]+'mod']).grid(row=counter, column=5)
        ttk.Label(parent, textvariable=abilityElements[i[0]+'race']).grid(row=counter, column=3)
        abilityElements[i[0]+'race'].set(racialModifiers[i[0]])
        ttk.Label(parent, textvariable=abilityElements[i[0]+'score']).grid(row=counter, column=4)
        counter += 1

    # submit
    global saveButton
    saveButton = ttk.Button(parent, text="Save")
    saveButton.grid(row=8, column=0)

def update():
    spentPoints = 0
    for i in abilities:
        # validate value is between 7 & 18
        v = int(abilityElements[i[0]].get())
        if v < config.minAbilityPoints:
            abilityElements[i[0]].set(config.minAbilityPoints)
        elif v > config.maxAbilityPoints:
            abilityElements[i[0]].set(config.maxAbilityPoints)
        # cost
        abilityElements[i[0]+'cost'].set(config.costTable[int(abilityElements[i[0]].get())])
        spentPoints += int(abilityElements[i[0]+'cost'].get())
        # score
        abilityElements[i[0]+'score'].set(int(abilityElements[i[0]].get()) + int(abilityElements[i[0]+'race'].get()))
        # mod
        cScore = int(abilityElements[i[0]+'score'].get())
        abilityElements[i[0]+'mod'].set(math.floor((cScore - 10)/2))
    # totals, disable button if points < 0
    pointsRemaining.set(config.abilityPoints - spentPoints)
    if int(pointsRemaining.get()) < 0:
        saveButton.state(["disabled"])
    else:
        saveButton.state(["!disabled"])