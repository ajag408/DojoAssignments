import unittest
from underscore import Underscore
class UnderscoreTest(unittest.TestCase):
    def setUp(self):
        # create an instance of the Underscore module we created
        self._ = Underscore()
        # initialize a list to run our tests on
        self.test_list = [1,2,3,4,5]
    def testMap(self):
        mappedArr = self._.map(self.test_list, lambda x: x*2 )
        return self.assertEqual([2,4,6,8,10], mappedArr)
    def testReduce(self):
        reduceArr = self._.reduce(self.test_list, lambda x, y: x+y, (5))
        return self.assertEqual(20, reduceArr)
    def testFind(self):
        findArr = self._.find(self.test_list, lambda x: x==1)
        return self.assertEqual(1, findArr)
    def testFilter(self):
        filterArr = self._.filter(self.test_list, lambda x: x%2 == 0)
        return self.assertEqual([2,4], filterArr)
    def testReject(self):
        rejectArr = self._.reject(self.test_list, lambda x: x%2 == 0)
        return self.assertEqual([1,3,5], rejectArr)
if __name__ == "__main__":
    unittest.main()
