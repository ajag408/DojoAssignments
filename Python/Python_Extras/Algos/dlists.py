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
        runner = self.head
        while runner.next != None and runner.next != val:
            runner = runner.next
        if runner.next = None:
            print "no node of that value"
        else:
            
