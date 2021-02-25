import fibonacci
import unittest

class TestFibonacciFunctions(unittest.TestCase):


    def test_series_30(self):
        print('\nTest Series 30')
        wanted_result = [0,1,1,2,3,5,8,13]
        test_result = fibonacci.fib2(30)
        self.assertEqual(wanted_result,test_result)
        print('Results Matched')

if __name__ == '__main__' : unittest.main()