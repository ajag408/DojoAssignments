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
    def __repr__(self):
        return "<Call object, id {}, name {}, number {}, time of call {}, reason {}>".format(self.id, self.name, self.number, self.time_of_call, self.reason)

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
    def sortAsc(self):
        self.calls = sorted(self.calls)
        return self
    def display(self):
        for call in self.calls:
            print '**************'
            print call.name
            print call.number
            print '**************'
        print self.qSize
    def __repr__(self):
        return "<CallCenter object, calls {}, qsize {}>".format(self.calls, self.qSize)

if __name__ == '__main__':
    call1 = Call('akash', 'to dance')
    call1.display()
    call2 = Call('james', 'to eat')
    call2.display()
    call3 = Call('bertrand', 'to chuck')
    call3.display()

    att = CallCenter().add(call3).add(call2).add(call1)
    att.display()
    att.sortAsc()
    att.display()
