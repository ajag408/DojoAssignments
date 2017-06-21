from random import randint
from datetime import datetime

class Call(object):
    def __init__(self,name, reason):
        self.id = randint(0, 30)
        self.name = name
        self.number = str(randint(1111111, 9999999))
        self.time_of_call = str(datetime.now())
        self.reason = reason
    def display(self):
        attributes = {'id': self.id, 'name': self.name, 'phone number': self.number, 'call time': self.time_of_call, 'reason of call': self.reason}
        print attributes

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.qSize = 0
    def add(self, new_call):
        self.calls.append(new_call)
        self.qSize += 1
        return self
    def remove(self):
        self.calls.pop(0)
        self.qSize -= 1
        return self
    def findCall(self, number):
        for call in self.calls:
            if call.number == number:
                idx = self.calls.index(call)
        self.calls.pop(idx)
        self.qSize -= 1
        return self
    def testFindCall(self):
        return self.calls[2].number
    def display(self):
        for call in self.calls:
            print '**************'
            print call.name
            print call.number
            print '**************'
        print self.qSize

call1 = Call('akash', 'to dance')
call2 = Call('james', 'to eat')
call3 = Call('bertrand', 'to fuck')

att = CallCenter().add(call1).add(call2).add(call3)
att.display()
pertinent_number = att.testFindCall()
att.findCall(pertinent_number)
att.display()
