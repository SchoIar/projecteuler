# Anton Ilic, Apr 21, 2023
# https://projecteuler.net/problem=31

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
def count_coin_combinations():
    listOfCombinations = []
    for onePence in range(0, 200):
        print(onePence)
        for twoPence in range(0, 100):
            for fivePence in range(0, 40):
                for tenPence in range(0, 20):
                    for twentyPence in range(0, 10):
                        for fiftyPence in range(0, 4):
                            for pound in range(0, 2):
                                combination = (f'{onePence}{twoPence}{fivePence}{tenPence}{twentyPence}{fiftyPence}{pound}')
                                if combination not in listOfCombinations:
                                    listOfCombinations.append(combination)                            
    #the 8 combinations where it's exclusively one type of coin (ie. 2 x £1 )
    return len(listOfCombinations) + 8

count_coin_combinations()