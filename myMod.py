def sqlParseUnique(o,h):
    """ o is fetchall(), h is list with column names in order"""
    r = {}
    for i in o:
        r[i[0]] = {}
        counter = 0
        for j in i:
            r[i[0]][h[counter]] = j
            counter += 1
    return r

def sqlParseOne(o,h):
    """ o is fetchone(), h is list with column names in order"""
    r = {}
    counter = 0
    for j in o:
        r[h[counter]] = j
        counter += 1
    return r