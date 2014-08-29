result = 0

for s in open('passTriangle.txt'): 
	line = ' '.join(list(map(int, s.strip().split())))
	# result += int(s.strip())
	print(line)

# print(result)