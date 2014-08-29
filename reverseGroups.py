# REVERSE GROUPS
# CHALLENGE DESCRIPTION:
# Given a list of numbers and a positive integer k, reverse the elements of
# the list, k items at a time. If the number of elements is not a multiple of
# k, then the remaining items in the end should be left as is.

# INPUT SAMPLE:
# Your program should accept as its first argument a path to a filename. Each
# line in this file contains a list of numbers and the number k, separated by
# a semicolon. The list of numbers are comma delimited. E.g.

# 1,2,3,4,5;2
# 1,2,3,4,5;3

# OUTPUT SAMPLE:
# Print out the new comma separated list of numbers obtained after reversing. E.g.

# 2,1,4,3,5
# 3,2,1,4,5

def reverseGroups(test):

	elements, k = test.strip().split(';')
	# elements = list(map(int, elements.split(',')))
	elements = elements.split(',')

	copy_elements = elements
	k = int(k)

	x = len(elements) // k
	
	for i in range(0, x*k, k):
		b = elements[i:k+i]
		elements[i:i+k] = b[::-1]

	return(elements)



test_cases = open('reverseGroups.txt','r')

for test in test_cases:

	# print(' '.join(map(str, reverseGroups(test))))
	print(','.join(reverseGroups(test)))


test_cases.close()