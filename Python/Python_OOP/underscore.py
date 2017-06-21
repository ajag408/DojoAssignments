class Underscore(object):
    def map(self, arr, callback):
        new_arr = []
        for val in arr:
            new_val = callback(val)
            new_arr.append(new_val)
        return new_arr
    def reduce(self, arr, callback, *memo):
        if memo:
            #start w memo (set it to first val)
            total = memo[0]
            # next_val = arr[0]
            pointer = 0
        else:
            #start w the first member in the array (set it to first val)
            total = arr[0]
            pointer = 1
        #pass first val(memo or first number) into callback w next val and save total
        while pointer < len(arr):
            total = callback(total, arr[pointer])
            pointer += 1
        return total
    # def find(self):
    #     # your code here
    def filter(self, arr, callback):
        new_arr = []
        for val in arr:
            if callback(val) is True:
                new_arr.append(val)
            else:
                continue
        return new_arr
    # def reject(self):
        # your code
# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
total = _.reduce([1], lambda x, y: x + y, 1)
print total
# should return [2, 4, 6] after you finish implementing the code above
