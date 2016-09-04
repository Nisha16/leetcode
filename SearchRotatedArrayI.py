class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1;
        targetInRotated = target>=nums[0]
        print "targetInRotated: ", targetInRotated
        begin = 0
        end = len(nums)-1
        while begin<=end:
            midpoint = (begin+end)//2
            if nums[midpoint]==target:
                return midpoint
            if targetInRotated and nums[midpoint]<nums[0]:
                end= midpoint - 1
            elif (not targetInRotated) and nums[midpoint]>=nums[0]:
                begin = midpoint + 1
            elif nums[midpoint]<target:
                begin = midpoint + 1
            else:
                end = midpoint - 1
        return -1
