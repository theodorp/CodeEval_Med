# DECIMAL TO BINARY
# CHALLENGE DESCRIPTION:

# Given a decimal (base 10) number, print out its binary representation.

# INPUT SAMPLE: Your program should accept as its first argument a path to a
# filename containing whole decimal numbers greater or equal to 0, one per
# line.  Ignore all empty lines. E.g.

# 2
# 10
# 67

# OUTPUT SAMPLE:
# Print the binary representation, one per line. E.g.

# 10
# 1010
# 1000011

test_cases = open('decimalToBinary.txt', 'r')
for test in test_cases:

    # line = test.strip()

    
    # print("{0:b}".format(int(test.strip())))
    print(bin(int(test.strip()))[2:])


test_cases.close()