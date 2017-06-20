class MathDojo(object):
    def __init__(self):
        self.total = 0
    def add(self, num, *more):
        self.total += num
        for number in more:
            self.total += number
        return self
    def subtract(self, num, *more):
        sub_total = num
        for number in more:
            sub_total += number
        self.total -= sub_total
        return self
    def result(self):
        return self.total


md = MathDojo().add(2).add(2,5).subtract(3,2).result()
print md
