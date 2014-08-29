# PASS TRIANGLE
# CHALLENGE DESCRIPTION:
# By starting at the top of the triangle and moving to adjacent numbers on the
# row below, the maximum total from top to bottom is 27.

#    5
#   9 6
#  4 6 8
# 0 7 1 5
# 5 + 9 + 6 + 7 = 27

# INPUT SAMPLE:
# Your program should accept as its first argument a path to a filename. Input
# example is the following

# 5
# 9 6
# 4 6 8
# 0 7 1 5

# You make also check full input file which will be used for your code
# evaluation.

# OUTPUT SAMPLE:
# The correct output is the maximum sum for the triangle. So for the given
# example the correct answer would be

# 27

def passTriangle(test):

	line = list(map(int, test.strip().split()))

	position = 0
	prev_position = 0

	for i in range(len(line)):
		if 
			position = line.index(max(line))
			position = prev_position
		return(position)


	# return(line)


test_cases = open('passTriangle.txt','r')

for test in test_cases:

	print(passTriangle(test))

test_cases.close()