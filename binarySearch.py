def binaryTree_rec(array,key,low,high):
	mid = low + ((high - low)/2)
	if low > high:
		return -1
	if array[mid] == key:
		return mid
	elif key < array[mid]:
		binaryTree_rec(array,key,low,mid - 1)
	else:
		binaryTree_rec(array,key,mid + 1, high)

def binary(arr):
	binaryTree_rec(arr,key,0,len(arr) - 1)

def binary_iter(array,key):
	low = 0
	high = len(array) - 1
	while low <= high:
		mid = low + ((high - low)/2)
		if key == array[mid]:
			return mid
		elif key > array[mid]:
			low = mid + 1
		else:
			high = mid - 1
	return -1
				
		





		
		