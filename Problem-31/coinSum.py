# Anton Ilic, Apr 22, 2023
# https://projecteuler.net/problem=31

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).


def bruteforce_count_coin_combinations():
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

# Used chatGPT to generate the following solution:
def count_coin_combinations(coinAmount):

    listOfCombinations = [0] * (coinAmount + 1)
    listOfCombinations[0] = 1
    coins = [1, 2, 5, 10, 20, 50, 100, 200] 
    for coin in coins:
        for i in range(coin, (coinAmount + 1)):
            listOfCombinations[i] += listOfCombinations[i - coin]
    
    return listOfCombinations[coinAmount]

# Define a helper function that calculates the number of combinations for a given amount and coin index.
def count_coin_combinations_helper(amount, index, coins):

    # Base case: If the amount is 0, a valid combination is found, return 1. If the amount is negative or all coins have been iterated through and there is no valid combination, return 0
    if amount == 0:
        return 1
    elif amount < 0 or index >= len(coins):
        return 0

    # Calculate the number of combinations in two ways:
    # 1. Use the current coin and reduce the amount by its value.
    # 2. Don't use the current coin and move on to the next coin.
    using_current_coin = count_coin_combinations_helper(amount - coins[index], index, coins)
    not_using_current_coin = count_coin_combinations_helper(amount, index + 1, coins)

    # Return the total number of combinations found by adding the two possibilities.
    return using_current_coin + not_using_current_coin

def count_coin_combinations():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    coinAmount = 200
    return count_coin_combinations_helper(coinAmount, 0, coins)

if __name__ == '__main__':
    print(count_coin_combinations())
