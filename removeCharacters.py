# REMOVE CHARACTERS
# CHALLENGE DESCRIPTION:
# Write a program to remove specific characters from a string.

# INPUT SAMPLE:
# The first argument will be a path to a filename containing an input string
# followed by a comma and then the characters that need to be scrubbed. E.g.

# how are you, abc
# hello world, def

# OUTPUT SAMPLE:
# Print to stdout, the scrubbed strings, one per line. Trim out any
# leading/trailing whitespaces if they occur. E.g.

# how re you
# hllo worl

import sys
test_cases = open('removeCharacters.txt', 'r')
for test in test_cases:

    line, remove = test.strip().split(', ')

    remove = [i for i in remove]

    for char in line:
    	if char in remove:
    		line = line.replace(char,'')

    # line =[line.replace(char,'') for char in line if char in remove]

    print(line)


test_cases.close()