class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self[len(self.items)-1]


def infixToPostfix(aaa):
    level = {'*': 3,
            '/': 3,
            '+': 2,
            '-': 2,
            ')': 1}

    operands = Stack()
    member = []
    b = aaa.split();

    for x in b:
        if x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or x in "0123456789":
            member.append(x)
        elif x == '(':
            operands.push(x)
        elif x == ')':
            topToken = operands.pop()
            while topToken != '(':
                member.append(topToken)
                topToken = operands.pop()
        else:
            while not operands.isEmpty() and (level[operands.peek()] >= level[x]):
                member.append(operands.pop())
            operands.push(x)

    while not operands.isEmpty():
        member.append(operands.pop())
    return " ".join(member)

# translate into postfix
if __name__ == '__main__':
    print(infixToPostfix('( A + B )'))





