# Python Fibonacci Sequence Function

The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it.
We will now calculate this using Python.

Code for calulating series is written in fibonacci.py

```
# Fibonacci numbers module
def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(a)
        a, b = b, a+b
    return result

def main():
    print (fib2(30))

if __name__ == '__main__' : main()
```

On execution of fibonacci.py, Output is 
```
C:\Users\visamadh\git\fibonacci>python fibonacci.py
[0, 1, 1, 2, 3, 5, 8, 13]
```

Code for Unit Test is written in fibonacciUnitTest.py
```
import fibonacci
import unittest

class TestFibonacciFunctions(unittest.TestCase):


    def test_series_30(self):
        print('\nTest Series 30')
        wanted_result = [0,1,1,2,3,5,8,13]
        test_result = fibonacci.fib2(30)
        self.assertEqual(wanted_result,test_result)
        

if __name__ == '__main__' : unittest.main()
```
On execution of fibonacciUnitTest.py, Output is
```
C:\Users\visamadh\git\fibonacci>python fibonacciUnitTest.py

Test Series 30
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```
