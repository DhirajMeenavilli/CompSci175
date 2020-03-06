class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self, initData, initNext, initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious

        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setNext(self, newNext):
        self.next = newNext

    def setPrevious(self, newPrevious):
        self.previous = newPrevious


class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
            index = -1
        return index

    def add(self, item):
        newNode = DLinkedListNode(item,self.__head,None)
        self.__head = newNode
        if self.getSize() == 0:
            self.__tail = newNode
        self.__size += 1

    def remove(self, item):
        pos = self.index(item)
        self.pop(pos)

    def append(self, item):
        if self.getSize() == 0:
            self.add(item)
        else:
            new_node = DLinkedListNode(item,None,self.__tail)
            self.__tail.setNext(new_node)
            self.__tail = new_node
            self.__size += 1

    def insert(self, pos, item):
        if pos == (self.getSize()):
            self.append(item)
        elif pos == 0:
            self.add(item)
        else:
            new_node = DLinkedListNode(item,None,None)
            current = self.__head
            for i in range(pos):
                current = current.getNext()
            new_node.setNext(current)
            new_node.setPrevious(current.getPrevious())
            current.getPrevious().setNext(new_node)
            current.setPrevious(new_node)
            self.__size += 1

    def pop1(self):
        current = self.__tail
        item = current.getData()
        self.__size -= 1
        current = self.__tail.getPrevious()
        self.__tail = current
        if self.getSize() > 0:
            current.setNext(None)
        if self.getSize() == 0:
            self.__head = None
        return item

    def pop(self, pos=None):
        if pos == None or pos == (self.getSize() - 1):
            item = self.pop1()
            return item

        else:
            i = 0
            current = self.__head
            while i != pos:
                current = current.getNext()
                i += 1
            current.getNext().setPrevious(current.getPrevious())
            current.getPrevious().setNext(current.getNext())
            self.__size -= 1

    def searchLarger(self, item):
        val = None
        current = self.__head
        i = 0
        while val == None or val <= item and i < self.getSize():
            val = current.getData()
            current = current.getNext()
            i += 1
        if i > self.getSize():
            val = -1
        pos = self.index(val)
        return pos

    def getSize(self):
        return self.__size

    def getItem(self, pos):
        if pos >= 0:
            i = 0
            current = self.__head
            while i != pos:
                current = current.getNext()
                i += 1
            item = current.getData()
        if pos < 0:
            i = -1
            current = self.__tail
            while i > pos:
                current = current.getPrevious()
                i -= 1
            item = current.getData()

        return item

    def __str__(self):
        try:
            current = self.__head
            s = ""
            i = 0
            if i == 0:
                s = s + str(current.getData())
                current = current.getNext()
                i += 1
            while current != None:
                s = s +" "+ str(current.getData())
                current = current.getNext()
            return s

        except:
            s = " "
            return s
def test():
    linked_list = DLinkedList()

    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    linked_list.add("World")
    linked_list.add("Hello")

    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(0) == "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    int_list2 = DLinkedList()

    for i in range(0, 10):
        int_list2.add(i)
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)

    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"


    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"

    for i in range(21, 23):
        int_list2.insert(0, i)

    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"

    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"

    int_list = DLinkedList()

    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    for i in range(0, 1000):
        int_list.append(i)
    correctOrder = True

    is_pass = (int_list.getSize() == 1000)
    assert is_pass == True, "fail the test"

    for i in range(0, 200):
        if int_list.pop() != 999 - i:
            correctOrder = False

    is_pass = correctOrder
    assert is_pass == True, "fail the test"

    is_pass = (int_list.searchLarger(200) == 201)
    assert is_pass == True, "fail the test"


    int_list.insert(7, 801)

    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"

    is_pass = (int_list.getItem(-1) == 799)
    assert is_pass == True, "fail the test"

    is_pass = (int_list.getItem(-4) == 796)
    assert is_pass == True, "fail the test"

    if is_pass == True:
        print("=========== Congratulations! Your have finished exercise 2! ============")

if __name__ == '__main__':
    test()
