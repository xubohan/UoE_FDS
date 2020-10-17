import abc


class Queue(abc.ABC):
    @abc.abstractmethod
    def isEmpty(self):
        pass

    @abc.abstractmethod
    def push(self, item):
        pass

    @abc.abstractmethod
    def pop(self):
        pass


class LL_Queue(Queue):
    '''
q.head[0]
Out[10]: (3, [(4, [()])])
q.push(5)
Out[11]: [()]
q.head
Out[12]: [(3, [(4, [(5, [()])])])]
q.tail[0]
Out[13]: ()
q.head
Out[14]: [(3, [(4, [(5, [()])])])]
q.tail
Out[15]: [()]
q.head
Out[16]: [(3, [(4, [(5, [()])])])]
q.pop()
Out[17]: 3
q.head
Out[18]: [(4, [(5, [()])])]
    '''

    def __init__(self):
        self.tail = [()]
        self.head = self.tail

    def isEmpty(self):
        return self.head[0] == ()

    def push(self, item):
        self.tail[0] = (item, [()])
        self.tail = self.tail[0][1]

    def pop(self):
        if self.isEmpty():
            raise IndexError
        else:
            y = self.head[0][0]
            self.head = self.head[0][1]
            return y


class CircBuffer_Queue(Queue):

    def __init__(self):
        self.tail = [()]
        self.head = self.tail
        self.counter = 0

    def isEmpty(self):
        return self.head[0] == ()

    def push(self, item):
        self.tail[0] = (item, [()])
        self.tail = self.tail[0][1]
        self.counter += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError
        else:
            y = self.head[0][0]
            self.head = self.head[0][1]
            self.counter -= 1
            return y

    def deep(self):
        return self.counter

    def setHead(self, num):
        if num == 0:
            pass
        else:
            for x in range(num):
                self.tail = self.tail[0][1]
                self.head = self.tail

    def bufferCirc(self, item, headInx, tailInx):
        temp = item.split(' ')
        temp_size = len(temp)
        if headInx > tailInx:
            headInx = headInx - temp_size

        for x in range(headInx, tailInx):
            self.push(temp[x])
        if headInx <= temp_size - 1 and tailInx <= temp_size - 1:
            if headInx == tailInx:
                print('the queue is empty')

            elif tailInx == 0:
                self.setHead(headInx)
            else:
                self.setHead(headInx)
                self.pop()
                self.push(temp[tailInx])
        else:
            raise Exception
'''   
            elif headInx < tailInx:
                for i in range(headInx, tailInx):
                    self.push(self.pop())
                self.pop()
                self.push(item[tailInx])
                print(self.head)
'''
if __name__ == '__main__':
    pass
