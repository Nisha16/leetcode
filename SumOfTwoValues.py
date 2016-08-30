def find_sum_two_numbers(array,val):

	found_values = set()
	result = []
	for a in array:
		if val-a in found_values:
			result.append([a,(val-a])
			print "list: ", result
			#return True
		found_values.add(a)
		print "found_values: ", found_values
		
	return result

a = [5,7,1,2,8,4,3]
print "Result: ", find_sum_two_numbers(a,10)			