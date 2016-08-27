class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        ret = list(self.nums)
        random.shuffle(ret)
        return ret

        #one more method
        # output = self.nums[:]
        # n = len(output)
        # for x in xrange(n):
        #     id = random.randint(0, n-1)
        #     output[x], output[id] = output[id], output[x]
        # return output