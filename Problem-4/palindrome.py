#Anton Ilic, Feb 27, 2023
#https://projecteuler.net/problem=4

#Find the largest palindrome made from the product of two 3-digit numbers.
#ie. 91x99 = 9009

def Reverse(myString):
    #reverse string
    myStringReversed = ''
    for character in myString:
        myStringReversed = character + myStringReversed
    return myStringReversed

def isPalindrome(number):
    if(str(number) == Reverse(str(number))):
        return True
    return False    


#Try all combinations to see which numbers are palindromes, store them in a list, choose the largest.
a = []

for i in range(1, 999):
    for j in range(1, 999):
        product = i * j
        if(isPalindrome(product)):
            a.append(product)

largestElement = 0
for element in a:
    if(largestElement < element):
        largestElement = element

print(largestElement)