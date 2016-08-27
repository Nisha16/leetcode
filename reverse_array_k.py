class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):k = k%len(nums)
        if k == 0:return
        nums[:] = nums[-k:] + nums[:len(nums)-k]