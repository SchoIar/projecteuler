# Anton Ilic, Apr 14, 2023
# https://projecteuler.net/problem=25

# F(n) = F(n-1) + F(n-2) where F(0), F(1) = 1
def FindNextFib(FibList):
    previousFibIndex = len(FibList) - 1
    FibList.append(int(FibList[previousFibIndex]) + int(FibList[previousFibIndex-1]))
    return FibList

def FindFibonacciOfNLength(n):
    Elements = [1,1]

    while(len(str(Elements[(len(Elements)) - 1])) < n):
        Elements = FindNextFib(Elements)
        
        
    return Elements

print(FindFibonacciOfNLength(3))