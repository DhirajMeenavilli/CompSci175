"""
Date: March/19/2020
Authour: Dhiraj Meenavilli
Title: Mini Spite and Malice
"""
import random
class Card():
    def __init__(self,face,val):
        assert (val >= -1 and val <= 9), "The value you entered was greater then 9 or less then -1 which is not allowed."
        self.__face = face
        self.__val = val

    def assign(self,val):
        assert (val >= 0 and val <= 9), "The value you entered was greater then 9 or less then 0 which is not allowed."
        if self.__face != "*":
            raise Exception("Only jokers can have their values changed.")
        self.__val = val

    def getValue(self):
        return self.__val

    def getFace(self):
        return self.__face

    def __str__(self):
        s = "["
        s += self.__face
        s += "]"
        return s

    def __repr__(self):
        rep = self.__str__() + "." + str(self.__val)
        return rep


class playStack():
    def __init__(self, cards=None):
        self.__cards = cards

    def peekValue(self):
        if self.__cards == None or self.__cards == []:
            raise Exception("The stack is empty so there are no cards to look at.")
        return self.__cards[0].getValue()

    def peekFace(self):
        if self.__cards == None or self.__cards == []:
            raise Exception("The stack is empty so there are no cards to look at.")
        return self.__cards[0].getFace()

    def playCard(self,card=None):
        stackEmpty = False
        if self.__cards == [] or self.__cards == None:
            self.__cards.append(Card("0",0))
            stackEmpty = True

        if stackEmpty != True:
            if card.getValue() == self.__cards[len(self.__cards)-1].getValue() + 1:
                self.__cards.append(card)

            else:
                raise Exception("The card placed was not directly greater then the last card on the stack therefore it cannot be added.")

            if self.__cards[len(self.__cards)-1].getValue() == 9:
                print(self.__str__())
                self.__cards = []

            else:
                print("[]")

    def __str__(self):
        cards = []

        for i in range(len(self.__cards)):
            cards.append(self.__cards[i].__str__())

        cards = "".join(cards)

        s = "|" + cards + "|"

        return s

class Hand():
    def __init__(self,hand):
        self.__hand = hand

    def sort(self):
        temp = []
        for i in range(len(self.__hand)):
            temp.append(self.__hand[i].getValue())

        temp.sort()

        for i in range(len(temp)):
            val = temp[i]
            for j in range(len(self.__hand)):
                if val == self.__hand[j].getValue():
                    swapTo = self.__hand[i]
                    self.__hand[i] = self.__hand[j]
                    self.__hand[j] = swapTo

    def pop(self):
        assert len(self.__hand) > 0, "There are no cards to play left in your hand"
        return self.__hand.pop()

    def specPop(self,i):
        assert (i >= 0 and i < len(self.__hand)), "There exists no card at that position"
        return self.__hand.pop(i)

    def index(self,v):
        assert (v >= -1 and v <= 9), "There exists no card like that to be searched for."
        h = -1
        for i in range(len(self.__hand)):
            if self.__hand[i].getValue() == v:
                h = i
                return h

        return h

    def checkZero(self):
        return self.index(0)

    def size(self):
        return len(self.__hand)

    def add(self,cardList):
        for i in range(len(cardList)):
            assert self.size() + 1 <=5, "There are too many cards being added for the hand to hold"
            self.__hand.append(cardList[i])

    def __str__(self):
        s = "["
        for i in range(self.size()):
            s += self.__hand[i].getFace()
            s += " "
        s += "]"
        return s

def shuffle(cards):
    result = []
    for i in range(len(cards)):
        result.append(cards.pop(random.randrange(0,len(cards))))

    return result
