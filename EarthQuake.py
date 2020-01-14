"""
Title: Earthquake
Date: 2020-01-13
Authour: Dhiraj Meenavilli
"""

earthquakes = []

Alaska = ['ALASKA']
Hawaii = ['HAWAII']
Panama = ['PANAMA']
Missouri = ['MISSOURI']
Indonesia = ['INDONESIA']
Vanuatu = ['VANUATU']
Mexico = ['MEXICO']
Complete = [Alaska,Hawaii,Panama,Missouri,Indonesia,Vanuatu,Mexico]

places = ['ALASKA','HAWAII','PANAMA','MISSOURI','INDONESIA','VANUATU','MEXICO']
fil = "earthquake.txt"
fil2 = ' earthquakefmt.txt'
f = open(fil,'r')
f = f.read().split("\n")

for i in range(len(f)):
    earthquakes.append(f[i])

earthquakes.sort()

for i in range(len(places)):
    for j in range(len(earthquakes)):
        if places[i] in earthquakes[j]:
            earthquake = earthquakes[j].split()
            Complete[i].append("["+earthquake[1])
            Complete[i].append(earthquake[0]+"]")

f_two = open(fil2,'w')

for i in range(len(Complete)):
    f_two.write("[")
    for j in range(len(Complete[i])):
        f_two.write(Complete[i][j])
        if not j >= (len(Complete[i])- 1):
            f_two.write(", ")
    f_two.write("]" + "\n\n")

f_two.close()
