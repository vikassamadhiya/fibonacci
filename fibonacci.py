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