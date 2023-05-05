# Anton Ilic, May 4, 2023
# https://projecteuler.net/problem=42
def findWordValue(word):
    wordValue = 0
    word = word.lower()
    for digit in word:
        wordValue += ord(digit) - 96
    return wordValue


def readData():
    with open("data.txt", "r") as file:
        for line in file:
            wordslist = line.strip().replace('"', '').split(',')
    return wordslist


def convertListOfWordsToNumbers(listOfWords):
    for word in range(0, len(listOfWords)):
        listOfWords[word] = findWordValue(listOfWords[word])
    return listOfWords


def triangleNumberValue(number):
    return (int(0.5 * number * (1 + number)))


def generateTriangleNumbers(maxNumber):
    numbersList = []
    number = 1
    # So that the maximum value appended to the list of triangle numbers is greater then the highest number value of the list of numbers
    while (triangleNumberValue(number - 1) < maxNumber):
        numbersList.append(triangleNumberValue(number))
        number += 1
    return numbersList


def solution():
    numberOfTriangleNumbers = 0
    numbersList = readData()
    numbersList = convertListOfWordsToNumbers(numbersList)
    maxNumber = max(numbersList)
    triangleNumberList = generateTriangleNumbers(maxNumber)

    for number in numbersList:
        if number in triangleNumberList:
            numberOfTriangleNumbers += 1
    return numberOfTriangleNumbers


if __name__ == '__main__':
    triangleWordsForData = solution()
    print(triangleWordsForData)
