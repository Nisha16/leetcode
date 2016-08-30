

def unique():
	
	for i in range(1, 100):
		temp = set()
		s = str(i)
		for j in s:
			temp.add(j)
		if len(s) == len(temp):
			print s


print unique()							

