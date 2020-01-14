"""
Title: BlueBell GreenHouses
Date: 2020/01/13
Authour: Dhiraj Meenavilli
"""
totalBulbs = 0
totalCost = 0
bulbsAndPrices = {'Daffodil': 0.35,
              'Tulip': 0.41,
              'Crocus': 0.25,
              'Hyacinth': 0.75,
              'Bluebell': 0.50}

marysOrder = {'Daffodil': 50,
              'Tulip': 100,
              'Hyacinth': 30}

marysOrderList = ['Daffodil', 'Tulip', 'Hyacinth']

print("You have purchased the following bulbs: ")
for i in range(len(marysOrderList)):
    print(marysOrderList[i] ,'*',marysOrder[marysOrderList[i]],"= $",str(bulbsAndPrices[marysOrderList[i]]*marysOrder[marysOrderList[i]])+"0")
    totalBulbs = totalBulbs + marysOrder[marysOrderList[i]]
    totalCost = totalCost + bulbsAndPrices[marysOrderList[i]]*marysOrder[marysOrderList[i]]
print("")
print("Thank you for purchasing",totalBulbs,"bulbs from Bluebell Greenhouses.\nYour total comes to $" + str(totalCost)+"0.")

