class SLNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class SList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def PrintAllVals(self):
        runner = self.head
        while runner!=None:
            print runner.value
            runner = runner.next
    def AddBack(self, val):
        if self.tail != None:
            self.tail.next = SLNode(val)
            self.tail = self.tail.next
        else:
            runner = self.head
            while runner.next != None:
                runner = runner.next
            runner.next = SLNode(val)
            self.tail = runner.next
    def AddFront(self, val):
        newHead = SLNode(val)
        newHead.next = self.head
        self.head = newHead
    def InsertBefore(self, nextVal, val):
        if self.head.value == nextVal:
            newNode = SLNode(val)
            newNode.next = self.head
            self.head = newNode
        else:
            runner = self.head
            while runner.next != None and runner.next.value != nextVal:
                runner = runner.next
            if runner.next == None:
                print 'no node of the value nextVal exists in this list!'
            else:
                newNode = SLNode(val)
                newNode.next = runner.next
                runner.next = newNode
    def InsertAfter(self, preval, val):
        runner = self.head
        while runner.next != None and runner.next.value != preval:
            runner = runner.next
        if runner.next == None:
            print 'no node of the value preval exists in this list!'
        else:
            newNode = SLNode(val)
            newNode.next = runner.next.next
            runner.next.next = newNode
    def RemoveNode(self, val):
        if self.head.value == val:
            if self.head.next == None:
                self.head = None
            else:
                self.head = self.head.next
        else:
            runner = self.head
            while runner.next != None and runner.next.value != val:
                runner = runner.next
            if runner.next == None:
                print 'no such node to remove'
            else:
                fucked = runner.next
                runner.next = fucked.next
    def ReverseList(self):
        storeArr = [self.head]
        runner = self.head
        while runner.next != None:
            storeArr.append(runner.next)
            runner = runner.next
        for node in storeArr:
            node.next = None
        self.head = storeArr[len(storeArr)-1]
        runner = storeArr[len(storeArr)-2]
        self.head.next = runner
        for idxInc in range(3, len(storeArr)+1):
            runner.next = storeArr[len(storeArr) - idxInc]
            runner = runner.next


list = SList()
list.head = SLNode('Jameson')
list.head.next = SLNode('Jon')
list.head.next.next = SLNode('Steve')



list.PrintAllVals()
