class Queue:

    ## FIFO

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class Deque:
    # Deque not FIFO, FILO
    # Left side is rear
    # Right side is front

    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def show(self):
        return [i for i in self.items]

class singleLinkedList:
    # Left to Right
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()

        else:
            previous.setNext(current.getNext())

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found


    def isEmpty(self):
        return self.head is None

    def size(self):
        counter = 0
        current = self.head

        while current != None:
            counter += 1
            current = current.getNext()

        return counter


    def append(self, item):
        # add in the last
        temp = Node(item)
        temp.setNext(None)
        current = self.head

        while current != None:
            current = current.getNext()
        current.setNext(temp)

    def index(self, item):
        counter = 0
        current = self.head
        while current != None:
            if current.getData() == item:
                return counter
            else:
                current = current.getNext()
                counter += 1
        return -1

    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        else:
            current = self.head
            for x in range(pos):
                current = current.getNext
            temp = Node(item)
            temp.setNext(current.getNext)
            current.setNext(temp)

    def pop(self):
        counter = 0
        current = self.head



    def pop(self, pos):





class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.last = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext



def hotPotato(nameList, num):

    a = Queue()
    for name in nameList:
        a.enqueue(name)

    while a.size() > 1:
        for i in range(num):
            a.enqueue(a.dequeue())
        a.dequeue()
    return a.dequeue()

