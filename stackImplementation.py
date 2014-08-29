# STACK IMPLEMENTATION
# CHALLENGE DESCRIPTION:
# Write a program implementing a stack inteface for integers.The interface
# should have 'push' and 'pop' functions. You will be asked to 'push' a series
# of integers and then 'pop' and print out every alternate integer.

# INPUT SAMPLE:
# Your program should accept as its first argument a path to a filename
# containing a series of space delimited integers, one per line. E.g.

# 1 2 3 4
# 10 -2 3 4

# OUTPUT SAMPLE:
# Print to stdout, every alternate integer(space delimited), one per line. E.g.

# 4 2
# 4 -2

test_cases = open('stackImplementation.txt', 'r')
for test in test_cases:
	stack = list(map(int, test.strip().split()))

	for i in range(len(stack)):
		pop = stack.pop()
		if i % 2 == 0:
			
			print(pop, end = ' ')
	print()

test_cases.close()