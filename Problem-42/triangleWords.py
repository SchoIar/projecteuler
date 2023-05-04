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

def nextTriangleValue(number):
    return (number, int(0.5 * number * (1 + number)))

def generateTriangleNumbers(listOfTriangles, upToNumber):
    if listOfTriangles == []:
         listOfTriangles.append((1, 1))
    maxTuple = listOfTriangles[len(listOfTriangles) - 1] 
    maxKey = maxTuple[0]; maxValue = maxTuple[1]
    while upToNumber > maxKey:
        maxKey += 1
        print(nextTriangleValue(maxKey))
        listOfTriangles.append(nextTriangleValue(maxKey))
    return listOfTriangles

generateTriangleNumbers([(1, 1)], 100)