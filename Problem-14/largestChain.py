# Anton Ilic, Mar 6, 2023
#https://projecteuler.net/problem=13

#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
longestChainStart = 1; maxChainLength = 1

def collatz(num):
    numCount = 1
    while(num != 1):
        if(num%2 == 0): #Case: Even
            num = int(num / 2)    
        else:
            num = int(3*num + 1)
        numCount += 1
    return numCount

for i in range(1,1000001): #Up to 1 million. 
#to lower being mult.  
    chainLength = collatz(i)
    if (maxChainLength < chainLength):
        longestChainStart = i
        maxChainLength = chainLength
        print(f"Start: {longestChainStart} Length:{maxChainLength}") 
    i += 1

        
