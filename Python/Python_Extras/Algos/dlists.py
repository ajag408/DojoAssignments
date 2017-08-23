class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def AddtoEnd(self, val):
        newNode = Node(val)
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
    def Delete(self, val):
        if self.head.value == val:
            headCopy = self.head
            self.head = self.head.next
            self.head.prev = None
        else:
            runner = self.head
            while runner.next != None and runner.next.value != val:
                runner = runner.next
            if runner.next == None:
                print "no node of that value"
            else:
                runnerCopy = runner
                runner = runner.next
                if runner.next != None:
                    runnerCopy.next = runner.next
                    runner.prev = None
                    runnerCopy2 = runner
                    runner = runner.next
                    runnerCopy2.next = None
                    runner.prev = runnerCopy
                else:
                    runnerCopy.next = None
                    self.tail = runnerCopy
    def Print(self):
        runner = self.head
        while runner!=None:
            print runner.value
            runner = runner.next
    def insertBefore(self,nextVal, val):
        if self.head.value == nextVal:
            newNode = Node(val)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            print newNode.next
            print self.head.next
        else:
            runner = self.head
            while runner.next.value != nextVal:
                runner = runner.next
            newNode = Node(val)
            newNode.next = runner.next
            runner.next.prev = newNode
            runner.next = newNode
            newNode.prev = runner
    def insertAfter(self, preVal, val):
        runner = self.head
        while runner.value != preVal:
            runner = runner.next
        newNode = Node(val)
        if runner == self.tail:
            runner.next = newNode
            newNode.prev = runner
        else:
            newNode.next = runner.next
            runner.next.prev = newNode
            runner.next = newNode
            newNode.prev = runner


list = DList()
node1 = Node('Chucky')
node2 = Node('Ste')
node3 = Node('James')

list.head = node1
list.tail = node3
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

list.insertAfter('Chucky', 'Jerm')
list.Print()
