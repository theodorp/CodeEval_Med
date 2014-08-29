# MINIMUM COINS
# CHALLENGE DESCRIPTION:

# You are given 3 coins of value 1, 3 and 5. You are also given a total which
# you have to arrive at. Find the minimum number of coins to arrive at it.

# INPUT SAMPLE:
# Your program should accept as its first argument a path to a filename. Each
# line in this file contains a positive integer number which represents the
# total you have to arrive at. E.g.

# 11
# 20

# OUTPUT SAMPLE:
# Print out the minimum number of coins required to arrive at the total. E.g.

# 3
# 4

def minimumCoins(test):

	total_money = int(test.strip())

	coins = [5, 3, 1]

	total_coins = 0

	for coin in coins:
		count = divmod(total_money, coin)[0]
		total_coins += count
		total_money -= count * coin
		if total_money == 0:
			return(total_coins)
			break

test_cases = open('minimumCoins.txt','r')

for test in test_cases:

	print(minimumCoins(test))

test_cases.close()