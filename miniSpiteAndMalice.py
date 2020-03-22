"""
Date: March/21/2020
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
        return self.__str__()

    def __str__(self):
        s = "["
        s += self.__face
        s += "]"
        return s

    def __repr__(self):
        rep = self.__str__() + "." + str(self.__val)
        return rep


class playStack():
    def __init__(self, cards=[]):
        self.__cards = cards

    def peekValue(self):
        if self.__cards == []:
            raise Exception("The stack is empty so there are no cards to look at.")
        return self.__cards[len(self.__cards)-1].getValue()

    def peekFace(self):
        if self.__cards == []:
            raise Exception("The stack is empty so there are no cards to look at.")
        return self.__cards[len(self.__cards)-1].getFace()

    def playCard(self,card=None):
        stackEmpty = True

        if self.__cards != []:
            stackEmpty = False

        if stackEmpty:
            assert card.getValue() == 0, "This stack is empty only zero is allowed to go here."

        if card.getValue() == 0:
            if self.__cards == []:
                self.__cards.append(Card("0",0))

        if stackEmpty != True:
            if card.getValue() == self.__cards[len(self.__cards)-1].getValue() + 1:
                self.__cards.append(card)

            else:
                raise Exception("The card placed was not directly greater then the last card on the stack therefore it cannot be added.")

            if self.__cards[len(self.__cards)-1].getValue() == 9:
                print(self.__str__())
                self.__cards = []

            else:
                return []

    def add(self,card):
        self.__cards.append(card)

    def pop(self):
        return self.__cards.pop()

    def size(self):
        return len(self.__cards)

    def __str__(self):
        cards = []

        for i in range(len(self.__cards)):
            cards.append(self.__cards[i].__str__())

        cards = "".join(cards)

        s = "|" + cards + "|"

        return s

class Hand():
    def __init__(self,hand=[]):
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

############################################### --- Code Starts Here --- ###############################################

cardShoe = []

cards1 = []
cards2 = []

pile1 = []
pile2 = []

for i in range(10):
    for j in range(10):
        cardShoe.append(Card(str(j),j))

for i in range(20):
    cardShoe.append(Card('*',-1))

cardShoe = shuffle(cardShoe) # Deck gets shuffled

for i in range(5): # This is simmilar to how cards are dealt in alternating ways
    cards1.append(cardShoe.pop())
    cards2.append(cardShoe.pop())

for i in range(15):
    pile1.append(cardShoe.pop())
    pile2.append(cardShoe.pop())

player1 = Hand(cards1)
goalPile1 = playStack(pile1)
player2 = Hand(cards2)
goalPile2 = playStack(pile2)

player1FirstDiscardPile = playStack([])
player1SecondDiscardPile = playStack([])
player1ThirdDiscardPile = playStack([])
player1FourthDiscardPile = playStack([])

player1DiscardPiles = [player1FirstDiscardPile,player1SecondDiscardPile,player1ThirdDiscardPile,player1FourthDiscardPile]

player2FirstDiscardPile = playStack([])
player2SecondDiscardPile = playStack([])
player2ThirdDiscardPile = playStack([])
player2FourthDiscardPile = playStack([])

player2DiscardPiles = [player2FirstDiscardPile,player2SecondDiscardPile,player2ThirdDiscardPile,player2FourthDiscardPile]

gamePile1 = playStack([])
gamePile2 = playStack([])
gamePile3 = playStack([])
gamePile4 = playStack([])

gamePiles = [gamePile1,gamePile2,gamePile3,gamePile4]

game = True

while game:
    player1Turn = False
    player2Turn = False
    set1 = [] # Sets are cleared so they can be added to later
    set2 = []
    turns = 0
    player1.sort()  # Players hands are sorted
    player2.sort()


    if goalPile2.peekValue() > goalPile1.peekValue():
        player2Turn = True

    else: # Because in any situation ther then player 2 having a higher value on top of the stack player1 goes first
        player1Turn = True

    print(goalPile1.peekFace())



    while player1Turn:
        if turns == 2: # If both players have had a turn then the round is done
            player1Turn = False
            player2Turn = False

        print("Player 1 Hand:",player1,"\nPlayer 1 Discard 1:",player1FirstDiscardPile,"\nPlayer 1 Discard 2:",player1SecondDiscardPile,
              "\nPlayer 1 Discard 3:",player1ThirdDiscardPile,"\nPlayer 1 Discard 4:",player1FourthDiscardPile,
              "\nPlayer 1 Goal Pile", goalPile1.peekFace(),goalPile1.size(),"cards left","\n\nPlay Stack 1:", gamePile1,"\nPlay Stack 2:",
              gamePile2,"\nPlay Stack 3:", gamePile3,"\nPlay Stack 4:", gamePile4,"\n\nPlayer 2 Hand:", player2, "\nPlayer 2 Discard 1:",
              player2FirstDiscardPile,"\nPlayer 2 Discard 2:",player2SecondDiscardPile, "\nPlayer 2 Discard 3:",player2ThirdDiscardPile,
              "\nPlayer 2 Discard 4:",player2FourthDiscardPile,"\nPlayer 2 Goal Pile",goalPile2.peekFace(), goalPile2.size(),"cards left")

        placing = True # this variable exists to create a state in which the user can keep playing until they have n legal moves left

        while placing:
            play = input("\nPlayer 1 choose action p (play) or x (discard/end turn) ").lower()

            handRemoved = False
            discardRemoved = False
            pileRemoved = False # Each of these when removed from need to be added back to separately therefore I created a simple way to discern which action needs to be taken

            for i in range(len(gamePiles)):
                if gamePiles[i].size() == 0 and player1.checkZero() > -1: # this is just checking if the user has a zero and if any of the game piles are empty
                    card = player1.specPop(player1.checkZero()) # if both are true then the player is forced to play their card
                    gamePiles[i].playCard(card) # The game pile which was first empty will recieve this 0 and be opened.
            try:
                if play[0] == "p":
                    playFrom = list(input("\nPlay from where: hi = hand at position i (1..5); g = goal; dj = discard pile j (1..4)?"))

                    assert playFrom[0] == "h" or playFrom[0] == "g" or playFrom[0] == "d", "You have picked an invalid place to play from" # So that if the user hits a different key there's no issues

                    if playFrom[0] == "h":
                        card = player1.specPop(int(playFrom[1])-1)
                        handRemoved = True

                    elif playFrom[0] == "g":
                        card = goalPile1.pop()
                        pileRemoved = True

                    elif playFrom[0] == "d":
                        card = player1DiscardPiles[int(playFrom[1])-1].pop()
                        discardRemoved = True

                    playTo = input("\nWhich Play Stack are you targeting (1..4)?")

                    assert int(playTo) > 0 and int(playTo) < 5, "You have picked an invalid pile to play to."

                    if card.getFace() == "*":
                        if gamePiles[int(playTo) - 1].size() == 0:
                            card.assign(0)
                        else:
                            card.assign(gamePiles[int(playTo) - 1].peekValue() + 1)

                    gamePiles[int(playTo)-1].playCard(card)

                if play[0] == "x":
                    playTo = input("\nWhich Discard Pile are you targeting (1..4)?")
                    card = player1.pop()
                    handRemoved = True # In case a 0 is in fact removed the assertion will catch and the card will be added back.

                    assert card.getValue() != 0, "You are not allowed to discard a card with value 0."

                    player1DiscardPiles[int(playTo) - 1].add(card)

                    placing = False

            except AssertionError as args:
                if handRemoved:
                    player1.add([card])
                    player1.sort()

                if pileRemoved:
                    goalPile1.add(card)

                if discardRemoved:
                    player1DiscardPiles[int(playFrom[1]) - 1].add(card)

                print(args) # This allows me to tell the user what the issue was if I was able to catch it.

            except IndexError as args:
                print(args)

            except Exception as args:
                print(args)


        turns += 1

        player1Turn = False
        player2Turn = True # This simply alternates the turns

    while player2Turn:
        if turns == 2:  # If both players have had a turn then the round is done
            player1Turn = False
            player2Turn = False

        print("Player 1 Hand:", player1, "\nPlayer 1 Discard 1:", player1FirstDiscardPile, "\nPlayer 1 Discard 2:",
              player1SecondDiscardPile,
              "\nPlayer 1 Discard 3:", player1ThirdDiscardPile, "\nPlayer 1 Discard 4:", player1FourthDiscardPile,
              "\nPlayer 1 Goal Pile", goalPile1.peekFace(), goalPile1.size(), "cards left", "\n\nPlay Stack 1:",
              gamePile1, "\nPlay Stack 2:",
              gamePile2, "\nPlay Stack 3:", gamePile3, "\nPlay Stack 4:", gamePile4, "\n\nPlayer 2 Hand:", player2,
              "\nPlayer 2 Discard 1:",
              player2FirstDiscardPile, "\nPlayer 2 Discard 2:", player2SecondDiscardPile, "\nPlayer 2 Discard 3:",
              player2ThirdDiscardPile,
              "\nPlayer 2 Discard 4:", player2FourthDiscardPile, "\nPlayer 2 Goal Pile", goalPile2.peekFace(),
              goalPile2.size(), "cards left")

        placing = True 

        while placing:
            play = input("\nPlayer 2 choose action p (play) or x (discard/end turn) ").lower()

            handRemoved = False
            discardRemoved = False
            pileRemoved = False  

            for i in range(len(gamePiles)):
                if gamePiles[i].size() == 0 and player2.checkZero() > -1:  
                    card = player2.specPop(player2.checkZero()) 
                    gamePiles[i].playCard(card) 
            try:
                if play[0] == "p":
                    playFrom = list(input("\nPlay from where: hi = hand at position i (1..5); g = goal; dj = discard pile j (1..4)?"))

                    assert playFrom[0] == "h" or playFrom[0] == "g" or playFrom[0] == "d", "You have picked an invalid place to play from"  

                    if playFrom[0] == "h":
                        card = player2.specPop(int(playFrom[1]) - 1)
                        handRemoved = True

                    elif playFrom[0] == "g":
                        card = goalPile2.pop()
                        pileRemoved = True

                    elif playFrom[0] == "d":
                        card = player2DiscardPiles[int(playFrom[1]) - 1].pop()
                        discardRemoved = True

                    playTo = input("\nWhich Play Stack are you targeting (1..4)?")

                    assert int(playTo) > 0 and int(playTo) < 5, "You have picked an invalid pile to play to."

                    if card.getFace() == "*":
                        if gamePiles[int(playTo) - 1].size() == 0:
                            card.assign(0)
                        else:
                            card.assign(gamePiles[int(playTo) - 1].peekValue() + 1)

                    gamePiles[int(playTo) - 1].playCard(card)

                if play[0] == "x":
                    playTo = input("\nWhich Discard Pile are you targeting (1..4)?")
                    card = player2.pop()
                    handRemoved = True  # In case a 0 is in fact removed the assertion will catch and the card will be added back.

                    assert card.getValue() != 0, "You are not allowed to discard a card with value 0."

                    player2DiscardPiles[int(playTo) - 1].add(card)

                    placing = False

            except AssertionError as args:
                if handRemoved:
                    player2.add([card])
                    player2.sort()

                if pileRemoved:
                    goalPile2.add(card)

                if discardRemoved:
                    player2DiscardPiles[int(playFrom[1]) - 1].add(card)

                print(args)  # This allows me to tell the user what the issue was if I was able to catch it.

            except IndexError as args:
                print(args)

            except Exception as args:
                print(args)
                
        turns += 1

        player2Turn = False
        player1Turn = True

    for i in range(5 - player1.size()): # This deals cards to the hand so that the user will always have 5 in hand
       set1.append(cardShoe.pop())

    for i in range(5 - player2.size()):
        set2.append(cardShoe.pop())

    player1.add(set1)
    player2.add(set2)

    if goalPile1.size() == 0 or goalPile2.size() ==0:# If the goal state of a player having no more cards in their goal pile is met the game is finished
        if goalPile1.size() == 0:
            print("Congratulations Player 1 you have won")
        else:
            print("Congratulations Player 2 you have won")
        game = False
