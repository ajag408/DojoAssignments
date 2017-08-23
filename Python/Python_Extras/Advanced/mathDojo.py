class MathDojo(object):
    def __init__(self):
        self.total = 0
    def add(self, *args):
        for arg in args:
            if type(arg) is list or type(arg) is tuple:
                for num in arg:
                    self.total += num
            else:
                self.total += arg
        return self
    def subtract(self, *args):
        for arg in args:
            if type(arg) is list or type(arg) is tuple:
                sub_total = 0
                for num in arg:
                    sub_total += num
                self.total -= sub_total
            else:
                self.total -= arg
        return self
    def result(self):
        return self.total
    def __repr__(self):
        return "<MathDojo object, current total {}>".format(self.total)



if __name__ == '__main__':
    md = MathDojo().add([1],3,4).add((3,5,7,8),[2,4.3,1.25]).subtract(2, (2,3), [1.1, 2.3]).result()
    print md
