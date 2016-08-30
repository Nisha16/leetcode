def largest_subsequence(list_of_integers):

	length = len(list_of_integers)
	maximum = 0
	maxSumIS = [0 for num in range(length)]
	temp = []

	for i in range(length):
		maxSumIS[i] = list_of_integers[i]

	# Compute maximum sum values in bottom up manner
	for i in range(1, length):
		for j in range(i):
			if list_of_integers[i] > list_of_integers[j] and maxSumIS[i] < maxSumIS[j] + list_of_integers[i]:
				maxSumIS[i] = maxSumIS[j] + list_of_integers[i]
				print "max: ", maxSumIS

	# # Pick maximum of all msis values
	# for i in range(length):
	# 	if maximum < maxSumIS[i]:
	# 		maximum = maxSumIS[i]

	return max(maxSumIS)
	
numbers = [1, 101, 2, 3, 100, 4, 5]

print largest_subsequence(numbers)							

