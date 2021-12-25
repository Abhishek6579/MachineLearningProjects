import csv
import random
field_names = ['age', 'PT', 'ST', 'tut', 'heal','conc', 'marks']

entries = []
def getMarks(age, pt, st, tut, heal, conc):
    sum = (age + st + tut + heal + conc -pt*5)
    frac = int(sum / 250 * 100)
    if frac > 100:
        frac = frac - (frac- 100) - pt * 2
    return frac

def enter():
    global entries
    i = 0
    marks  = 0
    dic = {}
    while i <= 1000:
        if True:
            age = random.randint(16, 22)
            pt = random.randint(1, 3)
            st = random.randint(1,10)
            tut = random.randint(0,100)
            heal = random.randint(1,100)
            conc = random.randint(1,100)
            marks = getMarks(age, pt, st, tut, heal, conc)
        dic['age'] = age
        dic['PT'] = pt
        dic['ST'] = st
        dic['tut'] = tut
        dic['heal'] = heal
        dic['conc'] = conc
        dic['marks'] = marks
        # print(dic)
        entries.append(dic.copy())
        i = i+1


    return
enter()
with open('data.csv','w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(entries)