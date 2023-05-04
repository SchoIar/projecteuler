with open("data.txt", "r+") as file:
        for line in file:
            wordslist = line.strip().replace('"','').split(',')
