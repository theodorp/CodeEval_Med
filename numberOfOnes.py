# NUMBER OF ONES
# CHALLENGE DESCRIPTION:
# Write a program to determine the number of 1 bits in the internal representation of a given integer.

# INPUT SAMPLE:
# The first argument will be a path to a filename containing an integer, one per line. E.g.

# 10
# 22
# 56

# OUTPUT SAMPLE:
# Print to stdout, the number of ones in the binary form of each number. E.g.

# 2
# 3
# 3

def numberOfOnes(test):
	line = list(bin(int(test.strip()))[2:])
	
	return(line.count('1'))

test_cases = open('numberOfOnes.txt', 'r')
for test in test_cases:
	print(numberOfOnes(test))

test_cases.close()