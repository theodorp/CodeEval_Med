# EMAIL VALIDATION
# CHALLENGE DESCRIPTION:
# You are given several strings that may/may not be valid emails. You should
# write a regular expression that determines if the email id is a valid email
# id or not. You may assume all characters are from the english language.

# INPUT SAMPLE:
# Your program should accept as its first argument a filename. This file will
# contain several text strings, one per line. Ignore all empty lines. E.g.

# foo@bar.com
# this is not an email id
# admin#codeeval.com
# good123@bad.com

# OUTPUT SAMPLE:
# Print out 'true' (all lowercase) if the string is a valid email. Else print
# out 'false' (all lowercase). E.g.

# true
# false
# false
# true

def emailValidation(test):
	import re

	email = test.strip()

	if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
		return('true')
	else:
		return('false')


test_cases = open('emailValidation.txt', 'r')

for test in test_cases:
	if not test.strip():
		continue
	else:
		print(test, emailValidation(test))

	# print(emailValidation(test))

test_cases.close()