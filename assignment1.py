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
costs = []

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

for i in range(len(neededAndCheapest)):
    costs.append([])
    costs[i].append(neededAndCheapest[i][1])

for i in range(len((neededAndCheapest))):
    neededAndCheapest[i][1] = "("+neededAndCheapest[i][1][:3]+")"+" "+neededAndCheapest[i][1][3:6]+" "+neededAndCheapest[i][1][6:10]


#- Fifth step is to create the orders.txt file -#
productName = {}
supplierName = {}
products = breakText(products,";")
suppliers = breakText(suppliers,";")
totalCost = 0

try:
    orders = open("orders.txt","x")
    orders.close()
    orders = open("orders.txt","w")
except:
    orders = open("orders.txt","w")


for i in range(len(products)):
    if len(products[i][1]) > 16:
        products[i][1] = products[i][1][:16]
    productName[products[i][0]] = products[i][1]

for i in range(len(suppliers)):
    supplierName[suppliers[i][0]] = suppliers[i][1]


orders.writelines(['+--------------+------------------+--------+----------------+----------+','\n'+'|', ' Product Code ', "|"," Product Name    ",' |'+"Quantity"+"| ", " Supplier     ", " | ", " Cost    ","|  "])
orders.writelines(["\n","+--------------+------------------+--------+----------------+----------+"])
for i in range(len(neededAndCheapest)):
    #if len(productName[neededAndCheapest[i][0]]) > 17:
    cost = str(round((neededAndCheapest[i][2] * neededAndCheapest[i][3]), 2))
    costs[i].insert(0,float(cost))
    costs[i].append(neededAndCheapest[i][1])
    totalCost += (neededAndCheapest[i][2] * neededAndCheapest[i][3])
    if len(cost) < 5:
        cost = cost + "0"

    orders.writelines(["\n","|  ", neededAndCheapest[i][0],"   |  ", productName[neededAndCheapest[i][0]],"|     ",str(neededAndCheapest[i][3])," | ", neededAndCheapest[i][1]," | ","$ ",cost.rjust(6), " |"])

orders.writelines(["\n","+--------------+------------------+--------+----------------+----------+"])
orders.writelines(["\n","| ","Total Cost","   |         ","      $   ",str(round(totalCost,2))+"  |"])
orders.writelines(["\n","+--------------+---------------------------+"])

highestCost = []
highestCostSuppliers = []
costs.sort(reverse=True)

for i in range(1):
    for j in range(len(costs)):
        if costs[0] == costs[j]:
            highestCost.append(costs[j])

for i in range(len(highestCost)):
    for j in range(len(suppliers)):
        if highestCost[i][1] in suppliers[j]:
            highestCostSuppliers.append([])
            highestCostSuppliers[i].append((suppliers[j][1]))
            highestCostSuppliers[i].append(highestCost[i][2])
            highestCostSuppliers[i].append(highestCost[i][0])

for i in range(len(highestCostSuppliers)):
    orders.writelines(["\n",'Highest cost: ', highestCostSuppliers[i][0]," ", highestCostSuppliers[i][1]," ["+"$"+str(highestCostSuppliers[i][2])+"]"])

orders.close()
