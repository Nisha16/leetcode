import heapq

def bubble_sort(array):

	for i in range(len(array)):
		for j in range(len(array) - 1 - i):
				if array[j] > array[j+1]:
					array[j],array[j+1] = array[j+1],array[j]

def insertion_sort(array):

	for i in range(1,len(array)):
		j = i
		while j > 0 and array[j] < array[j-1]:
			array[j],array[j-1] = array[j-1],array[j]
			j -= 1	

def merge_sort(array):

	if len(array) > 1:
		mid = len(array) // 2
		left = array[0:mid]
		right = array[mid:]

		merge_sort(left)
		merge_sort(right)

		l,r = 0,0

		for i in range(len(array)):
			lval = left[l] if l < len(left) else None
			rval = right[r] if r < len(right) else None

			if (lval is not None and rval is not None and lval < rval) or rval is None:
				array[i] = lval
				l += 1

			elif (lval is not None and rval is not None and lval >= rval) or lval is None:
				array[i] = rval
				r += 1
			else:
				raise Exception ('Could not merge.')

def quick_sort(array):

	if len(array) > 1:
		pivot = len(array) // 2
		smaller_num = []
		lareger_num = []

		for i, val in enumerate(array):
			if i != pivot:
				if val < array[pivot]:
					smaller_num.append(val)
				else:
					lareger_num.append(val)

		quick_sort(smaller_num)
		quick_sort(lareger_num)
		array[:] = smaller_num + [array[pivot]]	+ lareger_num	

def heap_sort(array):
	heapq.heapify(array)
	array[:] = [heapq.heappop(array) for i in range(len(array))]				



a = [2,7,3,5,1,4,6]
print "a: ", a
#bubble_sort(a)
heap_sort(a)
print "after sort a: ", a					