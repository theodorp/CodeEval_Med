# MTH TO LAST ELEMENT
# CHALLENGE DESCRIPTION:
# Write a program to determine the Mth to last element of a list. 

# INPUT SAMPLE:
# The first argument will be a path to a filename containing a series of space
# delimited characters followed by an integer representing a index into the list
# (1 based), one per line. E.g.

# a b c d 4
# e f g h 2

# OUTPUT SAMPLE:
# Print to stdout, the Mth element from the end of the list, one per line. If
# the index is larger than the list size, ignore that input. E.g.

# a
# g

def mthToLastElement(test):

	line = test.strip().split()

	string, m = line[0:len(line)-1], int(line[len(line)-1])

	n = len(string)

	if m < len(string):
		return(string[n-m])
	# else:	
		# return('')


test_cases = open('mthToLastElement.txt','r')

for test in test_cases:

	if not test.strip():
		continue
	else:
		result = mthToLastElement(test)
		if result is not None:
			print(result)

test_cases.close()