# ----------------------------------------------------
# Stack implementation #2
# (Top of stack corresponds to back of list)
#
# Author: CMPUT 175 team
# Updated by:
# ----------------------------------------------------

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        errorMessage = 'This array is empty nothing can be popped'
        try:
            return self.items.pop()
        except IndexError:
            raise Exception(errorMessage)

    def peek(self):
        errorMessage = 'This array is empty'
        try:
            peekPoint = self.items[len(self.items)-1]
            return peekPoint
        except IndexError:
            raise Exception(errorMessage)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)

    def __str__(self):
        stackAsString = ''
        for item in self.items:
            stackAsString += item + ' '
        return stackAsString

    def clear(self):
        if self.size() > 0:
            self.items = []

