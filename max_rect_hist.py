def maxRectHistogram(histogram):
	s = [-1]
	# print "first s: ", s
	histogram.append(-1)
	# print "first histo: ", histogram
	ans = 0
	for i in range(len(histogram)):
		# print "histogram[i]: ", histogram[i]
		# print "histogram[s[-1]] ", histogram[s[-1]]
		while histogram[i] < histogram[s[-1]]:
			temp = s.pop()
			# print "for s[-1]: ", s[-1]
			ans = max(ans, histogram[temp] * (i - s[-1] - 1))
			# print "temp ans: ", ans
		s.append(i)
		# print "for s: ", s

	return ans
	

input = [2,1,5,6,2,3]


# Space complexity O(cols) time complexity O(rows X cols)
def maxRectangleBinary(matrix):
	temp = [0] * len(matrix)

	maxArea = 0
	area = 0

	for i in range(len(matrix)):
		for j in range(len(matrix)):
			if matrix[i][j] == 0:
				temp[j] = 0
			else:
				temp[j] += matrix[i][j]
		area = maxRectHistogram(temp)
		if area > maxArea:
			maxArea = area
	return maxArea


def square_submatrix(matrix):

	row = len(matrix)
	col = len(matrix[0])
	result_matrix = [[0 for y in range(col)] for z in range(row)]

	for i in range(len(matrix)):
		result_matrix[i][0] = matrix[i][0]

	for i in range(len(matrix[0])):
		result_matrix[0][i] = matrix[0][i]

	max = 1
	
	for i in range(1, len(matrix)):
		for j in range(1, len(matrix[i])):
			if matrix[i][j] == 0:
				continue

			temp = min(result_matrix[i-1][j],result_matrix[i-1][j-1],result_matrix[i][j-1])	
			result_matrix[i][j] = temp + 1

			if result_matrix[i][j] > max:
				max = result_matrix[i][j]

	return max												


matrix = [[1,1,1,0],
		  [1,1,1,1],
		  [0,1,1,0],
		  [0,1,1,1]]

print "Area of rectangle: ", maxRectangleBinary(matrix)		  

print "maxArea: ", maxRectHistogram(input)

print "Square: ", square_submatrix(matrix)	


			