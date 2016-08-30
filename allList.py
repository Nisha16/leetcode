def find_max_sum_sub_array(A):
	if len(A) < 1:
		return 0

	curr_max = A[0]
	global_max = A[0]
	lengthA = len(A)

	for i in xrange(1, lengthA):
		if curr_max < 0:
			curr_max = A[i]
		else:
			curr_max += A[i]

		if global_max < curr_max:
			global_max = curr_max

	return global_max

def find_max_sum_nonadjacent(A):
	if len(A) < 1:
		return 0

	elif len(A) == 1:
		return A[0]

	lengthA = len(A)
	result = []
	result.append(A[0])

	for i in xrange(1,lengthA):
		result.append(max(A[i], result[i-1]))
		if i-2 >= 0:
			print 
			result[i] = max(result[i], A[i] + result[i-2])
			print "res: ", result	

	return result[lengthA - 1];

def find_max_sum_nonadjacent_own(A):
	if len(A) < 1:
		return 0
	elif len(A) == 1:
		return A[0]

	if len(A) % 2 == 0:
		even_max = 	0
		odd_max = 0
		for i in xrange(1,len(A),2):
			even_max = max(even_max,even_max+A[i-1])
			odd_max = max(odd_max, odd_max+A[i])
			res_max = max(even_max,odd_max)
	else:
		even_max = A[0]
		odd_max = 0
		for i in xrange(2,len(A),2):
			even_max = max(even_max,even_max+A[i])
			odd_max = max(odd_max,odd_max+A[i-1])
			res_max = max(even_max,odd_max)

	return res_max

#Consider a game where a player can score 3(any number) or 5(any number) or 10(any number) points in a move. Given a total score n, 
#find number of ways to reach the given score.


# def scoring_options_rec(n, result):
# 	if n < 0:
# 		return 0

# 	if result[n] > 0:
# 		return result[n]

# 	result[n] = scoring_options_rec(n-3, result) + \
# 				scoring_options_rec(n-5, result) + \
# 				scoring_options_rec(n-10, result)

# 	return result[n]
	
def scoring_options(n):
	if n<=0:
		return 0

	result = [0] * (n+1)
	result[0] = 1

	# scoring_options_rec(n,result)
	for i in range(3, n+1):
		result[i] += result[i-3]
	print "3: ", result
	for i in range(5, n+1):
		result[i] += result[i-5]
	print "5: ", result	
	for i in range(10, n+1):
		result[i] += result[i-10]
	print "10: ", result			

	return result[n]

def coin_change(denominations, amount):
	#solution = list('i', (0 for i in range(0, amount + 1)))
	solution = [0] * (amount + 1)
	print "sol1: ", solution
	solution[0] = 1
	print "sol2: ", solution

	for den in denominations:
		for i in xrange(den, amount + 1):
			solution[i] += solution[i-den]


	return solution[len(solution) - 1]		

	

a = [-4,2,-5,1,2,3,6,-5,1]

b = [1,-1,6,-4,2,2]

c = [1,2,3]

#print "Result: ", find_max_sum_sub_array(a)

#print "Result1: ", find_max_sum_nonadjacent(b)

#print "number of ways to run: ", scoring_options(13)	

print "coin change: ", coin_change(c,4)




