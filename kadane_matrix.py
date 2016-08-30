def kadane(array):
	max_so_far = 0
	max_end_here = 0
	#below inputs for matrix sum
	current_start = 0
	maxStart = -1
	maxEnd = 0

	allNegative = True

	for i in range(len(array)):
		max_end_here += array[i]

		if max_end_here < 0:
			max_end_here = 0
			current_start = i+1
		if max_so_far < max_end_here:
			max_so_far = max_end_here
			maxEnd = i
			maxStart = current_start

		# if allNegative:
		# 	return "All numbers are negative"
		# else:
	return max_so_far

def max_subarray(A):
   max_so_far = max_ending_here = 0
   for x in A:
       max_ending_here = max(0, max_ending_here + x)
       max_so_far = max(max_so_far, max_ending_here)
   return max_so_far		


#time complexity O(row) and space complexity O(col X col X row)
def matrix_subarray(matrix):
	maxSum = 0
	leftbound = 0
	rightbound = 0
	upperbound = 0
	lowerbound = 0
	kadaneResult = 0

	rows = len(matrix)
	cols = len(matrix[0])

	temp = [0 for x in range(rows)]

	for left in range(cols):
		for i in range(rows):
			temp[i] = 0
			print "temp: ", temp
		for right in range(left, cols):
			for j in range(0, rows):
				temp[j] += matrix[j][right]

			kadaneResult = kadane(temp)

			if kadaneResult > maxSum:
				maxSum = kadaneResult
				leftbound = left
				rightbound = right
				# upperbound = maxStart
				# lowerbound = maxEnd

	return maxSum, leftbound, rightbound
	
matrix = [[2,  1, -3, -4,  5],
		  [0,  6,  3,  4,  1],
		  [2, -2, -1,  4, -5],
		  [-3,  3,  1,  0,  3]]

#matrix = [[1,2,-1, -4, -20], [-8,-3,4,2,1], [3,8,10,1,3],[-4,-1,1,7,-6]]



print matrix_subarray(matrix)		  					



