"""
Title: Orders
Date: 01-18-2020
Authpur: Dhiraj Meenavilli
"""

#- First step is to open the files and load them in on read -#
def openFile(fileName):
    fileObject = open(fileName,'r')
    fileObject = fileObject.read()
    return fileObject

def breakText(textFile, seperator, newLines = True, otherSeperator = True):
    if newLines:
        textFile = textFile.split('\n')
        if otherSeperator:
            for i in range(len(textFile)):
                textFile[i] = textFile[i].split(seperator)
    else:
        textFile = textFile.split(seperator)

    return textFile

products = openFile("products.txt")
suppliers = openFile("suppliers.txt")
availability = openFile("availability.txt")
onshelves = openFile("onshelves.txt")

## -- Although I could have loaded them all in at once I believe it's easier for me to keep track of things by seperating them like this, that is the only reason why I did this. -- ##

#- Second step is to see if any of the products are below 20 units -#

## -- To do the second step I have to turn the text file into a list, which I can then mess around with.

onshelves = breakText(onshelves,'#')

#- Third step is if there are less then 20 than an order must be placed so that there are 50 in stock -#

needed = [] ##-- This will store the items call number and amount required
n = 0

for i in range(len(onshelves)):
    if int(onshelves[i][1]) < 20:
        needed.append([])
        needed[n].append(onshelves[i][0])
        needed[n].append(50-int(onshelves[i][1]))
        n += 1

#- Fourth step is to find the cheapest supplier of the items which are less then 20 -#

## -- To do this fourth step, I need to break the availability text and then compare it against the array of needed. As well find the cheapest supplier

### --- To find the cheapest supplier, I can simply compare all suppliers for a product then filter them into a new array from which I can match the needed array.

availability = breakText(availability,",")
availability.sort() # This way same products will be placed next to each other, regardless of the order the raw data is entered
#print(availability)

cheapest = [] # This will store which suppliers supply a given product at the cheapest point.
chosen = 0

h = 0
q = 0

## -- This creates a sublist of just the products which I can then reference against the list of availability to produce the list of cheapest available products
while h < len(availability):
    k = 0
    for j in range(len(availability)):
        if availability[h][0] == availability[j][0]:
            k += 1
    cheapest.append([]) # This is so every product can get its own cell
    cheapest[q].append(availability[h][0])
    q += 1
    h += k



for i in range(len(cheapest)):
    price = 10
    for j in range(len(availability)):
        if cheapest[i][0] in availability[j]:
            if float(availability[j][2]) < price:
                price = float(availability[j][2])
                company = availability[j][1]
    cheapest[i].append(company)
    cheapest[i].append(price)

neededAndCheapest = [] # This will be the array which contains the items which are required by the store at their
# cheapest price point and the number of the company selling them, and how many are needed by the store.

for i in range(len(needed)):
    for j in range(len(cheapest)):
        if needed[i][0] in cheapest[j]:
            neededAndCheapest.append(cheapest[j])
            neededAndCheapest[i].append(needed[i][1])

print(neededAndCheapest)

#- Fifth step is to create the orders.txt file -#
