# PRIME NUMBERS
# CHALLENGE DESCRIPTION:
# Print out the prime numbers less than a given number N. For bonus points your
# solution should run in N*(log(N)) time or better. You may assume that N is
# always a positive integer.

# INPUT SAMPLE:
# Your program should accept as its first argument a path to a filename. Each
# line in this file is one test case. Each test case will contain an integer n <
# 4,294,967,295. E.g.

# 10
# 20
# 100

# OUTPUT SAMPLE:
# For each line of input, print out the prime numbers less than N, in ascending
# order, comma delimited. (There should not be any spaces between the comma and
# numbers) E.g.

# 2,3,5,7
# 2,3,5,7,11,13,17,19
# 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97

def primeNumbers(test):

	n = int(test.strip())

	primes = []
	for num in range(2,n):
		for i in range(2,num):
			if num % i == 0:
				break
		else:
			primes.append(num)
	
	print(','.join(map(str, primes)))

test_cases = open('primeNumbers.txt','r')

for test in test_cases:
	# print(','.join(map(str, primeNumbers(test))))
	primeNumbers(test)

test_cases.close()