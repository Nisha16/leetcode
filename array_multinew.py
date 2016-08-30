def arrayMulti(array):
	output = array
	multi = array
	for i in range(0,4):
		temp = 1
		for j in range(0,4):
			if array[j] != output[i]:
				print 'array: ', array[j]

				temp = array[j] * temp
				print 'temp:' , temp
			else:
				continue
		multi[i] = temp		
	print multi	

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len (nums)
        Output = [ 1 ] * size
        left = 1 
        for index in range (size - 1):
            left *= nums[index]
            print 'l:', left
            Output[index + 1 ] *= left
            print 'Out: ', Output
        print Output
        right = 1 
        for i in range (size - 1 , 0 , - 1 ):
            right *= nums [i]
            print 'r: ', right
            Output[i - 1 ] *= right
            print 'out2: ', Output
        print 'result: ', Output    
        return Output 			

arr = [1,2,3,4]
arrayMulti(arr)		