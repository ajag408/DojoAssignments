import unittest
def min(l):
    # Should find and return minimum value in a given list
    if type(l) is not list or len(l) == 0:
        return None 
    else:
        min = l[0]
        for val in l:
            if val < min:
                min = val
        return min
def sum_list(l):
    # Should return total value of all list items
    total = 0
    for val in l:
        total += val
    return total
def less_than(a):
    # Should return a bool of whether given value is less than 100
    return a < 100
### For this exercise, work within this class. This is something you will come up with on your own soon ###
class MainTest(unittest.TestCase):
    # tests go here!    
    def test_min(self):
        self.assertEqual(min([3,4,2,1,5]), 1)
        self.assertEqual(min([1,2,3,4,5]), 1)
        self.assertIsNone(min(1))
    def test_sum(self):
        self.assertEqual(sum_list([1,2,3]), 6)
        self.assertEqual(sum_list([2]), 2)
        self.assertEqual(sum_list([-4, 3, -3]), -4)
    def test_less(self):
        self.assertTrue(less_than(40))
        self.assertFalse(less_than(140))
        self.assertFalse(less_than(100))