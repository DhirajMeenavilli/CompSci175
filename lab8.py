"""
Author:Dhiraj Meenavilli
Date: March/16/2020
Title: Lab 8
"""
def mylen(list):
    i = 0
    if list != []:
        i += 1
        list.pop()
        i += mylen(list)

    if list == []:
        return i

def intDivision(n,m):
    assert n > 0, ("The Value you input for your dividend must be positive")
    assert m > 0, ("The Value you input for your divisor must be positive")
    i = 0
    if n > m:
        i += 1
        n = n-m
        i += intDivision(n,m)

    return i

def sumDigits(num):
    if type(num) != type([]):
        assert num > 0, "This number needs to be a positive number"
        num = str(num)
        num = list(num)

    i = 0

    if num != []:
        i += int(num.pop())
        i += sumDigits(num)

    if num == []:
        return i

def reverseDisplay(num,new):
    if type(num) != type([]):
        assert num > 0, "This number needs to be a positive number"
        num = str(num)
        num = list(num)

    if num != []:
        new.append(num.pop(len(num)-1))
        reverseDisplay(num,new)

    if num == []:
        new = "".join(new)

    return new

def binary_search2(key,lis,low,high):
    guess = (low+high)//2

    inList = False
    for i in range(len(lis)):
        if key == lis[i]:
            inList = True

    if inList:
        if lis[guess] < key:
            guess = binary_search2(key,lis,guess+1,high)

        if lis[guess] > key:
            guess = binary_search2(key,lis,low,guess - 1)

        if lis[guess] == key:
            return guess

    if not inList:
        return "Item not in list"

def main():
    # Excercise 1

    alist=[43,76,97,86,"bob"]
    print(mylen(alist))

    # Excercise 2

    n = int(input('Enter an integer dividend: '))
    m = int(input('Enter an integer divisor: '))
    print('Integer division', n, '//', m, '=',intDivision(n, m))


    # Excercise 3

    number = int(input('Enter a number: '))
    print(sumDigits(number))

    #Excercise 4

    new = []
    number = int(input('Enter a number: '))
    print(reverseDisplay(number, new))

    # Excercise 5

    some_list = [-8, -2, 1, 3, 5, 7, 9]

    result1 = binary_search2(9, some_list, 0, len(some_list) - 1)
    print(result1)

    result2 = binary_search2(-8, some_list, 0, len(some_list) - 1)
    print(result2)

    result3 = binary_search2(4, some_list, 0, len(some_list) - 1)
    print(result3)

main()
