# FIRST NON-REPEATED CHARACTER
# CHALLENGE DESCRIPTION:
# Write a program to find the first non repeated character in a string.

# INPUT SAMPLE:
# The first argument will be a path to a filename containing strings. E.g.

# yellow
# tooth

# OUTPUT SAMPLE:
# Print to stdout, the first non repeating character, one per line. E.g.

# y
# h

test_cases = open('firstNonRepeatedCharacter.txt','r')

for test in test_cases:
	from collections import Counter

	line = test.strip()

	counter = Counter(line)
	

	for char in line:
		if counter[char] == 1:
			print(char)
			break


test_cases.close()