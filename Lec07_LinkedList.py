class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def popAt(self, pos):
        if pos<1 or pos>self.nodeCount:
            raise IndexError
        
        if pos == 1:
            curr = self.head
            self.head = curr.next
            if self.nodeCount == 1:
                self.tail = None  #self.head = None : 굳이 없어도 됨
            
        else:
            prev = self.getAt(pos-1) #self.getAt을 지양하기 위해 prev를 구하고
            curr = prev.next #curr를 구함
            prev.next = curr.next
            if pos == self.nodeCount: #마지막 노드를 pop할때는 뒤로 갈 수 없어서 popAt에서는 반드시                               
                self.tail = prev      #prev = getAt(pos-1)을 쓸 수밖에 없음
        
        self.nodeCount -= 1
        return curr.data


    


def solution(x):
    return 0
