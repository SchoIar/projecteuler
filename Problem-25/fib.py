# Anton Ilic, Apr 14, 2023
# https://projecteuler.net/problem=25

# F(n) = F(n-1) + F(n-2) where F(0), F(1) = 1
def FindNextFib(FibList):
    '''Finds the next fibonacci number in the list'''
    previousFibIndex = len(FibList) - 1
    FibList.append(int(FibList[previousFibIndex]) + int(FibList[previousFibIndex-1]))
    return FibList

def FindFibonacciOfNLength(n):
    '''Returns index of first Fibonacci number of N length'''
    Elements = [1,1]

    while(len(str(Elements[(len(Elements)) - 1])) < n):
        Elements = FindNextFib(Elements)
        
        
    return len(Elements)

print(FindFibonacciOfNLength(1000))