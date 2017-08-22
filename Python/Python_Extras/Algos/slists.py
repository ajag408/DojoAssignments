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
        runner = self.head
        while runner.next != None and runner.next.value != nextVal:
            runner = runner.next
        if runner.next == None:
            print 'no node of the value nextVal exists in this list!'
        else:
            newNode = SLNode(val)
            newNode.next = runner.next
            runner.next = newNode

list = SList()
list.head = SLNode('Jameson')
list.head.next = SLNode('Jon')
list.head.next.next = SLNode('Steve')


list.InsertBefore('Jon', 'Tyrese')
list.PrintAllVals()
