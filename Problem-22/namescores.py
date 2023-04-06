with open("names.txt", "r+") as file:
    for line in file:
        currentLine = line.strip().replace('"','').split(',')
        print(currentLine)