# Anton Ilic, May 4, 2023
# https://projecteuler.net/problem=42
def findWordValue(word):
    wordValue = 0; word = word.lower()
    for digit in word:
         wordValue += ord(digit) - 96
    return wordValue

def readData():
    with open("data.txt", "r+") as file:
            for line in file:
                wordslist = line.strip().replace('"','').split(',')
    return wordslist


