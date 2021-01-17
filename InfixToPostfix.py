class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def solution(S):
    result = ""
    opStack = ArrayStack()
    
    for c in S:
        if c in prec:
            
            if c == '(' or opStack.isEmpty():
                opStack.push(c)
            
            else:
                while prec[opStack.peek()] >= prec[c]:
                    result += opStack.pop()
                    if opStack.isEmpty():break
                opStack.push(c)
                    
        elif c == ')':
            while not opStack.peek()== '(':
                result += opStack.pop()
            opStack.pop()
            
        else:
            result += c
    
    while not opStack.isEmpty():
        result += opStack.pop()
    
    return result
