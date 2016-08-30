def remove_adjacency(example):
	result = []
	temp = []
	for char in example:
		if len(result) < 1:
			result.append(char)
		else:
			if result[-1] == char:
				temp.append(char)
				#print "temp: ", temp
			else:
				result.append(char)
				if temp:
					if result[-1] != temp[-1]:
						result.append(temp.pop())
				#print "result: ", result


	if len(temp) > 0:
		return "Not possible"


	#for i in range(len(temp)):
	#	result.append(temp.pop())

	return result
	

print ''.join(remove_adjacency('aabbdddxxgddbzzs'))							