class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def compare(x,y):
            sx = str(x)
            sy = str(y)
            sx = sx + sy
            sy = sy + sx
            if sx > sy:
                return -1
            if sx == sy:
                return 0
            if sx < sy:
                return 1
        temp = nums
        temp = sorted(temp)
        print "temp: ", temp
            
        nums = sorted(nums, cmp=compare)
        print nums
         
        if nums[0] == 0:
            return "0"
        else:
            return "".join([str(n) for n in nums])
