# CASH REGISTER
# CHALLENGE DESCRIPTION:

# The goal of this challenge is to design a cash register program. You will be
# given two float numbers. The first is the purchase price (PP) of the item.
# The second is the cash (CH) given by the customer. Your register currently
# has the following bills/coins within it:

# 'PENNY': .01,
# 'NICKEL': .05,
# 'DIME': .10,
# 'QUARTER': .25,
# 'HALF DOLLAR': .50,
# 'ONE': 1.00,
# 'TWO': 2.00,
# 'FIVE': 5.00,
# 'TEN': 10.00,
# 'TWENTY': 20.00,
# 'FIFTY': 50.00,
# 'ONE HUNDRED': 100.00
# The aim of the program is to calculate the change that has to be returned to the customer.

# INPUT SAMPLE:

# Your program should accept as its first argument a path to a filename. The
# input file contains several lines. Each line is one test case. Each line
# contains two numbers which are separated by a semicolon. The first is the
# Purchase price (PP) and the second is the cash(CH) given by the customer.
# eg.

# 15.94;16.00
# 17;16
# 35;35
# 45;50

# OUTPUT SAMPLE:

# For each set of input produce a single line of output which is the change to
# be returned to the customer. In case the CH < PP, print out ERROR. If CH ==
# PP, print out ZERO. For all other cases print the amount that needs to be
# returned, in terms of the currency values provided. The output should be
# sorted in highest-to-lowest order (DIME,NICKEL,PENNY). eg.


# NICKEL,PENNY
# ERROR
# ZERO
# FIVE

def getChange(change):
	drawer = {
		1: 'PENNY',
		5: 'NICKEL',
		10: 'DIME',
		25: 'QUARTER',
		50: 'HALF DOLLAR',
		100: 'ONE',
		200: 'TWO',
		500: 'FIVE',
		1000: 'TEN',
		2000: 'TWENTY',
		5000: 'FIFTY',
		10000: 'ONE HUNDRED'
		}

	coins = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]

	change = change*100

	coin_return = []
	for i in coins:
		while change >= i:
			change = change - i
			coin_return.append(drawer[i])
	
	return(','.join(coin_return))
	







	return(coin_return)


def cashRegister(test):

	price, paid = map(float, test.strip().split(';'))

	change = round(paid-price, 2)

	if change > 0:
		return(getChange(change))		
	elif change == 0:
		return('ZERO')
	else:
		return('ERROR')


test_cases = open('cashRegister.txt', 'r')
for test in test_cases:

	print(cashRegister(test))

test_cases.close()