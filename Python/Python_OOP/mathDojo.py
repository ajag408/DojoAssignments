class MathDojo(object):
    def __init__(self):
        self.total = 0
    def add(num, *more):
        self.total += num
        for number in more:
            self.total += number
        print self.total
        return self
    def subtract():
        return self


MathDojo().add(2)
