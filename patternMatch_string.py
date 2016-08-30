def patternmatch(string, pattern):
	m = len(string)
	n = len(pattern)
	print 'n: ', n
	string = list(string)
	occurences = 0
	i = 0
	j = 0
	for var in range(m-n):
		for char in range(j,n):
			if string[char] == pattern[i]:
				i += 1
			elif pattern[i] == '*':
				i += 1
			elif string[char] != pattern[i]:
				i = 0
				break
			if i == n:
				i = 0
				occurences += 1
		string.pop(0)		
		j = 0		
	return occurences			


# string = 'ABCDAABFDFGABCD'
# pattern = 'AB*D'
string = 'AAABBACCC'
pattern = '*A*'

print patternmatch(string, pattern)





