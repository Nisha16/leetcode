import collections
# def compress(s):
# 	store_freq = {}
# 	temp = collections.OrderedDict()
# 	for ch in s:
# 		try:
# 			temp[ch] += 1	
# 		except:
# 			temp[ch] = 1
# 	result = ''
	
# 	for keys in temp:
# 		result += keys + str(temp[keys])		

# 	return result

def encode(s):
	temp = ''
	count = 0
	result = ''

	for char in s:
		print char
		if temp == '':
			temp = char
			count = 1
		elif temp == char:
			count += 1
		elif temp != char:
			result += temp + str(count)
			count = 1
			temp = char
	result += temp + str(count)
	
	return result

def decode(s):
	result = ''
	for i in range(1,len(s),2):
		result += s[i-1] * int(s[i])
	return result						


print encode('aaabbbabcbcdde')
print decode('a3b3a1b1c1b1c1d2e1')
